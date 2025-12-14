"""
serialization.py
Module containing functions to serialize statistics from the history database.
"""
import os
import json
import shutil
import calendar


def export_statistics(titles, artists, genres, counts, durations, months, days, year):
    result = {
        "summary": {
            "items": {
                "total_unique_titles": counts["total_unique_titles"],
                "total_unique_artists": counts["total_unique_artists"],
                "total_unique_genres": counts["total_unique_genres"],
            },
            "counts": {
                "average_daily_count": round(int(counts["average_daily_count"])),
                "average_monthly_count": round(int(counts["average_monthly_count"])),
                "total_count": counts["total_count"],
            },
            "durations": {
                "average_daily_duration": round(int(durations["average_daily_duration"]) / 60),
                "average_monthly_duration": round(int(durations["average_monthly_duration"]) / 60),
                "total_duration": round(int(durations["total_duration"]) / 60),
            },
        },

        "top": {
            "titles": [],
            "artists": [],
            "genres": [],
        },

        "calendar": {
            "months": {}
        }
    }

    # TOP
    for item in titles[:5]:
        result["top"]["titles"].append({
            "title": item["title"],
            "artist": item["artist"],
            "times": item["times"],
        })

    for item in artists[:5]:
        result["top"]["artists"].append({
            "artist": item["artist"],
            "duration": int(int(item["length"]) / 60),
        })

    for item in genres[:5]:
        result["top"]["genres"].append({
            "genre": item["genre"],
            "duration": int(int(item["length"]) / 60),
        })

    # CALENDAR
    for i in range(12):
        month_key = f"{i + 1:02d}"

        result["calendar"]["months"][month_key] = {
            "summary": {
                "top_artist": None,
                "duration": 0,
                "total_count": 0,
                "total_duration": 0,
            },
            "days": {}
        }

        days_in_month = calendar.monthrange(int(year), int(month_key))[1]

        for day in range(1, days_in_month + 1):
            day_key = f"{day:02d}"

            result["calendar"]["months"][month_key]["days"][day_key] = {
                "top_artist": None,
                "duration": 0,
                "total_count": 0,
                "total_duration": 0,
            }

    # MONTHS
    for i in range(len(months["monthly_total"])):
        month_key = months["monthly_total"][i]["month"][5:]

        result["calendar"]["months"][month_key]["summary"] = {
            "top_artist": months["monthly_top_artist"][i]["artist"],
            "duration": round(int(months["monthly_top_artist"][i]["duration"]) / 60),
            "total_count": int(months["monthly_total"][i]["count"]),
            "total_duration": round(int(months["monthly_total"][i]["duration"]) / 60),
        }

    # DAYS
    for i in range(len(days["daily_total"])):
        full_day = days["daily_total"][i]["day"]
        month_key = full_day[5:7]
        day_key = full_day[8:]

        result["calendar"]["months"][month_key]["days"][day_key] = {
            "top_artist": days["daily_top_artist"][i]["artist"],
            "duration": round(int(days["daily_top_artist"][i]["duration"]) / 60),
            "total_count": int(days["daily_total"][i]["count"]),
            "total_duration": round(int(days["daily_total"][i]["duration"]) / 60),
        }

    base = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(base, "..", "data", "exports")
    os.makedirs(path, exist_ok=True)

    with open(f"{path}/{year}.json", "w", encoding="utf-8") as file:
        json.dump(result, file, ensure_ascii=False, indent=4)


def copy_statistics(year):
    base = os.path.dirname(os.path.realpath(__file__))
    src_path = os.path.join(base, "..", "data", "exports")
    dst_path = os.path.join(base, "..", "web", "public", "exports")
    os.makedirs(dst_path, exist_ok=True)

    files = [
        f"{year}.json",
        "index.json",
    ]

    for filename in files:
        src_file = os.path.join(src_path, filename)
        dst_file = os.path.join(dst_path, filename)
        
        if os.path.exists(src_file):
            shutil.copy2(src_file, dst_file)


def update_index(year):
    base = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(base, "..", "data", "exports")
    os.makedirs(path, exist_ok=True)

    index_path = os.path.join(path, "index.json")
    year_path = os.path.join(path, f"{year}.json")
    
    year = int(year)

    data = {
        "years": []
    }

    if os.path.exists(year_path):
        if os.path.exists(index_path):
            with open(index_path, "r", encoding="utf-8") as file:
                try:
                    data = json.load(file)
                except json.JSONDecodeError:
                    pass

        if year not in data.get("years", []):
            data["years"].append(year)
            data["years"].sort()

        with open(index_path, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)


def show_statistics(titles, artists, genres, counts, durations, months):
    print("--------------------------------------------------------------------------------------")
    for item in titles:
        print(f"{item['artist']}: {item['title']}".ljust(75), f"({item['times']})".rjust(10))
    print("--------------------------------------------------------------------------------------")
    for item in artists:
        length = int(int(item['length']) / 60)
        print(f"{item['artist']}:".ljust(75), f"{length} minutes".rjust(10))
    print("--------------------------------------------------------------------------------------")
    for item in genres:
        length = int(int(item['length']) / 60)
        print(f"{item['genre']}:".ljust(75), f"{length} minutes".rjust(10))
    print("--------------------------------------------------------------------------------------")

    print(f"{counts["total_unique_titles"]} total unique titles")
    print(f"{counts["total_unique_artists"]} total unique artists")
    print(f"{counts["total_unique_genres"]} total unique genres")

    print(f"{round(int(counts["average_daily_count"]))} average daily count")
    print(f"{round(int(counts["average_monthly_count"]))} average monthly count")
    print(f"{counts["total_count"]} total count")

    print(f"{round(int(durations["average_daily_duration"]) / 60)} average daily duration")
    print(f"{round(int(durations["average_monthly_duration"]) / 60)} average monthly duration")
    print(f"{int(int(durations["total_duration"]) / 60)} minutes", end="\n\n")

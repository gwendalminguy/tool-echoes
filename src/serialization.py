"""
serialization.py
Module containing functions to serialize statistics from the history database.
"""
import os
import json


def export_statistics(titles, artists, genres, counts, durations, year):
    result = {
        "counts": {
            "total_unique_titles": counts["total_unique_titles"],
            "total_unique_artists": counts["total_unique_artists"],
            "total_unique_genres": counts["total_unique_genres"],
            "average_daily_count": round(int(counts["average_daily_count"]))
        },
        "durations": {
            "average_daily_duration": round(int(durations["average_daily_duration"]) / 60),
            "total_duration": round(int(durations["total_duration"]) / 60)
        },
        "titles": {},
        "artists": {},
        "genres": {}
    }

    for i in range(5):
        try:
            result["titles"]["title_" + str(i + 1)] = {
                "title": titles[i]["title"],
                "artist": titles[i]["artist"],
                "times": titles[i]["times"]
            }
        except IndexError:
            pass
        try:
            result["artists"]["artist_" + str(i + 1)] = {
                "artist": artists[i]["artist"],
                "length": int(int(artists[i]['length']) / 60)
            }
        except IndexError:
            pass
        try:
            result["genres"]["genre_" + str(i + 1)] = {
                "genre": genres[i]["genre"],
                "length": int(int(genres[i]['length']) / 60)
            }
        except IndexError:
            pass

    base = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(base, "..", "data", "exports")
    os.makedirs(path, exist_ok=True)

    with open(f"{path}/{year}.json", "w", encoding="utf-8") as file:
        json.dump(result, file, ensure_ascii=False, indent=4)


def show_statistics(titles, artists, genres, counts, durations):
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
    print(f"{round(int(durations["average_daily_duration"]) / 60)} average daily duration", end="\n\n")
    print(f"{int(int(durations["total_duration"]) / 60)} minutes")

#!/usr/bin/python3
import os
import json
from datetime import datetime
from analyze import top_titles, top_artists, top_genres, total_unique_titles, total_unique_artists, total_unique_genres, total_duration


def main():
    titles = top_titles()
    artists = top_artists()
    genres = top_genres()

    count = {
        "total_titles": total_unique_titles(),
        "total_artists": total_unique_artists(),
        "total_genres": total_unique_genres(),
        "total_duration": total_duration()
    }

    export_statistics(titles, artists, genres, count)
    show_statistics(titles, artists, genres, count)


def export_statistics(titles, artists, genres, count):
    year = str(datetime.now().year)

    result = {
        "count": {
            "total_titles": count["total_titles"],
            "total_artists": count["total_artists"],
            "total_genres": count["total_genres"],
            "total_duration": int(int(count["total_duration"]) / 60)
        }
    }

    for i in range(5):
        result["title_" + str(i + 1)] = {
            "title": titles[i]["title"],
            "artist": titles[i]["artist"],
            "times": titles[i]["times"]
        }
        result["artist_" + str(i + 1)] = {
            "artist": artists[i]["artist"],
            "length": int(int(artists[i]['length']) / 60)
        }
        result["genre_" + str(i + 1)] = {
            "genre": genres[i]["genre"],
            "length": int(int(genres[i]['length']) / 60)
        }

    if not os.path.exists("archives/"):
        os.mkdir("archives")
    with open(f"archives/{year}.json", "w", encoding="utf-8") as file:
        json.dump(result, file, ensure_ascii=False, indent=4)


def show_statistics(titles, artists, genres, count):
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
    print(f"{count["total_titles"]} titles")
    print(f"{count["total_artists"]} artists")
    print(f"{count["total_genres"]} genres")
    print(f"{int(int(count["total_duration"]) / 60)} minutes", end="\n\n")


if __name__ == "__main__":
    main()

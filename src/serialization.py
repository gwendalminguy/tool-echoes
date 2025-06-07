#!/usr/bin/python3
"""
Module containing functions to serialize statistics from the history database.
"""
import os
import json


def export_statistics(titles, artists, genres, count, year):
    result = {
        "count": {
            "total_titles": count["total_titles"],
            "total_artists": count["total_artists"],
            "total_genres": count["total_genres"],
            "total_duration": int(int(count["total_duration"]) / 60)
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
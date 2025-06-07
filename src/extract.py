#!/usr/bin/python3
"""
extract.py
Script to extract statistics in JSON format.
"""
import os
import json
import argparse
from datetime import datetime
from analyze import top_titles, top_artists, top_genres, total_unique_titles, total_unique_artists, total_unique_genres, total_duration
from serialization import export_statistics, show_statistics


def main():
    current = str(datetime.now().year)

    parser = argparse.ArgumentParser()
    parser.add_argument("-y", "--year", default=current, type=str, help="year to process")
    args = parser.parse_args()
    year = (args.year).lower()

    titles = top_titles(year)
    artists = top_artists(year)
    genres = top_genres(year)
    count = {
        "total_titles": total_unique_titles(year),
        "total_artists": total_unique_artists(year),
        "total_genres": total_unique_genres(year),
        "total_duration": total_duration(year)
    }

    export_statistics(titles, artists, genres, count, year)
    #show_statistics(titles, artists, genres, count)


if __name__ == "__main__":
    main()

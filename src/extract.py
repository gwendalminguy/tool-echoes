#!/usr/bin/python3
"""
extract.py
Script to extract statistics in JSON format.
"""
import os
import json
import argparse
from datetime import datetime
from analyze import top_titles, top_artists, top_genres
from analyze import total_unique_titles, total_unique_artists, total_unique_genres, average_daily_count, total_count
from analyze import average_daily_duration, total_duration
from serialization import export_statistics, show_statistics
from management import initialize_history


def main():
    current = str(datetime.now().year)

    parser = argparse.ArgumentParser()
    parser.add_argument("-y", "--year", default=current, type=str, help="year to process")
    args = parser.parse_args()
    year = (args.year).lower()

    initialize_history()

    titles = top_titles(year)
    artists = top_artists(year)
    genres = top_genres(year)
    counts = {
        "total_unique_titles": total_unique_titles(year),
        "total_unique_artists": total_unique_artists(year),
        "total_unique_genres": total_unique_genres(year),
        "average_daily_count": average_daily_count(year),
        "total_count": total_count(year)
    }
    durations = {
        "average_daily_duration": average_daily_duration(year),
        "total_duration": total_duration(year)
    }

    export_statistics(titles, artists, genres, counts, durations, year)
    # show_statistics(titles, artists, genres, counts, durations)


if __name__ == "__main__":
    main()

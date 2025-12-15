#!/usr/bin/python3
"""
extract.py
Script to extract statistics in JSON format.
"""
import os
import json
import argparse
from datetime import datetime

from analyze import top_titles, top_artists, top_genres, top_albums
from analyze import total_unique_titles, total_unique_artists, total_unique_genres, total_unique_albums
from analyze import average_daily_count, average_monthly_count, total_count
from analyze import average_daily_duration, average_monthly_duration, total_duration
from analyze import monthly_top_artist, monthly_total, daily_average
from analyze import daily_top_artist, daily_total

from serialization import export_statistics, copy_statistics, update_index, show_statistics
from management import initialize_history


def main():
    current_year = datetime.now().year
    parser = argparse.ArgumentParser()
    parser.add_argument("-y", "--year", default=current_year, type=int, help="year to process")
    args = parser.parse_args()
    year = (str('{:04}'.format(args.year))).lower()

    initialize_history()

    limit = 25

    titles = top_titles(year, limit)
    artists = top_artists(year, limit)
    genres = top_genres(year, limit)
    albums = top_albums(year, limit)
    items = {
        "total_unique_titles": total_unique_titles(year),
        "total_unique_artists": total_unique_artists(year),
        "total_unique_genres": total_unique_genres(year),
        "total_unique_albums": total_unique_albums(year)
    }
    counts = {
        "average_daily_count": average_daily_count(year),
        "average_monthly_count": average_monthly_count(year),
        "total_count": total_count(year)
    }
    durations = {
        "average_daily_duration": average_daily_duration(year),
        "average_monthly_duration": average_monthly_duration(year),
        "total_duration": total_duration(year)
    }
    months = {
        "monthly_top_artist": monthly_top_artist(year),
        "monthly_total": monthly_total(year), 
        "daily_average": daily_average(year)
    }
    days = {
        "daily_top_artist": daily_top_artist(year),
        "daily_total": daily_total(year)
    }

    export_statistics(titles, artists, genres, albums, items, counts, durations, months, days, year)
    update_index(year)
    copy_statistics(year)

    # show_statistics(titles, artists, genres, counts, durations, months)


if __name__ == "__main__":
    main()

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
from analyze import total_unique_titles, total_unique_artists, total_unique_genres, average_daily_count, average_monthly_count, total_count
from analyze import average_daily_duration, average_monthly_duration, total_duration
from analyze import maximum_activity_day, maximum_activity_month
from analyze import monthly_top_artist

from serialization import export_statistics, show_statistics
from management import initialize_history


def main():
    current_year = datetime.now().year
    current_month = datetime.now().month

    parser = argparse.ArgumentParser()
    parser.add_argument("-y", "--year", default=current_year, type=int, help="year to process")
    parser.add_argument("-m", "--month", default=current_month, type=int, help="month to process")
    args = parser.parse_args()
    year = (str('{:04}'.format(args.year))).lower()
    month = (str('{:02}'.format(args.month))).lower()

    initialize_history()

    titles = top_titles(year)
    artists = top_artists(year)
    genres = top_genres(year)
    counts = {
        "total_unique_titles": total_unique_titles(year),
        "total_unique_artists": total_unique_artists(year),
        "total_unique_genres": total_unique_genres(year),
        "average_daily_count": average_daily_count(year),
        "average_monthly_count": average_monthly_count(year),
        "total_count": total_count(year)
    }
    durations = {
        "average_daily_duration": average_daily_duration(year),
        "average_monthly_duration": average_monthly_duration(year),
        "total_duration": total_duration(year)
    }
    activity = {
        "maximum_activity_day": maximum_activity_day(year),
        "maximum_activity_month": maximum_activity_month(year)
    }
    months = {
        "monthly_top_artist": monthly_top_artist(year, month)
    }

    export_statistics(titles, artists, genres, counts, durations, activity, months, year, month)
    # show_statistics(titles, artists, genres, counts, durations, activity, months)


if __name__ == "__main__":
    main()

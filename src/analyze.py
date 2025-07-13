"""
analyze.py
Module containing functions to analyze the history database.
"""
import sys
import os
import sqlite3
from datetime import datetime


DB_PATH = os.path.dirname(os.path.realpath(__file__)) + "/../data/history.db"


def top_titles(year):
    """
    Computes top titles ordered by occurences.

    Return: dictionary of result
    """
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute(f"""
        SELECT title, artist, COUNT(title) as times
        FROM listen
        WHERE strftime('%Y', date)='{year}'
        GROUP BY title
        ORDER BY times DESC
        LIMIT 5
    """)
    items = cursor.fetchall()
    connection.close()

    if len(items) == 0:
        sys.exit(f"No Data ({year})")
    return items


def top_artists(year):
    """
    Computes top artists ordered by total duration.

    Return: dictionary of result
    """
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute(f"""
        SELECT artist, duration, SUM(duration) as length
        FROM listen
        WHERE strftime('%Y', date)='{year}'
        GROUP BY artist
        ORDER BY length DESC
        LIMIT 5
    """)
    items = cursor.fetchall()
    connection.close()

    if len(items) == 0:
        sys.exit(f"No Data ({year})")
    return items


def top_genres(year):
    """
    Computes top genres ordered by total duration.

    Return: dictionary of result
    """
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute(f"""
        SELECT genre, duration, SUM(duration) as length
        FROM listen
        WHERE strftime('%Y', date)='{year}'
        GROUP BY genre
        ORDER BY length DESC
        LIMIT 5
    """)
    items = cursor.fetchall()
    connection.close()

    if len(items) == 0:
        sys.exit(f"No Data ({year})")
    return items


def total_unique_titles(year):
    """
    Computes total unique titles count.

    Return: total count
    """
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute(f"""
        SELECT COUNT(title)
        FROM (
            SELECT DISTINCT title, artist
            FROM listen
            WHERE strftime('%Y', date)='{year}'
        )
    """)
    count = cursor.fetchone()[0]
    connection.close()

    if count == 0:
        sys.exit(f"No Data ({year})")
    return count


def total_unique_artists(year):
    """
    Computes total unique artists count.

    Return: total count
    """
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute(f"""
        SELECT COUNT(DISTINCT artist)
        FROM listen
        WHERE strftime('%Y', date)='{year}'
    """)
    count = cursor.fetchone()[0]
    connection.close()

    if count == 0:
        sys.exit(f"No Data ({year})")
    return count


def total_unique_genres(year):
    """
    Computes total unique genres count.

    Return: total count
    """
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute(f"""
        SELECT COUNT(DISTINCT genre)
        FROM listen
        WHERE strftime('%Y', date)='{year}'
    """)
    count = cursor.fetchone()[0]
    connection.close()

    if count == 0:
        sys.exit(f"No Data ({year})")
    return count


def total_duration(year):
    """
    Computes total duration.

    Return: total duration
    """
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute(f"""
        SELECT SUM(duration)
        FROM listen
        WHERE strftime('%Y', date)='{year}'
    """)
    duration = cursor.fetchone()[0]
    connection.close()

    if duration == 0:
        sys.exit(f"No Data ({year})")
    return duration


def average_daily_titles(year):
    """
    Computes daily titles average.

    Return: daily titles average
    """
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute(f"""
        SELECT AVG(count)
        FROM (
            SELECT COUNT(*) as count
            FROM listen
            WHERE strftime('%Y', date)='{year}'
            GROUP BY DATE(date)
        )
    """)
    average = cursor.fetchone()[0]
    connection.close()

    if average == 0:
        sys.exit(f"No Data ({year})")
    return average

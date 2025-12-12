"""
analyze.py
Module containing functions to analyze the history database.
"""
import sys
import os
import sqlite3
from datetime import datetime


DB_PATH = os.path.dirname(os.path.realpath(__file__)) + "/../data/history.db"


# ---------- TOP ----------

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
        GROUP BY artist, title
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


# ---------- COUNTS ----------

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


def average_daily_count(year):
    """
    Computes average daily count.

    Return: average daily count
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
    count = cursor.fetchone()[0]
    connection.close()

    if count == 0:
        sys.exit(f"No Data ({year})")
    return count


def average_monthly_count(year):
    """
    Computes average monthly count.

    Return: average monthly count
    """
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute(f"""
        SELECT AVG(count) FROM (
            SELECT COUNT(*) as count
            FROM listen
            WHERE strftime('%Y', date)='{year}'
            GROUP BY strftime('%m', date)
        )
    """)
    count = cursor.fetchone()[0]
    connection.close()

    if count == 0:
        sys.exit(f"No Data ({year})")
    return count


def total_count(year):
    """
    Computes total count.

    Return: total count
    """
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute(f"""
        SELECT COUNT(*)
        FROM listen
        WHERE strftime('%Y', date)='{year}'
    """)
    count = cursor.fetchone()[0]
    connection.close()

    if count == 0:
        sys.exit(f"No Data ({year})")
    return count


# ---------- DURATIONS ----------

def average_daily_duration(year):
    """
    Computes daily average duration.

    Return: daily average duration in seconds
    """
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute(f"""
        SELECT AVG(daily_duration)
        FROM (
            SELECT SUM(duration) as daily_duration
            FROM listen
            WHERE strftime('%Y', date)='{year}'
            GROUP BY DATE(date)
        )
    """)
    duration = cursor.fetchone()[0]
    connection.close()

    if duration == 0:
        sys.exit(f"No Data ({year})")
    return duration


def average_monthly_duration(year):
    """
    Computes monthly average duration.

    Return: monthly average duration in seconds
    """
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute(f"""
        SELECT AVG(monthly_duration)
        FROM (
            SELECT SUM(duration) as monthly_duration
            FROM listen
            WHERE strftime('%Y', date)='{year}'
            GROUP BY strftime('%m', date)
        )
    """)
    duration = cursor.fetchone()[0]
    connection.close()

    if duration == 0:
        sys.exit(f"No Data ({year})")
    return duration


def total_duration(year):
    """
    Computes total duration.

    Return: total duration in seconds
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


# ---------- MONTHS ----------

def monthly_top_artist(year, month):
    """
    Computes monthly top artist.

    Return: artist, duration and date of monthly top artist.
    """
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    activity = {}

    for i in range(int(month)):
        current = str('{:02}'.format(i + 1))
        cursor.execute(f"""
            SELECT artist, SUM(duration) as duration
            FROM listen
            WHERE strftime('%Y-%m', date)='{year}-{current}'
            GROUP BY artist
            ORDER BY duration DESC
            LIMIT 1
        """)
        result = cursor.fetchone()
        if result:
            activity[current] = result[0:]

    connection.close()

    if activity == 0:
        sys.exit(f"No Data ({year}-{month})")
    return activity


def monthly_total_duration(year, month):
    """
    Computes monthly total duration.

    Return: monthly total duration and date.
    """
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    activity = {}

    for i in range(int(month)):
        current = str('{:02}'.format(i + 1))
        cursor.execute(f"""
            SELECT SUM(duration), strftime('%Y-%m', date) as month
            FROM listen
            WHERE month='{year}-{current}'
            GROUP BY month
            LIMIT 1
        """)
        result = cursor.fetchone()
        if result:
            activity[current] = result[0:]

    connection.close()

    if activity == 0:
        sys.exit(f"No Data ({year}-{month})")
    return activity

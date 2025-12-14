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

def top_titles(year, limit):
    """
    Computes top titles ordered by occurences.

    Return: dictionary of result
    """
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute(f"""
        SELECT title, artist, COUNT(title) AS times
        FROM listen
        WHERE strftime('%Y', date)='{year}'
        GROUP BY artist, title
        ORDER BY times DESC
        LIMIT '{limit}'
    """)
    items = cursor.fetchall()
    connection.close()

    if len(items) == 0:
        sys.exit(f"No Data ({year})")
    return items


def top_artists(year, limit):
    """
    Computes top artists ordered by total duration.

    Return: dictionary of result
    """
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute(f"""
        SELECT artist, duration, SUM(duration) AS length
        FROM listen
        WHERE strftime('%Y', date)='{year}'
        GROUP BY artist
        ORDER BY length DESC
        LIMIT '{limit}'
    """)
    items = cursor.fetchall()
    connection.close()

    if len(items) == 0:
        sys.exit(f"No Data ({year})")
    return items


def top_genres(year, limit):
    """
    Computes top genres ordered by total duration.

    Return: dictionary of result
    """
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute(f"""
        SELECT genre, duration, SUM(duration) AS length
        FROM listen
        WHERE strftime('%Y', date)='{year}'
        GROUP BY genre
        ORDER BY length DESC
        LIMIT '{limit}'
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
            SELECT COUNT(*) AS count
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
            SELECT COUNT(*) AS count
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
            SELECT SUM(duration) AS daily_duration
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
            SELECT SUM(duration) AS monthly_duration
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

def monthly_top_artist(year):
    """
    Computes monthly top artist.

    Return: artist, duration and date of monthly top artist.
    """
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    cursor.execute(f"""
        SELECT artist, duration, month
        FROM (
            SELECT artist, SUM(duration) AS duration, strftime('%Y-%m', date) AS month, ROW_NUMBER() OVER (
                PARTITION BY strftime('%Y-%m', date)
                ORDER BY SUM(duration) DESC
            ) AS rank
            FROM listen
            WHERE strftime('%Y', date)='{year}'
            GROUP BY month, artist
        )
        WHERE rank = 1
        ORDER BY month;
    """)
    items = cursor.fetchall()

    connection.close()

    if len(items) == 0:
        sys.exit(f"No Data ({year})")
    return items


def monthly_total(year):
    """
    Computes monthly total count and duration.

    Return: monthly total count, duration and date.
    """
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    cursor.execute(f"""
        SELECT COUNT(*) AS count, SUM(duration) AS duration, strftime('%Y-%m', date) AS month
        FROM listen
        WHERE strftime('%Y', date)='{year}'
        GROUP BY month
    """)
    items = cursor.fetchall()

    connection.close()

    if len(items) == 0:
        sys.exit(f"No Data ({year})")
    return items


# ---------- DAYS ----------

def daily_top_artist(year):
    """
    Computes daily top artist.

    Return: artist, duration and date of daily top artist.
    """
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    cursor.execute(f"""
        SELECT artist, duration, day
        FROM (
            SELECT artist, SUM(duration) AS duration, strftime('%Y-%m-%d', date) AS day, ROW_NUMBER() OVER (
                PARTITION BY strftime('%Y-%m-%d', date)
                ORDER BY SUM(duration) DESC
            ) AS rank
            FROM listen
            WHERE strftime('%Y', date)='{year}'
            GROUP BY day, artist
        )
        WHERE rank = 1
        ORDER BY day;
    """)
    items = cursor.fetchall()

    connection.close()

    if len(items) == 0:
        sys.exit(f"No Data ({year})")
    return items


def daily_total(year):
    """
    Computes daily total count and duration.

    Return: daily total count, duration and date.
    """
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    cursor.execute(f"""
        SELECT COUNT(*) AS count, SUM(duration) AS duration, strftime('%Y-%m-%d', date) AS day
        FROM listen
        WHERE strftime('%Y', date)='{year}'
        GROUP BY day
    """)
    items = cursor.fetchall()

    connection.close()

    if len(items) == 0:
        sys.exit(f"No Data ({year})")
    return items

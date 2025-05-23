import sqlite3
from datetime import datetime
"""
analyze.py
Module containing functions to analyze the history database.
"""
DB_PATH = "history.db"
year = str(datetime.now().year)


def top_titles():
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

    return items


def top_artists():
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

    return items


def top_genres():
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

    return items


def total_unique_titles():
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

    return count


def total_unique_artists():
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

    return count

def total_unique_genres():
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

    return count


def total_duration():
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
    print(duration)
    return duration

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
    Displays titles ordered by occurences.

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
    
    for item in items:
        print(f"{item['artist']}: {item['title']}".ljust(75), f"({item['times']})".rjust(10))

    return items


def top_artists():
    """
    Displays artists ordered by total duration.

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
    
    for item in items:
        length = int(int(item['length']) / 60)
        print(f"{item['artist']}:".ljust(75), f"{length} minutes".rjust(10))

    return items


def top_genres():
    """
    Displays genres ordered by total duration.

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
    
    for item in items:
        length = int(int(item['length']) / 60)
        print(f"{item['genre']}:".ljust(75), f"{length} minutes".rjust(10))

    return items


def total_unique_titles():
    """
    Displays total unique titles count.

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

    return count


def total_unique_artists():
    """
    Displays total unique artists count.

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

    return count

def total_unique_genres():
    """
    Displays total unique genres count.

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

    return count

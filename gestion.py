import sqlite3
from datetime import datetime
"""
gestion.py
Module containing functions to manage the history database.
"""
DB_PATH = "history.db"


def initialize_history():
    """
    Initializes a listen table in history database.
    """
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS listen (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            artist TEXT,
            album TEXT,
            year INTEGER,
            genre TEXT,
            date DATETIME DEFAULT CURRENT_TIMESTAMP,
            duration INTEGER
            )
        """)
    connection.commit()
    connection.close()


def delete_history():
    """
    Deletes a listen table from history database.
    """
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    cursor.execute("""
        DROP TABLE listen
        """)
    connection.close()


def log_listen(title, artist, album, year, genre, duration):
    """
    Logs an entry in a listen table.
    """
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    cursor.execute("""
        INSERT INTO listen (title, artist, album, year, genre, duration, date)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (title, artist, album, year, genre, duration, datetime.now()))
    connection.commit()
    connection.close()

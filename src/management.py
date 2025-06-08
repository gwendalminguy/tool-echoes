"""
management.py
Module containing functions to manage the history database.
"""
import os
import subprocess
import sqlite3
from datetime import datetime


DB_PATH = os.path.dirname(os.path.realpath(__file__)) + "/../data/history.db"


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
    connection.commit()
    connection.close()


def get_listen():
	applescript = """
	tell application "Music"
		if player state is playing then
			set trackName to get name of current track
			set artistName to get album artist of current track
			set albumName to get album of current track
			set albumYear to get year of current track
			set trackGenre to get genre of current track
			set trackDuration to get duration of current track
			return trackName & "|||" & artistName & "|||" & albumName & "|||" & albumYear & "|||" & trackGenre & "|||" & trackDuration
		end if
	end tell
	"""

	try:
		result = subprocess.run(["osascript", "-e", applescript], capture_output=True, text=True)
	except FileNotFoundError:
		print("Apple Music Not Responding")
	else:
		if result.stdout:
			items = result.stdout.strip().split("|||")
			return {"title": items[0],
        			"artist": items[1],
        			"album": items[2],
        			"year": int(items[3]),
        			"genre": items[4],
        			"duration": int(items[5].split(",")[0])}
	
	return None


def check_listen(song):
    """
    Checks if song matches last entry in listen table.
    """
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    cursor.execute("""
        SELECT title, artist
        FROM listen
        ORDER BY rowid DESC
        LIMIT 1
    """)
    last = cursor.fetchall()
    connection.close()
    
    if last == []:
        return False
    elif last[0][0] == song["title"] and last[0][1] == song["artist"]:
        return True
    return False


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

#!/usr/bin/python3
import subprocess
import sqlite3
from gestion import initialize_history, delete_history, check_listen, log_listen


def main():
    song = get_listen()
    if song is not None:
        initialize_history()
        if not check_listen(song):
        	log_listen(song["title"], song["artist"], song["album"], song["year"], song["genre"], song["duration"])

        #print(f"Title: {song["title"]}",
              #f"Artist: {song["artist"]}",
              #f"Album: {song["album"]}",
              #f"Year: {song["year"]}",
              #f"Genre: {song["genre"]}",
              #f"Duration: {song["duration"]}", sep="\n")


def get_listen():
	applescript = """
	tell application "Music"
		if player state is playing then
			set trackName to get name of current track
			set artistName to get artist of current track
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


if __name__ == "__main__":
    main()

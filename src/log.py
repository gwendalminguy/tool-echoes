#!/usr/bin/python3
"""
Script to log an entry in the history database.
"""
import os
from management import initialize_history, delete_history, get_listen, check_listen, log_listen


def main():
    base = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(base, "..", "data", "exports")
    os.makedirs(path, exist_ok=True)

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


if __name__ == "__main__":
    main()

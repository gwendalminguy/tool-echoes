#!/usr/bin/python3
from gestion import initialize_history, delete_history, get_listen, check_listen, log_listen


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


if __name__ == "__main__":
    main()

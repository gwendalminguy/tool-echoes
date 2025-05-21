#!/usr/bin/python3
import sqlite3
from gestion import initialize_history, delete_history, log_listen
from analyze import top_titles, top_artists, top_genres, total_unique_titles, total_unique_artists, total_unique_genres


def main():
	initialize_history()

	print("--------------------------------------------------------------------------------------")
	titles = top_titles()
	print("--------------------------------------------------------------------------------------")
	artists = top_artists()
	print("--------------------------------------------------------------------------------------")
	genres = top_genres()
	print("--------------------------------------------------------------------------------------")

	title_count = total_unique_titles()
	artist_count = total_unique_artists()
	genre_count = total_unique_genres()
	print(f"{title_count} titles from {artist_count} artists of {genre_count} genres", end="\n\n")


if __name__ == "__main__":
    main()

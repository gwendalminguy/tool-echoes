# Echoes

Echoes is a simple tool logging a history of music listened locally, and generating nicely designed statistics about artists, songs and genres for each year.

## 📋 Description

Echoes logs an entry in a history database for every song listened locally through a player. When launched, the `statistics.py` script exports statistics for the current year, including a top five of titles, a top five of artists, a top five of genres, and total count of titles, artists, genres and duration. Those statistics, saved in json format in the `archives/` directory, are then used for visualization.

## 📂 Project Structure

The project contains several files and directories, which are the following:

| Files | Description |
| :---- | :---------- |
| [`analyze.py`](https://github.com/gwendalminguy/tool-echoes/blob/main/analyze.py) | The module containing functions to extract statistics from the history database. |
| [`gestion.py`](https://github.com/gwendalminguy/tool-echoes/blob/main/gestion.py) | The module containing functions to manage the history database. |
| [`index.html`](https://github.com/gwendalminguy/tool-echoes/blob/main/index.html) | The HTML document to visualize statistics. |
| [`log.py`](https://github.com/gwendalminguy/tool-echoes/blob/main/log.py) | The python file containing the script to log an entry in the history database. |
| [`statistics.py`](https://github.com/gwendalminguy/tool-echoes/blob/main/statistics.py) | The python file containing the script to generate statistics from the history database. |
| [`style.css`](https://github.com/gwendalminguy/tool-echoes/blob/main/style.css) | The CSS document defining the style. |

## ⚙️ Installation

In order to install Echoes, the three steps of this guide must be followed:

**1. Cloning the repository**

To use Echoes, this repository must be cloned locally, using the following command:

```
$ git clone https://github.com/gwendalminguy/tool-echoes.git
```

**2. Setting an automation**

To let Echoes log an entry for each song listened in the history database, an automation must be set. This can be achieved by using the `Crontab` utility (pre-installed on macOS), that can be used to execute of a script on a regular schedule.

```
$ crontab -e
```

This will invoke a text editor, in which the following line must be written:

```
* * * * * <path/to/python3> <path/to/tool-echoes/log.py>
```

The paths must be changed to match the locations...

## 🖥️ Usage

The statistics can be updated using the following command:

```
$ ./statistics.py -y <year>
```

This will export the statistics for the chosen year (or for the current year if not specified) as a json file in the `archives/`directory, and print those statistics to the terminal.

### Limitations:

At this time, Echoes is restricted to some limitations, which are the following:

- only OS supported is macOS
- only player supported is Apple Music
- repeated listens of the same song in a row only counted once

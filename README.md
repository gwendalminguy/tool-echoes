# Echoes

Echoes is a simple tool logging a history of music listened locally, and generating nicely designed statistics about artists, songs and genres for each year with a dashboard visualization.

## 📋 Description

Echoes logs an entry in a history database for every song listened locally through a player. Statistics are regularly exported for the current year, including a top five of titles, artists and genres, among others. Those statistics are saved in JSON format in the `data/exports/` directory (automatically created if not existing), are then used to generate a nice dashboard visualization. The aim of this project is to have the opportunity to get statistics about some listening activity from local files using a player, without a streaming service.

### Statistics:

Available statistics saved in the JSON file for each year include the following:

- Top 25 Titles
- Top 25 Artists
- Top 25 Genres
- Top 25 Albums
- Total Unique Titles Count
- Total Unique Artists Count
- Total Unique Genres Count
- Total Unique Albums Count
- Average Daily Count & Duration
- Average Monthly Count & Duration
- Total Count & Duration
- Monthly Top Artist
- Monthly Total Count & Duration
- Daily Top Artist
- Daily Total Count & Duration

## 📂 Project Structure

The project contains several files and directories, which are the following:

| Files | Description |
| :---- | :---------- |
| `data/history.db` | The history database file. |
| `data/exports/index.json` | The JSON files listing available years. |
| `data/exports/<year>.json` | The JSON files containing statistics for each year. |
| [`src/analyze.py`](https://github.com/gwendalminguy/tool-echoes/blob/main/src/analyze.py) | The module containing functions to create statistics from the history database. |
| [`src/extract.py`](https://github.com/gwendalminguy/tool-echoes/blob/main/src/extract.py) | The python file containing the script to extract statistics. |
| [`src/log.py`](https://github.com/gwendalminguy/tool-echoes/blob/main/src/log.py) | The python file containing the script to log an entry in the history database. |
| [`src/management.py`](https://github.com/gwendalminguy/tool-echoes/blob/main/src/management.py) | The module containing functions to manage the history database. |
| [`src/serialization.py`](https://github.com/gwendalminguy/tool-echoes/blob/main/src/serialization.py) | The module containing functions to serialize statistics in JSON format. |
| [`web/`](https://github.com/gwendalminguy/tool-echoes/blob/main/web/) | The React dashboard application for statistics visualization. |
| [`install.sh`](https://github.com/gwendalminguy/tool-echoes/blob/main/install.sh) | The bash script setting automations to log entries and export statistics. |

## ⚙️ Installation

In order to install Echoes, the two steps of this guide must be followed:

**1. Cloning the repository**

To use Echoes, this repository must be cloned locally, using the following command:

```
$ git clone https://github.com/gwendalminguy/tool-echoes.git
```

**2. Setting the configuration**

To let Echoes log an entry for each song listened in the history database, and export the statistics, two automations must be set, along with some configuration details. This can be achieved by launching the `install.sh` bash script, and must be done at the root of the Echoes directory, using these commands:

```
$ cd tool-echoes/
$ chmod u+x install.sh
$ ./install.sh
```

This will allow the execution on a regular schedule of `log.py` and `extract.py` scripts, and install dependencies. The statistics for the current year will regularly be exported as a JSON file in the `data/exports/` directory. The user might be prompted by the system to authorize the automations, to allow scripts execution.

<details>
	<summary><b>Manual Installation Procedure</b></summary>
<br>

If desired, this installation can also be achieved manually, using the `Crontab` utility (pre-installed on macOS), as follows:

```
$ crontab -e
```

This will invoke a text editor, in which the following lines must be written (paths must be changed to match the locations of python3, of `src/log.py` and of `src/extract.py` files):

```
* * * * * <path/to/python3> <path/to/tool-echoes/src/log.py>
0 */6 * * * <path/to/python3> <path/to/tool-echoes/src/extract.py>
```

One other command needs to be run, in order to let Echoes work. It will create the `data/exports/` directory:

```
$ mkdir -p data/exports
```
</details>

## 🖥️ Usage

In order to visualize the statistics, the following commands must be executed at the root of the Echoes directory:

```
$ cd web/
$ npm run dev
```

The following URL should then be copied into any web browser:

```
http://localhost:5173/
```

This will open the default web browser and display a dashboard with several statistics for the current year. Navigation to the previous/next year or card is possible using the arrow buttons at the top, in the navigation bar. Once done, the server needs to be shut down using Ctrl+C.

<details>
	<summary><b>Manual Statistics Update</b></summary>
<br>

Although the statistics are updated automatically every four hours, it be achieved manually using the following command:

```
$ ./src/extract.py [-y <year>]
```

### Year:

If desired, the script can be launched to extract statistics for any previous year (as long as the history database contains matching entries). The desired year can then be chosen by calling it as a command-line argument with **-y** or **--year**, followed by the year itself.
</details>

## 🚫 Limitations

At this time, Echoes is restricted to some limitations:

- only OS supported is macOS
- only player supported is Apple Music
- installation script must be launched outside of any container
- automations seem to be removed after an OS update
- songs that are less than one minute long might not be logged in the history

# Echoes

Echoes is a simple tool logging a history of music listened locally, and generating nicely designed statistics about artists, songs and genres for each year.

## 📋 Description

Echoes logs an entry in a history database for every song listened locally through a player. When launched, the `statistics.py` script exports statistics for the current year, including a top five of titles, a top five of artists, a top five of genres, and total count of titles, artists, genres and duration. Those statistics, saved in json format in the `data/exports/` directory (automatically created if not existing), are then used to generate a nice visualization.

## 📂 Project Structure

The project contains several files and directories, which are the following:

| Files | Description |
| :---- | :---------- |
| `data/history.db` | The SQLITE history database. |
| `data/exports/*.json` | The JSON files containing statistics for each year. |
| [`src/analyze.py`](https://github.com/gwendalminguy/tool-echoes/blob/main/src/analyze.py) | The module containing functions to extract statistics from the history database. |
| [`src/gestion.py`](https://github.com/gwendalminguy/tool-echoes/blob/main/src/gestion.py) | The module containing functions to manage the history database. |
| [`src/log.py`](https://github.com/gwendalminguy/tool-echoes/blob/main/src/log.py) | The python file containing the script to log an entry in the history database. |
| [`src/statistics.py`](https://github.com/gwendalminguy/tool-echoes/blob/main/src/statistics.py) | The python file containing the script to generate statistics from the history database. |
| [`web/index.html`](https://github.com/gwendalminguy/tool-echoes/blob/main/web/index.html) | The HTML document to visualize statistics. |
| [`web/script.js`](https://github.com/gwendalminguy/tool-echoes/blob/main/web/script.js) | The javascript file... |
| [`web/style.css`](https://github.com/gwendalminguy/tool-echoes/blob/main/web/style.css) | The CSS document defining the style. |
| [`automation.sh`](https://github.com/gwendalminguy/tool-echoes/blob/main/automation.sh) | The bash script setting an automation to run `log.py` on a regular schedule. |

## ⚙️ Installation

In order to install Echoes, the two steps of this guide must be followed:

**1. Cloning the repository**

To use Echoes, this repository must be cloned locally, using the following command:

```
$ git clone https://github.com/gwendalminguy/tool-echoes.git
```

**2. Setting an automation**

To let Echoes log an entry for each song listened in the history database, an automation must be set. This can be achieved by launching the `automation.sh` bash script, and must be done at the root of the Echoes directory, using these commands:

```
$ chmod u+x automation.sh
$ ./automation.sh
```

This will allow the execution on a regular schedule of the `log.py` script. The user might be prompted by the system to authorize the automation, to allow it to execute the script. If desired, this can also be achieved manually, using the `Crontab` utility (pre-installed on macOS), as follows:

```
$ crontab -e
```

This will invoke a text editor, in which the following line must be written (both paths must be changed to match the locations of python3 and the `log.py` file from the cloned directory):

```
* * * * * <path/to/python3> <path/to/tool-echoes/src/log.py>
```

## 🖥️ Usage

The statistics can be updated using the following command:

```
$ ./src/statistics.py [-y <year>]
```

This will export the statistics for the current year as a json file in the `data/exports/`directory, and print those statistics to the terminal. The `index.html` file can then be opened in any web browser to view the statistics.

### Year:

If desired, the script can be launched to export statistics for any previous year (as long as the history database contains matching entries). The desired year can then be chosen by calling it as a command-line argument with **-y** or **--year**, followed by the year itself.

### Limitations:

At this time, Echoes is restricted to some limitations, which are the following:

- only OS supported is macOS
- only player supported is Apple Music

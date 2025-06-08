# Echoes

Echoes is a simple tool logging a history of music listened locally, and generating nicely designed statistics about artists, songs and genres for each year.

## 📋 Description

Echoes logs an entry in a history database for every song listened locally through a player. Statistics are regularly exported for the current year, including a top five of titles, a top five of artists, a top five of genres, and the total count of different titles, artists, and genres. Those statistics are saved in JSON format in the `data/exports/` directory (automatically created if not existing), are then used to generate a nice visualization. The aim of this project is to have the opportunity to get statistics about some listening activity from local files using a player, without a streaming service.

## 📂 Project Structure

The project contains several files and directories, which are the following:

| Files | Description |
| :---- | :---------- |
| `data/history.db` | The history database file. |
| `data/exports/*.json` | The JSON files containing statistics for each year. |
| [`src/analyze.py`](https://github.com/gwendalminguy/tool-echoes/blob/main/src/analyze.py) | The module containing functions to extract statistics from the history database. |
| [`src/management.py`](https://github.com/gwendalminguy/tool-echoes/blob/main/src/management.py) | The module containing functions to manage the history database. |
| [`src/serialization.py`](https://github.com/gwendalminguy/tool-echoes/blob/main/src/serialization.py) | The module containing functions to serialize statistics in JSON format. |
| [`src/extract.py`](https://github.com/gwendalminguy/tool-echoes/blob/main/src/extract.py) | The python file containing the script to extract statistics. |
| [`src/log.py`](https://github.com/gwendalminguy/tool-echoes/blob/main/src/log.py) | The python file containing the script to log an entry in the history database. |
| [`web/index.html`](https://github.com/gwendalminguy/tool-echoes/blob/main/web/index.html) | The HTML file defining the structure of the statistics visualization. |
| [`web/script.js`](https://github.com/gwendalminguy/tool-echoes/blob/main/web/script.js) | The JavaScript file defining the behaviour of the statistics visualization. |
| [`web/style.css`](https://github.com/gwendalminguy/tool-echoes/blob/main/web/style.css) | The CSS file defining the style of the statistics visualization. |
| [`install.sh`](https://github.com/gwendalminguy/tool-echoes/blob/main/install.sh) | The bash script setting automations to log entries and export statistics. |
| [`run.sh`](https://github.com/gwendalminguy/tool-echoes/blob/main/run.sh) | The bash script to visualize statistics. |

## ⚙️ Installation

In order to install Echoes, the two steps of this guide must be followed:

**1. Cloning the repository**

To use Echoes, this repository must be cloned locally, using the following command:

```
$ git clone https://github.com/gwendalminguy/tool-echoes.git
```

**2. Setting an automation**

To let Echoes log an entry for each song listened in the history database, and export the statistics, an automation must be set. This can be achieved by launching the `install.sh` bash script, and must be done at the root of the Echoes directory, using these commands:

```
$ cd tool-echoes/
$ chmod u+x install.sh
$ ./install.sh
```

This will allow the execution on a regular schedule of `log.py` and `extract.py` scripts. The statistics for the current year will regularly be exported as a JSON file in the `data/exports/`directory. The user might be prompted by the system to authorize the automations, to allow scripts execution.

<details>
	<summary><b>Manual Setting Procedure</b></summary>
<br>
If desired, this can also be achieved manually, using the `Crontab` utility (pre-installed on macOS), as follows:

```
$ crontab -e
```

This will invoke a text editor, in which the following lines must be written (paths must be changed to match the locations of python3, of `src/log.py` and of `src/extract.py` files):

```
* * * * * <path/to/python3> <path/to/tool-echoes/src/log.py>
* * * * 0 <path/to/python3> <path/to/tool-echoes/src/extract.py>
```
</details>

## 🖥️ Usage

<details>
	<summary><b>Manual Statistics Update</b></summary>
<br>
Although the statistics are updated automatically every hour, this can be achieved manually using the following command:

```
$ ./src/extract.py [-y <year>]
```

### Year:

If desired, the script can be launched to extract statistics for any previous year (as long as the history database contains matching entries). The desired year can then be chosen by calling it as a command-line argument with **-y** or **--year**, followed by the year itself.
</details>

In order to view the statistics, the `run.sh` bash script can be launched:

```
$ ./run.sh
```

<details>
	<summary><b>Manual Running Procedure</b></summary>
<br>
If desired, this can also be achieved manually, using the following command at the root of the Echoes directory:

```
$ python3 -m http.server --directory web
```

The following URL can then be copied into any web browser:

```
http://localhost:8000/
```
</details>

## 🚫 Limitations

At this time, Echoes is restricted to some limitations, which are the following:

- only OS supported is macOS
- only player supported is Apple Music
- automation must be set outside of any container
- automation seem to be removed after an OS update
- songs that are less than one minute long might not be logged in the history

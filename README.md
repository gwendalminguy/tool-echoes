# Echoes

Echoes is a simple tool logging a history of music listened locally, and generating nicely designed statistics about artists, songs and genres for each year.

## 📋 Description

...

## 📂 Project Structure

The project contains several files and directories, which are the following:


| Files | Description |
| :---- | :---------- |
| [`analyze.py`](https://github.com/gwendalminguy/tool-echoes/blob/main/analyze.py) | The module containing functions to extract statistics from the history database. |
| [`gestion.py`](https://github.com/gwendalminguy/tool-echoes/blob/main/gestion.py) | The module containing functions to manage the history database. |
| [`log.py`](https://github.com/gwendalminguy/tool-echoes/blob/main/log.py) | The python file containing the script to log an entry in the history database. |
| [`statistics.py`](https://github.com/gwendalminguy/tool-echoes/blob/main/statistics.py) | The python file containing the script to generate statistics from the history database. |

## ⚙️ Installation

In order to install Echoes, the three steps of this guide must be followed:

**1. Cloning the repository**

To use Echoes, this repository must be cloned locally, using the following command:

```
$ git clone https://github.com/gwendalminguy/tool-echoes.git
```

**2. Setting an automation**

To let Echoes log a history of each song listened, an automation must be set. This can be achieved by using `Crontab`, a utility that can be used to execute of a script on a regular schedule.

```
$ crontab -e
```

This will invoke a text editor, in which the following line must be ...

```
* * * * * <path/to/python> <path/to/tool-echoes/log.py>
```

...

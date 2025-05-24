#!/bin/bash
current=$(pwd)
python=$(which python3)
(crontab -l ; echo "* * * * * $python $current/log.py") | crontab -

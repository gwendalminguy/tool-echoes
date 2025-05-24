#!/bin/bash

# automation.sh - adds an automatic execution of the log.py script

current=$(realpath .src/log.py)
python=$(which python3)
(crontab -l ; echo "* * * * * $python $current") | crontab -

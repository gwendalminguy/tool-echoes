#!/bin/bash
mkdir -p data/exports
current=$(realpath ./src/log.py)
python=$(which python3)
(crontab -l 2>/dev/null ; echo "* * * * * $python $current") | crontab -

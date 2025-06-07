#!/bin/bash
mkdir -p data/exports
log=$(realpath ./src/log.py)
extract=$(realpath ./src/extract.py)
python=$(which python3)
(crontab -l 2>/dev/null; \
echo "* * * * * $python $log"; \
echo "* * * * 0 $python $extract") | crontab -

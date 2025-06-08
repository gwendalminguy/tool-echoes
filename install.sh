#!/bin/bash
mkdir -p data/exports
ln -s ../data/exports web/exports
LOG=$(realpath ./src/log.py)
EXTRACT=$(realpath ./src/extract.py)
PYTHON=$(which python3)
(crontab -l 2>/dev/null; \
echo "* * * * * $PYTHON $LOG"; \
echo "* * * * 0 $PYTHON $EXTRACT") | crontab -

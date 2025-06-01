#!/bin/bash
mkdir -p data/exports
log=$(realpath ./src/log.py)
statistics=$(realpath ./src/statistics.py)
python=$(which python3)
(crontab -l 2>/dev/null; \
echo "* * * * * $python $log"; \
echo "* * * * 0 $python $statistics") | crontab -

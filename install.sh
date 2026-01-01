#!/bin/bash

set -e

# Checking Requirements (npm - python3)
if ! command -v npm >/dev/null 2>&1; then
  echo "🔴 Failure: npm required but not found."
  exit 1
fi

if ! command -v python3 >/dev/null 2>&1; then
  echo "🔴 Failure: python3 required but not found."
  exit 1
fi

# Setting Paths
ROOT_DIRECTORY="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WEB_DIRECTORY="$ROOT_DIRECTORY/web"
LOG=$(realpath "$ROOT_DIRECTORY/src/log.py")
EXTRACT=$(realpath "$ROOT_DIRECTORY/src/extract.py")
PYTHON=$(which python3)

mkdir -p "$ROOT_DIRECTORY/data/exports"
chmod u+x "$ROOT_DIRECTORY/run.sh"

# Installing Frontend Dependencies
echo "🟡 Installing dependencies..."
(
  cd "$WEB_DIRECTORY"
  npm install
)

# Setting Cron Automations
echo "🟡 Setting automations..."
(crontab -l 2>/dev/null; \
echo "* * * * * $PYTHON $LOG"; \
echo "0 */6 * * * $PYTHON $EXTRACT") | crontab -

echo "🟢 Success: installation complete."

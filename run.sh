#!/bin/bash

# Setting Paths
ROOT_DIRECTORY="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WEB_DIRECTORY="$ROOT_DIRECTORY/web"

# Starting Server
echo "🟡 Starting server..."
(
  cd "$WEB_DIRECTORY"
  npm run dev
)

# Opening Navigator
/bin/sh -ec 'open http://localhost:5173'

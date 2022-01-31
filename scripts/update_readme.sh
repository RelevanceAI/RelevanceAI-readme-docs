#!/usr/bin/env bash

set -a
set -euo pipefail

DEBUG_MODE=${1:-false}

if [ "$DEBUG_MODE" = true ]; then
  set -x
fi

LUE=`tput bold && tput setaf 4`
CYAN=`tput bold && tput setaf 6`
blue=`tput setaf 4`
NC=`tput sgr0`

function BLUE(){
	echo -e "\n${BLUE}${1}${NC}"
}
function CYAN(){
	echo -e "\n${CYAN}${1}${NC}"
}
function blue(){
	echo -e "\n${blue}${1}${NC}"
}

README_VERSION=$(cat __version__)

CYAN "=== Updating asset links to v$README_VERSION ==="
python scripts/update_asset_links.py

CYAN "=== Rebuilding Readme versions ==="
python scripts/build_docs.py

CYAN "=== Syncing ReadMe version v$README_VERSION ==="
./scripts/sync_readme_docs.sh $DEBUG_MODE $README_VERSION

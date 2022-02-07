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

ROOT_PATH=${2:-$PWD}
PIP_PACKAGE_NAME=${3:-"RelevanceAI"}
README_VERSION=${4:-$(cat __version__)}


CYAN "=== Updating asset links to v$README_VERSION ==="

if $DEBUG_MODE; then
	python scripts/update_docs_version.py -d -p $PWD -pn $PIP_PACKAGE_NAME -v $README_VERSION
else
	python scripts/update_docs_version.py -p $PWD -pn $PIP_PACKAGE_NAME -v $README_VERSION
fi

CYAN "=== Rebuilding Readme docs ==="
if $DEBUG_MODE; then
	python scripts/build_docs.py  -d -p $PWD -pn $PIP_PACKAGE_NAME -v $README_VERSION
else
	python scripts/build_docs.py  -p $PWD -pn $PIP_PACKAGE_NAME -v $README_VERSION
fi

CYAN "=== Syncing ReadMe version v$README_VERSION ==="
./scripts/sync_readme_docs.sh $DEBUG_MODE $README_VERSION

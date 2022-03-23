#!/usr/bin/env bash

set -a
set -euo pipefail

DEBUG_MODE=${1:-false}

if [ "$DEBUG_MODE" = true ]; then
  set -x
fi


RED=; GREEN=; YELLOW=; BLUE=; BOLD=; RESET=;
case ${TERM} in '') ;;  *)
	BLUE=`tput bold && tput setaf 4`
	CYAN=`tput bold && tput setaf 6`
	blue=`tput setaf 4`
	NC=`tput sgr0`
esac

function BLUE(){
	echo -e "\n${BLUE}${1}${NC}"
}
function CYAN(){
	echo -e "\n${CYAN}${1}${NC}"
}
function blue(){
	echo -e "\n${blue}${1}${NC}"
}

DOCS_PATH=${2:-"$PWD/docs/"}
PIP_PACKAGE_NAME=${3:-"RelevanceAI"}

GIT_BRANCH_NAME=$(git rev-parse --abbrev-ref HEAD)
VERSION_FILE=$(cat __version__)

if [[ $GIT_BRANCH_NAME == "main" ]]; then
	GIT_BRANCH_NAME="v$VERSION_FILE"
	GIT_BRANCH_NAME_VERSION=$VERSION_FILE
	echo 'Branch ver is main'
else
	GIT_BRANCH_NAME_VERSION=$(echo $GIT_BRANCH_NAME | sed 's/[^0-9.]//g')
	echo $GIT_BRANCH_NAME_VERSION > __version__
fi

README_VERSION=${4:-$GIT_BRANCH_NAME_VERSION}

CYAN "=== Updating asset links to $GIT_BRANCH_NAME ==="

if $DEBUG_MODE; then
	python scripts/update_asset_ref.py -p $PWD -pn $PIP_PACKAGE_NAME -v $GIT_BRANCH_NAME
else
	python scripts/update_asset_ref.py -p $PWD -pn $PIP_PACKAGE_NAME -v $GIT_BRANCH_NAME
fi

CYAN "=== Updating semver ref to $README_VERSION ==="

if $DEBUG_MODE; then
	python scripts/update_semver_ref.py  -p $PWD -pn $PIP_PACKAGE_NAME -v $GIT_BRANCH_NAME_VERSION
else
	python scripts/update_semver_ref.py -p $PWD -pn $PIP_PACKAGE_NAME -v $GIT_BRANCH_NAME_VERSION
fi

CYAN "=== Rebuilding Readme docs $GIT_BRANCH_NAME ==="
if $DEBUG_MODE; then
	python scripts/build_docs.py  -d -p $PWD -pn $PIP_PACKAGE_NAME -v $GIT_BRANCH_NAME
else
	python scripts/build_docs.py  -p $PWD -pn $PIP_PACKAGE_NAME -v $GIT_BRANCH_NAME
fi

CYAN "=== Syncing ReadMe version $GIT_BRANCH_NAME ==="
./scripts/sync_readme.sh $DEBUG_MODE $DOCS_PATH $GIT_BRANCH_NAME

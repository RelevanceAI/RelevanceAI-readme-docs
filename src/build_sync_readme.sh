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

GIT_BRANCH_NAME=$(git rev-parse --abbrev-ref HEAD | sed -e 's/heads\///g')
echo $GIT_BRANCH_NAME
VERSION_FILE=$(cat __version__)

if [[ $GIT_BRANCH_NAME == "main" ]]; then
	GIT_BRANCH_NAME="v$VERSION_FILE"
	GIT_BRANCH_NAME_VERSION=$VERSION_FILE
	echo 'Branch ver is main'
else
	GIT_BRANCH_NAME_VERSION=$(echo $GIT_BRANCH_NAME | sed -e 's/v\///g' )
	echo $GIT_BRANCH_NAME_VERSION
	echo $GIT_BRANCH_NAME_VERSION > __version__
fi


README_VERSION=${4:-$GIT_BRANCH_NAME_VERSION}

CYAN "=== Updating asset links to $GIT_BRANCH_NAME ==="

if $DEBUG_MODE; then
	echo $GIT_BRANCH_NAME
	python src/rdme_sync/build/update_asset_ref.py -d -p $PWD -pn $PIP_PACKAGE_NAME -v $GIT_BRANCH_NAME
else
	python src/rdme_sync/build/update_asset_ref.py -p $PWD -pn $PIP_PACKAGE_NAME -v $GIT_BRANCH_NAME
fi

CYAN "=== Updating semver ref to $README_VERSION ==="

if $DEBUG_MODE; then
	python src/rdme_sync/build/update_semver_ref.py -d -p $PWD -pn $PIP_PACKAGE_NAME -v $GIT_BRANCH_NAME_VERSION
else
	python src/rdme_sync/build/update_semver_ref.py -p $PWD -pn $PIP_PACKAGE_NAME -v $GIT_BRANCH_NAME_VERSION
fi


CYAN "=== Converting notebooks to Markdown $GIT_BRANCH_NAME ==="
### Converts *ipynb  to *.md not in _notebooks
if $DEBUG_MODE; then
	python src/rdme_sync/readme/nbconvert_rdmd.py -d -f "block" -p $PWD -v $GIT_BRANCH_NAME_VERSION
else
	python src/rdme_sync/readme/nbconvert_rdmd.py -f "block" -p $PWD -v $GIT_BRANCH_NAME_VERSION
fi

# CYAN "=== Updating config $GIT_BRANCH_NAME with new files ==="
# ### Updates ReadMe with new files in docs
# if $DEBUG_MODE; then
# 	python src/rdme_sync/config/sync.py --method "update" -d -p $PWD -v $GIT_BRANCH_NAME
# else
# 	python src/rdme_sync/config/sync.py --method "update"  -p $PWD -v $GIT_BRANCH_NAME
# fi


CYAN "=== Rebuilding Readme docs $GIT_BRANCH_NAME ==="
### Builds all code snippets all Markdown files from docs to docs_template as well *ipynb in _notebooks
###
if $DEBUG_MODE; then
	python src/rdme_sync/build/build_docs.py -d -c -p $PWD -pn $PIP_PACKAGE_NAME -v $GIT_BRANCH_NAME
else
	python src/rdme_sync/build/build_docs.py -c -p $PWD -pn $PIP_PACKAGE_NAME -v $GIT_BRANCH_NAME
fi



CYAN "=== Syncing ReadMe version $GIT_BRANCH_NAME ==="
./src/sync_readme.sh $DEBUG_MODE $DOCS_PATH $GIT_BRANCH_NAME

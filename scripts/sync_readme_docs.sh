#!/usr/bin/env bash

set -a
set -euo pipefail

DEBUG_MODE=${1:-false}

if [ "$DEBUG_MODE" = true ]; then
  set -x
fi



###############################################################################
# Functions to get env vars
###############################################################################

check_readme_api_key_set(){
    if [[ -z "${RELEVANCEAI_README_API_KEY+x}" ]]; then
        echo "RELEVANCEAI_README_API_KEY is not set. Please export as ENV VAR"
        echo "export RELEVANCEAI_README_API_KEY='xxx'"
        false
    else
        true
    fi
}

get_latest_readme_version() {
    npx rdme versions --key $RELEVANCEAI_README_API_KEY --raw | jq -r 'sort_by(.createdAt)[-1].version'
}

###############################################################################
# Setting env vars
###############################################################################
check_readme_api_key_set

PIP_PACKAGE_NAME="RelevanceAI"
PACKAGE_JSON_URL="https://pypi.org/pypi/$PIP_PACKAGE_NAME/json"
RELEVANCEAI_SDK_VERSIONS=$(curl -L -s "$PACKAGE_JSON_URL" | jq  -r '.releases | keys | .[]' | sort -V)
LATEST_RELEVANCEAI_SDK_VERSION=$(curl -L -s "$PACKAGE_JSON_URL" | jq  -r '.releases | keys | .[]' | sort -V | tail -n1)
LATEST_README_VERSION=$(get_latest_readme_version)

DOCS_PATH=${2:-"$PWD/docs/"}
GIT_BRANCH_NAME=$(git rev-parse --abbrev-ref HEAD)
README_VERSION_NAME=${3:-${GIT_BRANCH_NAME}}
README_VERSION=$(echo $README_VERSION_NAME | sed 's/[^0-9.]//g')
RELEVANCEAI_SDK_VERSION=${README_VERSION}

echo "README_VERSION_NAME: $README_VERSION_NAME"
echo "README_VERSION: v$README_VERSION"
echo "RELEVANCEAI_SDK_VERSION: $RELEVANCEAI_SDK_VERSION"

if check_readme_api_key_set; then
    README_VERSIONS=$(npx rdme versions --key $RELEVANCEAI_README_API_KEY --raw | jq -r '.[] | .version')
fi


###############################################################################
# Create a new readme version if not exists
###############################################################################

README_VERSION_NAME_STRIPPED=$(echo $README_VERSION_NAME | sed 's/[v]//g')   ## stripping 'v' from version string

check_sdk_version_exists(){
    if [[ $RELEVANCEAI_SDK_VERSIONS =~ $RELEVANCEAI_SDK_VERSION ]]; then
        true
    else
        false
    fi
}


check_readme_version_exists(){
    if [[ $README_VERSIONS =~ $README_VERSION_NAME_STRIPPED ]]; then
        true
    else
        false
    fi
}

if ! check_sdk_version_exists; then
    echo "SDK version $RELEVANCEAI_SDK_VERSION does not exist. Please check the version number"
    exit 1
fi

if ! check_readme_version_exists; then
    npx rdme versions:create  --version=$README_VERSION_NAME_STRIPPED --key=$RELEVANCEAI_README_API_KEY --fork=$LATEST_README_VERSION --main=False --beta=True --isPublic=True
else
    echo "ReadMe version $README_VERSION_NAME already exists"
fi


###############################################################################
# Sync documentation
###############################################################################

echo "Syncing $DOCS_PATH to ReadMe version $README_VERSION_NAME"
npx rdme docs $DOCS_PATH --version=$README_VERSION_NAME_STRIPPED  --key $RELEVANCEAI_README_API_KEY


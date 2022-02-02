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
    check_readme_api_key_set
    npx rdme versions --key $RELEVANCEAI_README_API_KEY --raw | jq -r 'sort_by(.createdAt)[-1].version'
}


###############################################################################
# Setting env vars 
###############################################################################

PIP_PACKAGE_NAME="RelevanceAI"
PACKAGE_JSON_URL="https://pypi.org/pypi/$PIP_PACKAGE_NAME/json"  
RELEVANCEAI_SDK_VERSIONS=$(curl -L -s "$PACKAGE_JSON_URL" | jq  -r '.releases | keys | .[]' | sort -V)             
LATEST_RELEVANCEAI_SDK_VERSION=$(curl -L -s "$PACKAGE_JSON_URL" | jq  -r '.releases | keys | .[]' | sort -V | tail -n1)
LATEST_README_VERSION=$(get_latest_readme_version)

README_VERSION=${2:-${LATEST_README_VERSION}}
README_VERSION=$(echo $README_VERSION | sed 's/[^0-9.]//g')     ## stripping 'v' from version string

RELEVANCEAI_SDK_VERSION=${README_VERSION}

echo $README_VERSION

if check_readme_api_key_set; then
    README_VERSIONS=$(npx rdme versions --key $RELEVANCEAI_README_API_KEY --raw | jq -r '.[] | .version')
fi


###############################################################################
# Create a new readme version if not exists
###############################################################################

check_sdk_version_in_readme(){
    if [[ $README_VERSIONS =~ $RELEVANCEAI_SDK_VERSION ]]; then
        true
    else
        false
    fi
}

if ! check_sdk_version_in_readme; then
    npx rdme versions:create  --version=$README_VERSION --key=$RELEVANCEAI_README_API_KEY --fork=$LATEST_README_VERSION --main=False --beta=True --isPublic=True 
else
    echo "ReadMe version $README_VERSION already exists"
fi


###############################################################################
# Sync documentation
###############################################################################

echo "Syncing ReadMe version $README_VERSION"
npx rdme docs ./docs/ --version=$README_VERSION  --key $RELEVANCEAI_README_API_KEY
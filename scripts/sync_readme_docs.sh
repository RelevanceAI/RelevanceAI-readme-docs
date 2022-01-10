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


pip install --upgrade pip
pip --version
RELEVANCEAI_SDK_VERSION=$(pip --use-deprecated=legacy-resolver install RelevanceAI== | grep -oP '\(\K[^\)]+')
LATEST_README_VERSION=$(get_latest_readme_version)
echo $RELEVANCEAI_SDK_VERSION
echo $LATEST_README_VERSION

if check_readme_api_key_set; then
    README_VERSIONS=$(npx rdme versions --key $RELEVANCEAI_README_API_KEY --raw | jq -r '.[] | .version')
fi

###############################################################################
# Create a new readme version if not exists
###############################################################################


check_sdk_version_in_readme(){
    if [[ $README_VERSIONS =~ $RELEVANCEAI_SDK_VERSION ]]; then
        echo "RelevanceAI SDK version $RELEVANCEAI_SDK_VERSION is in README_VERSIONS"
        true
    else
        echo "RelevanceAI SDK version $RELEVANCEAI_SDK_VERSION is not in README_VERSIONS"
        false
    fi
}

if ! check_sdk_version_in_readme; then
    npx rdme versions:create  --version=$RELEVANCEAI_SDK_VERSION --key=$RELEVANCEAI_README_API_KEY --fork=$LATEST_README_VERSION --main=False --beta=True --isPublic=True 
else
    echo "RelevanceAI SDK version $RELEVANCEAI_SDK_VERSION already exists in ReadMe"
fi


###############################################################################
# Sync documentation
###############################################################################

npx rdme docs ./RelevanceAI-ReadMe-docs/ --version=$RELEVANCEAI_SDK_VERSION  --key $RELEVANCEAI_README_API_KEY
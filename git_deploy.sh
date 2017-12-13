#!/bin/bash
# A simple script to be called from a remote machine to deploy from GIT (i.e. Travis)

DEPLOY_PATH=${1}
DEPLOY_REPO=https://github.com/${2}.git
DEPLOY_COMMIT=${3}

# Check if deploy folder exists and create if necessary
if [ ! -d "${DEPLOY_PATH}" ]; then
    mkdir "${DEPLOY_PATH}"
fi

# Check if the git repo exists and clone or fetch
cd "${DEPLOY_PATH}";
if [ ! -d .git ]; then
    git clone ${DEPLOY_REPO} ${DEPLOY_PATH}
else
    git fetch --all
fi

# Checkout the branch
git checkout --force "${DEPLOY_COMMIT}"

#!/bin/bash

echo "Deploying to Webfaction"

if [ ${1} = "staging" ];
then
    echo "Deploying to staging server"
    DEPLOY_PATH=$DEPLOY_PATH_STAGING
else
    echo "Deploying to production server"
fi

export SSHPASS=$DEPLOY_PASS
sshpass -e ssh -o stricthostkeychecking=no ${DEPLOY_USER}@${DEPLOY_HOST} bash "${DEPLOY_HOME}/git_deploy.sh" "${DEPLOY_PATH}" ${DEPLOY_REPO} ${TRAVIS_COMMIT}
sshpass -e ssh -o stricthostkeychecking=no $DEPLOY_USER@$DEPLOY_HOST bash "${DEPLOY_PATH}/deploy.sh" $1

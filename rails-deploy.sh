#!/bin/bash

APP_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
WEBAPP_DIR="$(dirname "$APP_DIR")"

export PATH=$WEBAPP_DIR/bin:$PATH
export GEM_HOME=$WEBAPP_DIR/gems
export RUBYLIB=$WEBAPP_DIR/lib

cd $APP_DIR
bundle install
rake db:migrate

cd $WEBAPP_DIR
# Checks if this is the first run
if [ -d "hello_world" ]; then
    rm -rf "hello_world"
    sed -i 's/hello_world/app/g' nginx/conf/nginx.conf
fi

restart

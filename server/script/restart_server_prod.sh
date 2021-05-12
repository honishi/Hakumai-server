#!/usr/bin/env sh

basedir=$(cd $(dirname $0);pwd)

cd ${basedir}

./stop_server_prod.sh
sleep 3
./start_server_prod.sh
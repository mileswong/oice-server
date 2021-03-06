#!/usr/bin/env bash

PWD=`pwd`
WD=`cd $(dirname "$0") && pwd -P`

cd "${WD}"

docker build -t modmod-example -f Dockerfile .
docker build -t modmod-socket socket.io

cd "${PWD}"

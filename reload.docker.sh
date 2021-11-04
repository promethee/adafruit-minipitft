#!/bin/sh
./build.docker.sh
docker rm $(basename "$PWD") -f
./run.docker.sh
docker logs $(basename "$PWD")

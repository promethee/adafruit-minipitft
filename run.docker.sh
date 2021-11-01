#!/bin/sh
docker run -d --privileged --device /dev/i2c-1:/dev/i2c-1 --name minipitft promethee/adafruit-minipitft:latest

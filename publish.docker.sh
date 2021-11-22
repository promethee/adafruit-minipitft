#!/bin/sh
NAME=n$(md5sum Dockerfile | cut -c-4)
echo "using building context:" $NAME
docker buildx create --use --name $NAME
docker buildx build --push --platform linux/arm/v6,linux/arm/v7 --tag $USER/$(basename "$PWD"):latest .
docker buildx rm $NAME

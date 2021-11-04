#!/bin/sh
docker build -t $USER/$(basename "$PWD"):latest .

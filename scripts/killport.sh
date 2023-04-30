#!/bin/sh

if [ $# -eq 0 ]; then
    echo >&2 "No arguments provided"
    exit 1
fi

port=$1

kill $(lsof -t -i:${port})

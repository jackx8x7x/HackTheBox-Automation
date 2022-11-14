#!/bin/bash

NAME=htb-trick-auto

if ! docker images | grep -q $NAME
then
  docker build --tag=$NAME .
fi

if [ $# -eq 1 ]
then
  IP=$1
  docker run -it --rm --name $NAME $NAME $IP
else
  docker run -it --rm --name $NAME $NAME -h
fi

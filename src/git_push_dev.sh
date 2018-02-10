#!/usr/local/bin/bash

if [ "$1" == "" ]; then
	echo "usage: command message"
	exit
fi

MESSAGE=$1

git add -A
git commit -a -m $MESSAGE
git push

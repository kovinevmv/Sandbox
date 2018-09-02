#!/bin/bash
for (( i=0; ; i++ ));
do
	head -c 100000 /dev/urandom | tr -dc a-z > log.txt
	grep -aq "$1" ./log.txt
	if [[ $? == 0 ]]
	then
		echo "Found $1"
		exit 1
	else
		echo "Attempt [$i]: \"$1\" not found. Random text size: 100000"
	fi
done

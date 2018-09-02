#!/bin/bash

function traverse() 
{
for file in "$1"/*
do
    if [ ! -d "${file}" ] ; 
	then
		if [[ "$file" =~ ".jpg" || "$file" =~ ".JPG" ]]; 
		then
			echo  "Found jpg ---> ${file}"
			jpegoptim --max 60 "${file}"
		else
			echo "Another type  ---> ${file}"
		fi
		
    else
        traverse "${file}"
    fi
done
}

function main() 
{
    traverse "$1"
}

main "$1"

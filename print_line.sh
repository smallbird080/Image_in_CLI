#!/bin/bash

if [ "$#" -ne 3 ]; then
    echo "Usage: $0 <file> <character> <width>"
    exit 1
fi

file=$1
char=$2
width=$3
count=0

while IFS= read -r line; do
    IFS=',' read -r r g b <<< "$line"
    printf "\033[38;2;%d;%d;%dm%s" "$r" "$g" "$b" "$char"
    count=$((count + 1))
    if [ "$count" -eq "$width" ]; then
        printf "\n"
        count=0
    fi
done < "$file"

# Reset color
printf "\033[0m\n"
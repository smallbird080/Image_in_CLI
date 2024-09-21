#!/bin/bash

file="output/output.txt"
width=$1
count=0

while IFS= read -r line; do
    IFS='_' read -r r g b char<<< "$line"
    printf "\033[38;2;%d;%d;%dm%s" "$r" "$g" "$b" "$char"
    count=$((count + 1))
    if [ "$count" -eq "$width" ]; then
        printf "\n"
        count=0
    fi
done < "$file"

printf "\033[0m\n"
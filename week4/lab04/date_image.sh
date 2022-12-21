#!/bin/dash

ls -l file

time=$(ls -l file | cur -d ' ' -f6,7,8)
convert -gravity south -pointsize 36 -draw "text 0,10 '$time'" "$1" "$1"
display $1
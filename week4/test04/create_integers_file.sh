#! /bin/dash

start=$1
end=$2
while test "$start" -le "$end"
do
    echo "$start" >> "$3"  #append the number
    start=$((start + 1 ))
done
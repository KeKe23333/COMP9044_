#!/bin/dash

for file in "$@"

do
    names=$(grep '^#include "[^"]*"' < $file | sed "s/#include \"//g; s/\"//g")
    # echo $names
    for name in $names
    do
        if ! test -e "$name"
        then 
            echo "${name} include into ${file} does not exist"
        fi
    done

done
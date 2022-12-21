#!/bin/dash

dict1=$1
dict2=$2

test -e tmp/tmp$$ && rm tmp/tmp$$
touch tmp/tmp$$

#same name,

for file in $dict1/*
do
    test "$file" = "$dict1/*" && exit 1
    name=$(echo $file | sed "s_dict/__")
    # s/regex/expression/
    if test -e "$dict2/$file"
    then
        diff=`diff "$file" "$dict2/$file"`

        if test $? -eq 0
        then
            echo "$name" 
        fi    
    fi
done

sort < /tmp/tmp$$

#!/bin/bash

small=""
mid=""
large=""

for file in *
do
    size=$(wc -l <$file)
    if test $size -lt 10
    then
        small+="$file "    
    elif [ $size -ge 10 -a $size -lt 100 ]
    then
        mid+="$file "
    elif test $size -ge 100
    then
        large+="$file "
    fi
    
done

echo "Small files: $small"
echo "Medium-sized files: $mid"
echo "Large files: $large"


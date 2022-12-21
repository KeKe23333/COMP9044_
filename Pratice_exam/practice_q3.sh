#! /bin/dash

for file in *
do
    if [ -d $file ]
    then
        [ `ls -1 "$file" | wc -l ` -ge 2 ] && echo "$file"
    fi
done

#!/bin/dash
if test $# -ne 1
then 
    exit 1
fi

num=0
name.".$1.$num"
while test -e $name
do 
    num=$((num+1))
    name".$1.$num"
done

cp $1 $name



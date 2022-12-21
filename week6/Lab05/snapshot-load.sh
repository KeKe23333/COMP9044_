#!/bin/dash

i=0
dict=".snapshot.$i"

while test -e $dict
do
    i=$((i+1))
    dict=".snapshot.$i"
done
mkdir $dict $$ echo "Creating snapshot $i"


for file in *
do
    if test $file !="^\..*" && test $file != 'snapshot-save.sh' && test $file != 'snapshot-load.sh'
    then
        cp $file "$dic/"
    fi

done
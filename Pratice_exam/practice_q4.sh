#! /bin/dash

a1="$1"
a2="$2"
start=`echo "$a1" | sed -E 's/[a-z]//g'`
end=`echo "$a2" | sed -E 's/[a-z]//g'`

i=$start
while [ $i -le $end ]
do
    echo "$a1" | sed -E "s/[0-9]+/${i}/g"
    i=$((i+1))
done

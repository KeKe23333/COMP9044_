#!/bin/dash

for i in *.jpg
do 
	name=$(echo "$i" | cut -d"." -f1)
	
	if test -e "$name".png
	then	
		echo "${name}.png already exists " && exit 1
	fi

	convert "$name".jpg "$name".png 2> /dev/null  && rm "$name".jpg

done

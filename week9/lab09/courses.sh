#!/bin/dash

courses=$(curl --location --silent http://www.timetable.unsw.edu.au/2022/$1KENS.html)

echo $courses | sed 's/<td class="data">/\n/g' | grep -E "<a href=\"$1" | sed '1d; n; d' | sed "s/<a href=\"//g;s/.html\">/ /g;s/<\/td>//g" | sed "s/<\/a>//g" | sort | uniq
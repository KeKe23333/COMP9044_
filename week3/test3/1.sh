#!/bin/dash


#Q1
cut -d'|' -f2,3 | sort | uniq | cut -d'|' -f2 | cut -d',' -f2 | cut -d' ' -f2 | sed 's/ //'g | sort 

#Q2
grep "COMP2041\|COMP9044" | cut -d '|' -f3 | cut -d',' -f2 |cut -d' ' -f2 |  sort | uniq -c | sort | tail -n1 | sed 's/.*[0-9] //g'

#Q3
cut -d'|' -f2 | sort | uniq -c | grep '2 [0-9]' | sed 's/.*[0-9] //g'

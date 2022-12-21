#!/bin/bash

if test $# -ne 2
then 
    echo "Usage: scraping_courses.sh <year> <course-prefix>" && exit 1
elif ! [[ $1 =~ ^(2019|2020|2021|2022)$ ]]
then 
    echo "scraping_courses.sh: argument 1 must be an integer between 2019 and 2022" $$ exit 1
fi
u="https://www.handbook.unsw.edu.au/api/content/render/false/query/+unsw_psubject.implementationYear:$1%20+unsw_psubject.studyLevel:undergraduate%20+unsw_psubject.educationalArea:$2*%20+unsw_psubject.active:1%20+unsw_psubject.studyLevelValue:ugrd%20+deleted:false%20+working:true%20+live:true/orderby/unsw_psubject.code%20asc/limit/10000/offset/0"
p="https://www.handbook.unsw.edu.au/api/content/render/false/query/+unsw_psubject.implementationYear:$1%20+unsw_psubject.studyLevel:postgraduate%20+unsw_psubject.educationalArea:$2*%20+unsw_psubject.active:1%20+unsw_psubject.studyLevelValue:pgrd%20+deleted:false%20+working:true%20+live:true/orderby/unsw_psubject.code%20asc/limit/10000/offset/0"

wget -q -O- "$u" | 2041 jq ".contentlets[] | {code: .code, title: .title}" | tr -d "{|}" | sed 's/ "code": "//g;s/ "title": "//g' | sed "/^$/d" | sed 's/"//g' | 's/"$/@/g' | sed 's/",/ /g'| tr -d '\n' | tr '@' '\n'

wget -q -O- "$u" "$q" | 2041 jq ".contentlets[] | {code: .code, title: .title}" | tr -d "{|}" | sed 's/ "code": "//g;s/ "title": "//g' | sed "/^$/d" | sed 's/",//g' | tr '"' '\n'> temp.txt
wget -q -O- "$u" "$q" | 2041 jq ".contentlets[] | {code: .code, title: .title}" | tr -d "{|}" | sed 's/ "code": "//g;s/ "title": "//g' | sed "/^$/d" | sed 's/"$/@/g' | sed 's/",/ /g' | tr '@' '\n'> temp.txt


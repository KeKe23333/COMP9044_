#! /bin/dash

for file in *.htm
do
    name=$(echo $file | cut -d'.' -f1)
    if test -e ${name}.html
    then
        echo "${name}.html exists" && exit 1 
    fi
    mv "$file" "${name}".html # rename a file, apeend new file and delete orignal one 

done
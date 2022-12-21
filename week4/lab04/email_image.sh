#!/bin/dash
if test $# -eq 0
then 
    echo "Please enter a image" && exit 1

fi

for image in  "$@" 
do
    # gm display "$image"
    read -p "Address to e-mail this image to?" email
    if [ -z $email ]
    then 
        echo "No email sent" && exit 1

    fi
    echo $email
    read -p "Message to accompany image?" string
    name=$(echo "$image" | cut -d"." -f1)
    echo '$string' | mutt -s '${name}!' -e 'set copy=no' -a $image -- "$email" && echo "$image sent to $email"
    
done
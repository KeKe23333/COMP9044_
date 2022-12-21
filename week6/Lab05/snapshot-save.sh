#!/bin/dash
sh snapshot-save.sh

repo=".snapshot.$1"
echo "Restoring snapshot $1"


for i in $repo/*
do
    cp -f $i ./ || exit 1
done
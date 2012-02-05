#!/bin/bash
MAX=26

# grab hw number
num=`echo "$@" | sed "s/[0-9]/X/g"`
hw=`echo "$@" | sed "s/^[^1-9]*\([1-9][0-9]*\).*$/\1/"`

# reject a missing number
if [ -z "$hw" ] || [ "$num" = "$hw" ]; then
    echo "Error: missing homework number"
    echo "example: ./turnin.sh hw01"
    exit 1
fi

# reject numbers that are out of the range
if [ $hw -gt $MAX ] || [ $hw -lt 1 ]; then
    echo "Homework number should be between 1 and $MAX"
    exit 1
fi

hw=hw`printf "%02d" $hw`

if [ "$hw" != "$1" ]; then
    echo "Assuming you meant $hw"
fi

git add .
git commit -m "$hw done"
git tag --force $hw
git push
git push --tags

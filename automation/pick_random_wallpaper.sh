#!/bin/bash
# assuming that there are no subfolders inside destination folder
arr=(`echo ~/Pictures/Walls/*`)

#echo ${arr[*]}

val=`ls ~/Pictures/Walls/* | wc -l`

n=`eval echo ${val}`

#echo "no of files are $n"

n=`shuf -i 1-$n -n 1`

#echo "random number chosen is $n"

#echo "chosen random file is : ${arr[$n]}"

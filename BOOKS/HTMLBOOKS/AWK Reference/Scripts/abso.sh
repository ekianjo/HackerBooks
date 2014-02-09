#!/bin/sh
# usage:
#    abso filename [filename ...]
# output - a list of files with the full pathname
# list each file with the full pathname
# plus
# delete /tmp_mnt
# change $HOME to ~
cwd=`pwd`
for i in $* 
do 
	test -f $i && echo $cwd/$i;
done | sed "
s,/tmp_mnt,,
"


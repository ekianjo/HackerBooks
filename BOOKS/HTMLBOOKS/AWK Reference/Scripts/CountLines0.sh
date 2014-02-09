#!/bin/sh
filename=/tmp/$0.$$
cat "$@" | wc -l >$filename
echo  `cat $filename` lines were found
/bin/rm $filename


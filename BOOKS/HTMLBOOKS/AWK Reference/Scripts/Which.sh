#!/bin/sh
# A simple version of which that prints all 
# locations that contain the command
file=${1:-"Wrong number of arguments - usage: 'which command'"}
paths=`echo $PATH | sed '
s/^:/.:/g
s/:$/:./g
s/::/:.:/g
s/:/ /g
'`
for dir in $paths
do
    [ -x $dir/$file ] && echo $dir/$file
done


#!/bin/sh
arg1="a.out"
arg2=`pwd`
arg3=$HOME
if [ $# -gt 3 ]
then
	echo too many arguments
	exit 1
fi

if [ $# -eq 0 ]
then
	echo must specify at least one argument
	exit 1
fi
[ $# -ge 1 ] && arg1=$1 # do this if 1, 2 or 3 arguments
[ $# -ge 2 ] && arg2=$2 # do this if 2 or 3 arguments
[ $# -ge 3 ] && arg3=$3 # do this if 3 arguments

mv $arg2/$arg1 $arg3

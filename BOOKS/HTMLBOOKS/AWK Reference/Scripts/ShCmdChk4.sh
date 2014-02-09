#!/bin/sh

usage() {
	echo `basename $0`: ERROR: $* 1>&2
	echo usage: `basename $0` 'filename [fromdir] [todir]' 1>&2
	exit 1
}
arg1="a.out"
arg2=`pwd`
arg3=$HOME

case $# in
	0) usage "must provide at least one argument";;
	1) arg1=$1;;
	2) arg1=$1;arg2=$2;;
	3) arg1=$1;arg2=$2;arg3=$3;;
	*) usage "too many arguments";;

esac
mv $arg2/$arg1 $arg3

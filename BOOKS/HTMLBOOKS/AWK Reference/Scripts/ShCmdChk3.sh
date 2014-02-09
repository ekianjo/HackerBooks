#!/bin/sh

usage() {
	echo `basename $0`: ERROR: $* 1>&2
	echo usage: `basename $0` 'filename [fromdir] [todir]' 1>&2
	exit 1
}
arg1="a.out"
arg2=`pwd`
arg3=$HOME

[ $# -gt 3  -o $# -lt 1 ] && usage "Wrong number of arguments"

arg1=$1;shift
[ $# -gt 0 ] && { arg2=$1;shift;}
[ $# -gt 0 ] && { arg3=$1;shift;}

mv $arg2/$arg1 $arg3

#!/bin/sh

usage() {
	echo `basename $0`: ERROR: $* 1>&2
	echo usage: `basename $0` '[-a] [-b] [-c] [-o file] \
		[file ...]' 1>&2
	exit 1
}

a= b= c= o=

while :
do
    case "$1" in
	-a) a=1;;
	-b) b=1;;
	-c) c=1;;
	-o) shift; o="$1";;
	--) shift; break;;
	-*) usage "bad argument $1";;
	*) break;;
    esac
    shift
done
# rest of script...

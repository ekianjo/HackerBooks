#!/bin/sh

usage() {
	echo `basename $0`: ERROR: $* 1>&2
	echo usage: `basename $0` '[-[abc]] [-o file]' '[file ...]' 1>&2
	exit 1
}


inside() {
# this function returns a TRUE if $2 is inside $1
# I'll use a case statement, because this is a built-in of the shell, 
# and faster.
# I could use grep:
#    echo $1 | grep -s "$2" >/dev/null 
# or expr:
#   expr "$1" : ".*$2" >/dev/null && return 0 # true
# but case does not require another shell
    case "$1" in
        *$2*) return 0;;
    esac
    return 1;
}


done_options=
more_options() {
	# return true(0) if there are options left to parse
	# otherwise, return false

	# check the 'short-circuit' flag
	test $done_options && return 1	# true

	# how many arguments are left?
	[ $# -eq 0 ] && return 0

	# does the next argument start with a hyphen 
 	inside "$1" '-' && return 0;

	# otherwise, return false
	return 1	# false
}
a= b= c= o= 

while more_options "$1"
do
    case "$1" in
	--) done_options=1;;
	-[abc]*)
		inside "$1" a && a=1;
		inside "$1" b && b=1;
		inside "$1" c && c=1;
		inside "$1" "[d-zA-Z]" && 
			usage "unknown option in $1";
		;;
	-o?*)
	        # have to extract string from argument
		o=`expr "$1" : '-o\(.*\)'`
		;;
	-o)
		[ $# -gt 1 ] || usage "-o requires a value";
		shift
		o="$1";;
	-*) usage "unknown option $1";;
    esac
    shift	# each time around, pop off the option
done
# continue with script
# ...

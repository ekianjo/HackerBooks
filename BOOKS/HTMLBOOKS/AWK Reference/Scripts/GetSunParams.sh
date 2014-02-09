#!/bin/sh
# set path - just in case
PATH=/usr/5bin:/usr/bin:/bin:/usr/ucb;
export PATH

# GetSunParms - written by Bruce Barnett 

# NOTE - this does not work if the window is a cmdtool.
# the window must be a shelltool, so turn off scrolling

# only one argument allowed
case $# in
1)	;;
*)	echo 'Usage: GetSunParms [rc|wh|icon|pos|label|ilabel|page|scroll]';
	exit 1;;
esac
# hardwire these variables
E="\033"
N="\c"
# Because the searchpath has 5bin before bin
#   we get the system 5 echo 
ECHO="echo"

# turn off scrolling
$ECHO "${E}[>4l${N}" >/dev/tty


# and that argument must be one of these:
case $1 in
icon)	esc="${E}[11t${N}";;
pos)	esc="${E}[13t${N}";;
wh)	esc="${E}[14t${N}";;
rc)	esc="${E}[18t${N}";;
ilabel)	esc="${E}[20t${N}";;
label)	esc="${E}[21t${N}";;
page)	esc="${E}[>1;k${N}";;
scroll)	esc="${E}[>4;k${N}";;
*)	echo 'Unknown parameter';exit 1;;
esac

#turn off line mode and echo
stty raw -echo >/dev/tty

# send escape sequence to the SunView window
$ECHO $esc >/dev/tty

# use dd to get one line, then use tr to delete octal 33 (escape)
# and set $@ to be the results
set `dd </dev/tty count=1 2>/dev/null | tr -d '\033'`

# Put the terminal back the way it was
stty -raw echo >/dev/tty

# Now output just the numeric values
case $1 in 
\[1t)	echo Open;;
\[2t)	echo Closed;;
\[3*)	echo "$@" | sed 's/^\[3;\([0-9]*\);\([0-9]*\)t/\1 \2/';;
\[4*)	echo "$@" | sed 's/^\[4;\([0-9]*\);\([0-9]*\)t/\1 \2/';;
\[8*)	echo "$@" | sed 's/^\[8;\([0-9]*\);\([0-9]*\)t/\1 \2/';;
\]L*)	echo "$@" | sed 's/^\]L\(.*\).$/\1/';;
\]l*)	echo "$@" | sed 's/^\]l\(.*\).$/\1/';;
\[\>1*)	echo "$@" | sed 's/^\[>1//';;
\[\>2*)	echo "$@" | sed 's/^\[>2//';;
\[\>4*)	echo "$@" | sed 's/^\[>4//';;
\[\>8*)	echo "$@" | sed 's/^\[>8//';;
*)	echo "don't understand $@";;
esac


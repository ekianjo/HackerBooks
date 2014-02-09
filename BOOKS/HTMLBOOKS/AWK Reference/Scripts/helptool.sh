#!/bin/sh
#
# %W% %G%
# Bruce Barnett 1986-1993
#
# Usage: three cases
#
# 	helptool 2 exec
# 	helptool exec(2)
#	helptool exec
#
# In all cases, a new window is created if a manual page exists.
#


ONCE=""
SHOW="textedit -Wh 7" # Open WIndows
#WHATIS=Key
WHATIS="whatis"
#SHOW="xedit"	#X/11
#SHOW="TextEditor"	# A/UX


# set NAME to the name of the command without the section

case $# in 
	2) # must be like case 1
		ARG="$1 $2"
		ARGID="$2($1)"
		NAME="$2"
		;;
	1) # one argument - must be like case 3 above or case 2
	   # find out which one
		case "$1" in
		*\([0-9]*\)) # case 2
			# change "cmd(1)" to "1 cmd"
			NAME=`echo $1|sed 's/\([a-zA-Z0-9_]*\)([1-8][A-Z]*)/\1/'`
			ARG=`echo $1|sed 's/\([a-zA-Z0-9_]*\)(\([1-8]\)[A-Z]*)/\2 \1/'`
			ARGID=$1;
			;;
		[a-z09-9]*)  # case 3
			# fine the way it is, a simple command
			ARG=$1
			NAME=$1
			;;
		esac
		;;
	*) # error
		echo "need one argument"; exit 1
		;;
esac


# 
# move to the tmp directory so textedit will display
# the file without a directory name
cd /tmp

#echo formatting "$ARG"...
# format the manual page for dumb terminals
# if textedit can handle bold (typeover) then this can eventually change
# need an eval in case $ARG is 2 parameters
eval man "$ARG" |ul -tdumb >/tmp/man$$

#error check - how many lines were generated
count=`wc -l </tmp/man$$`

# if zero, then there was no entry

if [ $count -le 2 ] 
then
	echo man cannot find anything on $ARG;
	 exit 1;
fi

# find out what this document is called by using sed
# look for [a-z0-9A-Z][a-zA-Z0-9]*([1-8][A-Z]*)
# and keep it, discard everything else
name=`sed -n '/[a-zA-Z0-9_]([1-8][A-Z]*)/{
s/.*[^a-zA-Z0-9_]\([a-zA-Z0-9_][a-zA-Z0-9_]*([1-8][A-Z]*)\).*/\1/
p
q
}' </tmp/man$$| tr 'A-Z' 'a-z'`

#echo name is $name, count is $count

# Find the SEE ALSO values
# That is, look for the line after the SEE ALSO header and print it out
# but only if it matches the patterns we expect
seealso=`sed -n '/[ ]*SEE ALSO/{
n
/[a-zA-Z0-9][a-zA-Z0-9]*([1-8][A-Z]*)/p
q
}' </tmp/man$$ | head -1`

#echo seealso is $seealso

# find the whatis values

# if $name doesn't have a value, use $NAME
shortname=`echo ${name:-$NAME}|sed 's/(.*)//'`


# try to get the whatis line done to a single word
# convert 
# 	uid_allocd, gid_allocd(8C) - UID and GID allocator daemons
#
# into 
#	uid_allocd(8C)
#
# and
#	vi, view, vedit (1)	- visual display editor based on ex(1)
# into
#	vi(1)
#
# this is why the sed line below is so complicated 
# besides underscore characters, also deal with hyphens and spaces
# and deal with lines that are poorly formated
whatis=`$WHATIS $shortname|sed -e '
/([1-8][A-Z]*)/ {
 s/\([a-zA-Z0-9_-][a-zA-Z0-9_-]*\)[,a-zA-Z0-9 _-]*\(([1-8][A-Z]*)\).*/\1\2/p
}
/([1-8][A-Z]*)/ !d
'|sort|uniq`

#echo statis is $? ,  whatis is $whatis

	/bin/mv /tmp/man$$ /tmp/${name:-$NAME}
	if [ -n "$seealso" ] 
	then
		if [ -z "$ONCE" ] 
		then
			echo "SEE ALSO"
			ONCE="YES"
		fi
		echo  $seealso
	fi
	for x in $whatis
	do
		# convert to lower case for comparison
		y=`echo $x | tr '-A-Z' 'a-z'`
		if [ "$y" != "$name"  ] 
		then
			if [ -z "$ONCE" ] 
			then
				echo "SEE ALSO"
				ONCE="YES"
			fi
			echo $x
		fi
	done
#echo $SHOW  ${name:-$NAME}; /bin/rm -i ${name:-$NAME}  
($SHOW  ${name:-$NAME}; /bin/rm ${name:-$NAME}  )&

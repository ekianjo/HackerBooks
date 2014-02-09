#!/bin/sh
# Bruce Barnett 
# This script will change the specified resource
#
# Usage: Resource [-p] [resource[:] value]
# where RESOURCE  is set to VALUE
# if -p is given, change the value permanently.
# if -p is given, but no resource specified, save all
#

# specify default filename
XD="$HOME/.Xdefaults"

# Is there a -p?
if [ $# -gt 0 ] ; 
then
	case "$1" in
		-p) PERM=1;shift;;
	esac
fi

# must have 0 or 2 arguments now, else error

if [ $# -eq 1 -o $# -gt 2 ] ; then
	echo "Usage: `basename $0 ` [-p] [resource[:] value]"
	exit 1;
fi



if [ $# -eq 2 ] ; then

	# the colon is optional - this removes it
	RESOURCE=`echo $1 | tr -d :`
	VALUE=$2;
	# Make the change
# 	echo "echo $RESOURCE $VALUE | xrdb -merge"
	echo $RESOURCE: $VALUE | xrdb -merge
fi

# Is this a permanent change?
if [ $PERM ] ; then
#	echo "xrdb -edit $XD -backup .b"
	xrdb -edit $XD -backup .b

	# Note that the backup fill will be created even if
	# the value does not change.
	# therefore - compare the original backup file with the new file
	# if no difference, delete the backup file
	# else rename the backup file to .Xdefaults.old.1
	# and rename .Xdefaults.old.1 to .Xdefaults.old.2

	diff $XD $XD.b >/dev/null && {
		# if identical, delete .Xdefaults.b
		/bin/rm $XD.b
	}  || {
		# different files - keep 2 backups
		#  you can easily make it keep 3, 4 or 5 backups.
		# .Xdefaults.old.1 may not exist
		# if it does, then rename it
		[ -f $XD.old.1 ] && /bin/mv $XD.old.1 $XD.old.2
		/bin/mv $XD.b $XD.old.1
	}
fi

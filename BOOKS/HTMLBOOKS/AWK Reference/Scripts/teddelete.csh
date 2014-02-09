#!/bin/csh -f
# this is like the ted script, but it deletes the files afterwards
# for safety reasons, it only edits one file
# get size of file
# usage:
#      teddelete file
if ( -f $1 ) then
	set size = (`height_width.awk <$1`)
# too bad -width <columns> doesn't work
#	echo textedit -En $size[1] -width $size[2] $1 
	textedit -En $size[1] $1 
	echo "deleting file $1"
	/bin/rm $1
else
	echo file $1 not found
endif


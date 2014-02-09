#!/bin/sh

# grep4: prints out 4 lines around pattern
# if there is only one argument, exit

case $# in 
	1);;
	*) echo "Usage: $0 pattern";exit;;
esac;

sed -n '
'/$1/' !{
	# does not match - add this line to the hold space
	H
	# bring it back into the pattern space
	x
	# Two lines would look like .*\n.*
	# Three lines look like .*\n.*\n.*
	# Delete extra lines - keep two
	s/^.*\n\(.*\n.*\)$/\1/
	# now put the two lines (at most) into 
	# the hold buffer again
	x
}
'/$1/' {
	# matches - append the current line
	H
	# get the next line
	n
	# append that one also
	H
	# bring it back, but keep the current line in
	# the hold buffer. This is the line after the pattern,
	# and we want to place it in hold in case the next line
	# has the desired pattern
	x
	# print the 4 lines
	p
	# add the mark
	a\
---
}'

#!/bin/sh
# grep3 version b - another version using the hold commands
# if there is only one argument, exit

case $# in 
	1);;
	*) echo "Usage: $0 pattern";exit;;
esac;

# again - I hope the argument doesn't contain a /

# use sed -n to disable printing 

sed -n '
'/$1/' !{
	# put the non-matching line in the hold buffer
	h
}
'/$1/' {
	# found a line that matches
	# append it to the hold buffer
	H
	# the hold buffer contains 2 lines
	# get the next line
	n
	# and add it to the hold buffer
	H
	# now print it back to the pattern space
	x
	# and print it.
	p
	# add the three hyphens as a marker
	a\
---
}'

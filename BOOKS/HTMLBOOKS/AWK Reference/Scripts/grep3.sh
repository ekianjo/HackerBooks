#!/bin/sh
# grep3 - prints out three lines around pattern
# if there is only one argument, exit

case $# in 
	1);;
	*) echo "Usage: $0 pattern";exit;;
esac;
# I hope the argument doesn't contain a /
# if it does, sed will complain

# use sed -n to disable printing 
# unless we ask for it
sed -n '
'/$1/' !{
	#no match - put the current line in the hold buffer
	x
	# delete the old one, which is 
	# now in the pattern buffer
	d
}
'/$1/' {
	# a match - get last line
	x
	# print it
	p
	# get the original line back
	x
	# print it
	p
	# get the next line 
	n
	# print it
	p
	# now add three dashes as a marker
	a\
---
	# now put this line into the hold buffer
	x
}'

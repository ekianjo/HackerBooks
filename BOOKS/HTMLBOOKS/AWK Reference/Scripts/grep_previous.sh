#!/bin/sh 
# print previous entry
sed -n '
/^[ ^I]/!{
	# line does not start with a space or tab,
	# does it have the pattern we are interested in?
	'/$1/' {
		# yes it does. print three dashes
		i\
---
		# get hold buffer, save current line
		x
		# now print what was in the hold buffer
		p
		# get the original line back
		x
	}
	# store it in the hold buffer
	h
}
# what about lines that start
# with a space or tab?
/^[ ^I]/ {
	# append it to the hold buffer
	H
}'

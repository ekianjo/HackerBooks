#!/bin/sh
# This is a Bourne shell script that removes #-type comments
# between 'begin' and 'end' words.
sed -n '
	/begin/,/end/ {
	     s/#.*//
	     s/[ ^I]*$//
	     /^$/ d
	     p
	}
'


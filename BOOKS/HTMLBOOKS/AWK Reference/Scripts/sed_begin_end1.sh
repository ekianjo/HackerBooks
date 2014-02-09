#!/bin/sh
# This is a Bourne shell script that removes #-type comments
# between 'begin' and 'end' words.
sed -n '
	1,100 {
		/begin/,/end/ {
		     s/#.*//
		     s/[ ^I]*$//
		     /^$/ d
		     p
		}
	}
'


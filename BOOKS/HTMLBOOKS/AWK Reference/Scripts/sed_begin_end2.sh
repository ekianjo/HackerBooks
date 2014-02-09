#!/bin/sh
sed '
	/begin/,/end/ !{
	     s/#.*//
	     s/[ ^I]*$//
	     /^$/ d
	     p
	}
'


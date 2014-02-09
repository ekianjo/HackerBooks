#!/bin/sh
# format paragraphs - work around fmt limitation
# usage:
#	Fmt <input >output
#
# note - there are two things about this script that makes 
# it non-portable (i.e. won't run on many UNIX systems)
# 1) The \{...\} construct
# 2) the sed comments that start with a "#"
# Sun's sed supports this. Not all versions do.
# you may have to convert this into perl
#
# Now break the problem into steps
# 1) add a \n at the end, using ( cat -;echo "")
# 2) expand tabs into spaces, using expand
# 3) use sed to
#  3a) remove blank lines at the end of a line
#  3b) split ling lines into two lines
#
# 	use the string ".\{68,80\}" string to
#	 match 68-80 characters. 
#  3c) delete last line if it is empty
# 4) run it through fmt -c
# 5) unexpand spaces into tabs using unexpand
#
(cat - ; echo "" ) | expand | sed '
# remove extra spaces at the end of the line
s/ *$//
# now add a new line after 68-80 characters
s/\(.\{68,80\}\) \(.*\)/\1\
\2/
# now remove the last line if and only if it is blank
$ {
/^$/ d
}' | fmt -c | unexpand


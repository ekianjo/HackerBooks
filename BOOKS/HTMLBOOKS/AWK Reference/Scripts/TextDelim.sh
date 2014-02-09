#!/bin/sh
# This script changes the text delimiter chaacters
# It calls the Resource script described before
# the resource to be changes is text.delimiterChars
# The second argument is just a quoted string
# The \011 is the form the resource manager wants to see for the tab character
# Two warnings:
# if you ask the resource manager to output the current value
#	it doesn't quote the characters properly
#	Therefore you can't automatically save 
#	this property into the .Xdefaults file
# Problem two:
#	The order of spaces and \011 in the string is tricky
# for some reason, the order of the space, tab, or
# other character is important. If the first four
# characters are ' \011!@' it doesn't work.
# however, '! @\011' does.
# - Don't know why
#
# also notice how I added the single quote to the string
# remember - you can't use
#	'....\''
# to quote a single string in a single string
#
# I used the form
#    '........' concatenated with "'"
# which is the preferred form.
# the backquote doesn't backquote anything below
#
# after all that - I can throw these characters at you
# without you flinching		(too much :-)
#
Resource text.delimiterChars '! @\011#%$%^&*()_+-=[]{}|;:",<>?`~/\'"'"
# all those comments for one line of code!
# the rest of the script can be uncommented for debug purposes;

#echo delimiter is now:
#xrdb -query | grep delimiter >/dev/console


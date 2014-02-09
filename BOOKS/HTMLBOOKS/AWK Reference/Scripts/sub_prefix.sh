#!/bin/sh
# sub_prefix - subtract prefixes
# usage
#     sub_prefix < in > out
#
# search for lines that start with 
# anything except
#      a letter
#      a number
#      a space or tab
# which may be duplicated
# followed by 0 or 1 spaces
# the above is called the prefix
# followed by a word - Keep the word with every case
# some explanation of the sed script
# We use the \(...\) to "remember" parts of the pattern
# and use \1, \2 to "recall" the remembered pattern
# this is how we keep the first word, or look for
# duplicate patterns
#
# the pattern
#      [a-zA-Z0-9      ]
# matches upper/lower case letters, numbers space, tab
#
# the pattern
#      [^a-zA-Z0-9     ]
# matches everything EXCEPT upper/lower case letters, numbers space, tab
#
# portability warning:
# The comment lines within the sed command may have to be 
# removed for non-SunOS Systems
sed '
# this line is a sed comment
#
# remove leading spaces
s/^[   ]*//
# now deal with the prefixes, different cases
# case where prefix = non-alphanumeric
s/^[^a-zA-Z0-9         ]\([a-zA-Z0-9]\)/\1/
# prefix = non-alphanumeric followed by 0 or more spaces/tabs
s/^[^a-zA-Z0-9         ][      ]*\([a-zA-Z0-9]\)/\1/
# prefix = duplicate non-alphanumeric followed by 0 or more spaces/tabs
# note the use of \1 in the pattern to be matched
s/^\([^a-zA-Z0-9       ]\)\1[  ]*\([a-zA-Z0-9]\)/\2/
# prefix = triplicate non-alphanumeric followed by 0 or more spaces/tabs
s/^\([^a-zA-Z0-9       ]\)\1\1[        ]*\([a-zA-Z0-9]\)/\2/
# prefix = one or more right brackets followed by 0 or more spaces/tabs
s/^[]}>][]}>]*[        ]*//
'


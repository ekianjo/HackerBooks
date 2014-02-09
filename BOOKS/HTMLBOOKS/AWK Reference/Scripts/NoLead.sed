#!/bin/sed -f
# NoLead: a sed filter that removes leading spaces
# It also removes trailing whitespace.
# inside the [] are two characters: a space and a tab
s/^[ 	]*//
s/[ 	]*$//


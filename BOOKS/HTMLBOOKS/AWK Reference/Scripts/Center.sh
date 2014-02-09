#!/bin/sh
# Inspired from UNIX Power Tools
# Center - center text
# usage
#      Center [length] <in >out
# where [length] is the optional line length
# defaults to 80
#
LENGTH=${1-80}
# If first argument not specified, assume line length of 80
#
# first - remove excess spaces from end of lines
# I could also use the NoLead script.
# note that between the [ and ] are two characters
#   a space and a tab
sed '
s/[ 	]$//g
s/^[ 	]//g
' | awk  '
#  $0 is the input line
{
prefix = "";
for (i = 1;i<('$LENGTH' - length($0))/2;i++)
       prefix = prefix " ";
print prefix $0;
}'


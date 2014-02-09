#!/bin/sh
# convert2uc version b
# change the first hex number to upper case format
# uses sed once
# used as a filter
# convert2uc <in >out
sed '
{
# remember the line
h
#change the current line to upper case
y/abcdef/ABCDEF/
# add the old line back
G
# Keep the first word of the first line, 
# and second word of the second line
# with one humongous regular expression
s/^\([^ ]*\) .*\n[^ ]* \(.*\)/\1 \2/
}'

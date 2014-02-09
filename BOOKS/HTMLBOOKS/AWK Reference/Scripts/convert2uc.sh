#!/bin/sh
# change the first hex number to upper case format
# uses sed twice
# used as a filter
# convert2uc <in >out
sed '
s/ /\
/' | \
sed ' {
	y/abcdef/ABCDEF/
	N
	s/\n/ /
}'

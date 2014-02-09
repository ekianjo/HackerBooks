#!/bin/sh
sed '
s/ /\
/' | \
sed ' {
	y/abcdef/ABCDEF/
	N
	s/\n/ /
}'


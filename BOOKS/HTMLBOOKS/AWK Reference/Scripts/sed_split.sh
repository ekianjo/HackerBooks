#!/bin/sh
tr ' ' '\012' file| \
sed ' {
	y/abcdef/ABCDEF/
	N
	s/\n/ /
}'


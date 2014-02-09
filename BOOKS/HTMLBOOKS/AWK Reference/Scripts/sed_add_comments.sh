#!/bin/sh
sed '
/begin/ {
0i\
	This is a comment\
	It can cover several lines\
	It will work with any version of sed
}'

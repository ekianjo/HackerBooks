#!/bin/sh
# add_prefix
# usage
#     add_prefix [prefix] < in > out
#
# get the prefix
#
# I hope it isn't a funny character - like a space, or /
PRE=${1-">"}
sed 's/^/'"$PRE"'/'


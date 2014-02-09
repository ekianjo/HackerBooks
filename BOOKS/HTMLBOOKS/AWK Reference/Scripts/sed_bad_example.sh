#!/bin/sh
# this example is WRONG
sed -e '1 {
	d
	s/.*//
}'


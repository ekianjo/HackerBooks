#!/bin/sh
# watch out for a '/' in the parameter
# use alternate search delimiter
sed -e '\_#INCLUDE <'"$1"'>_{

	# read the file
	r '"$1"'

	# delete any characters in the pattern space
	# and read the next line in
	d
}'


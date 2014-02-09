#!/bin/sh
sed '
/ONE/ {
# append the next line
	N
# look for "ONE" followed by "TWO"
	/ONE.*TWO/ {
#	delete everything between
		s/ONE.*TWO/ONE TWO/
#	print
		P
#	then delete the first line
		D
	}
}' file


#!/bin/sh
# Spelling filter version 1
# we need two temporary files
FILE=/tmp/spell.$$
# the second file s the same as the first, 
# but has a "1" appended to the name
FILE1=${FILE}1
trap "/bin/rm $FILE $FILE1" 0 1 2 15
# send standard input to output
tee $FILE
# find misspelled words
spell $FILE >$FILE1
# and append them to the end of the selection
# use the shell && and || for if then else
# is the test condition ( non-zero file) true?
[ -s $FILE1 ] && {
	# then the size of the file is larger than zero
	echo "-----"
	cat $FILE1
	echo "----"
} || {
	# else
	echo "-----"
	echo " no misspelled words"
	echo "----"
}


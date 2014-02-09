#!/bin/sh
# Spelling filter version 2
# this one creates a new window
FILE=/tmp/spell.$$
FILE1=${FILE}1
# standard input is passed to the temporary file 
# and standard output
tee $FILE;
# now find the misspelled words
spell <$FILE >$FILE1
# display them in a new window
# that is tall and wide
(textedit -geometry 100x400-0-0 $FILE1;/bin/rm $FILE $FILE1) <&- >&- &


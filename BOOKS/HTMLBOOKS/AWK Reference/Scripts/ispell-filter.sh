#!/bin/sh
# ispell filter
# pick a name of a temporary file
FILE=/tmp/ispell.$$
# if the script ends, or is interrupted, 
#  delete the temporary file
trap "/bin/rm $FILE" 0 1 2 15
cat >$FILE
shelltool ispell -x $FILE 
cat <$FILE


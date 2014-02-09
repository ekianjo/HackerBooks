#!/bin/sh
# ispell filter
# Part 1- store the new file
FILE=/tmp/ispell
# if the script ends, or is interrupted, 
#  delete the temporary file
tee $FILE
shelltool ispell -x $FILE >&- &


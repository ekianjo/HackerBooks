#!/bin/sh
# this edits the temporary dynamic filter
# while allowing standard input and output to flow through
FILE=$HOME/bin/dynamic
# 'tee' sends stdin through to stdout, leaving the selection alone
#tee $FILE;
# 'cat' sends redirects stdin, so the selection is deleted
# the >> appends the selection to the current file, so it will work
# even if nothing is currently selected
cat >> $FILE;
# make it executable
chmod +x $FILE
# it is necessary to close standard output 
# use the Bourne shell  sequence ">&-"
# also fork a new process
textedit -geometry 500x100+0-0 $FILE >&- &


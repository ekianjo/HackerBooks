#!/bin/csh
tee /tmp/file | \
( grep MATCH /tmp/file >/dev/null && \
( echo BEFORE; cat - ) || ( cat - ; echo AFTER) )
/bin/rm /tmp/file

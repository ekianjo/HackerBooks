#!/bin/csh -f
# this could be one script instead of three if 
# we were using the Bourne Shell
# But the C shell isn't very good at piping
# commands inside of loops.
#
# Therefore we generate the pipe in one script, 
# and feed AWK in another script
GetPaths | analyze_paths.awk HOSTNAME=`hostname`


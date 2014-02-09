#!/bin/csh -f
# Script name: S
# written by Bruce Barnett 
# usage:
#	S [argument] [window arguments...]
# where the first argument is a filename, 
# and the rest are appended to the command
# pick default window parameters
set defaults = "-Wx medium"
# Assume no additional arguments for now
set w_args = ""

# any arguments?
if ( $#argv > 0  ) then
# yes - one found
# does the file ~/.S/$1 exist?
	if ( -f ~/.S/$1 ) then
# use egrep to remove comments from file		
# use egrep because it's faster than grep
		set w_args = `egrep -v '^#' ~/.S/$1`
# delete first argument, move 2nd to 1st, etc.
		shift
	else
# file doesn't exist
	endif
endif

# execute the shell
cmdtool $defaults $w_args $* &

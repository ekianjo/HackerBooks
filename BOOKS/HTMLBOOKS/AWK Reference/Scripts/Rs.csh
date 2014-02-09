#!/bin/csh -f
# remote shell script 
# Bruce Barnett 

# only one argument allowed
if ( $#argv != 1 ) then
	echo "Usage:	Rs <hostname>"
	exit 1
endif

# if you use emacs and the Meta key, you need the -8 option
set RLOGIN = "rlogin -8"

#define the window arguments, in case there aren't any
set w_args = ""

# look for the file ~/.Rs/hostname
# if there, then use the parameters when starting a new window

# ignore lines that start with a '#'
if ( -f ~/.Rs/$1 ) set w_args = `egrep -v '^#' ~/.Rs/$1`

#execute the shell, use eval because of variables and ''
eval cmdtool -label $1 -icon_label $1 $w_args $RLOGIN $* &


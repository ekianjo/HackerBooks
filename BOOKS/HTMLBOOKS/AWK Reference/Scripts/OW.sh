#!/bin/sh
# check DISPLAY first
# This will give an error if the variable is not set
x=${DISPLAY:?Variable_not_set} 
# now look for directory that contains the OW libraries
# maybe it's in /usr/openwin - the default
[ -d /usr/openwin/bin ] && {
#	/usr/openwin found
	OPENWINHOME=/usr/openwin;
} || {
#	else try /usr/local/openwin
	OPENWINHOME=/usr/local/openwin;
}
#
# if FONTPATH is not defined, use "/usr/lib/X11/font"
defaultfont=${FONTPATH:-/usr/lib/X11/font} 
# add $OPENWINHOME/lib/fonts to the path
FONTPATH=$OPENWINHOME/lib/fonts:$defaultfont
# help path should be set
HELPPATH=$OPENHOME/lib/help
# Add Open Windows dynamic libraries to path
LD_LIBRARY_PATH=$OPENWINHOME/lib:${LD_LIBRARY_PATH:-/usr/lib}
# add OW directories to searchpath
PATH=$OPENWINHOME/bin/xview:$OPENWINHOME/bin:$PATH
export OPENWINHOME FONTPATH HELPPATH 
export LD_LIBRARY_PATH DISPLAY PATH
exec $*


#!/bin/csh -f
setenv OPENWINHOME /usr/openwin
setenv MANPATH /usr/lang/man:/usr/share/man
setenv DISPLAY :0.0

if ( -f ~/.display ) then
	echo -n "Delete the display file? "
	/bin/rm -i ~/.display
endif
if ( ! -f ~/.display ) then
	echo `hostname`:0.0 >~/.display
endif
openwin 
echo -n "Delete the display file? "
/bin/rm -i ~/.display


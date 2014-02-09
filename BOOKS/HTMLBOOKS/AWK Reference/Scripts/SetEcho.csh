#!/bin/csh -f
# set the echo variables
# place this in your .cshrc or equivalent file.

if ( ! $?HOSTNAME ) then
	setenv  HOSTNAME `hostname`
endif

# have I executed this script before on this system?
if ( $?E ) then
	#echo "already set the echo variables">/dev/tty
else if ( -f ~/.echo.${HOSTNAME} ) then
	source ~/.echo.${HOSTNAME}
else if ( `echo -n |wc -l`  == 0 ) then
	#echo "built-in echo is bsd" >/dev/tty
	echo 'set ech = "echo -n"' >~/.echo.${HOSTNAME}
	echo "set E = `echo a | tr a '\033'`" >> ~/.echo.${HOSTNAME}
	echo "set B = `echo a | tr a '\007'`" >> ~/.echo.${HOSTNAME}
	echo 'set N = ""' >> ~/.echo.${HOSTNAME}
	source ~/.echo.${HOSTNAME}
else 
	#echo "built-in echo is sysV" >/dev/tty
	echo 'set ech = "echo"' >~/.echo.${HOSTNAME}
	echo 'set E = "\033"' >> ~/.echo.${HOSTNAME}
	echo 'set B = "\007"' >> ~/.echo.${HOSTNAME}
	echo 'set N = "\c"' >> ~/.echo.${HOSTNAME}
	source ~/.echo.${HOSTNAME}
endif	

#!/bin/csh -f
# look for processes, and open them using the shell alias
if ($#argv != 1 ) then
	echo 'usage: OpenProc1 <processname>'
	exit 1
endif

set arg = $argv[1]
set tty=`tty`

set ttys = (`ps -w | awk '/'$arg'/ {print $2}'|sort|uniq`)
if ( $#ttys > 0 ) then
	if ( -f ~/.echo.${HOSTNAME} ) then
		source ~/.echo.${HOSTNAME}	
		alias Open '$ech  "${E}[1t${N}"'
	endif
	foreach t ( $ttys)
		if ( $t != co  && ( $tty !~ /dev/tty${t} )) then
			echo "Open > /dev/tty${t}"
			Open >/dev/tty${t}
		endif
	end
endif


#!/bin/csh -f
# look for processes, and open them using the shell alias
if ($#argv != 3 ) then
	echo 'usage: MoveProc <processname> <x-pos> <x-pos>'
	exit 1
endif

set pat = $1
set x = $2
set y = $3
set ttys = (`ps -c | awk '$5 ~ /'$pat'/ {print $2}'`)
if ( $#ttys > 0 ) then
	if ( -f ~/.echo.${HOSTNAME} ) then
		source ~/.echo.${HOSTNAME}	
	else
		echo "cannot find ~/.echo.${HOSTNAME}
		exit
	endif

	foreach t ( $ttys)
		if ( $t != co ) then

 #			alias Move  '${ech}  "${E}[3;\!:1;\!:2t${N}"'
			${ech}  "${E}[3;${x};${y}t${N}" >/dev/tty${t}
		endif
	end
endif


#!/bin/csh -f
# Created by Bruce Barnett
# look for processes, and open them using the shell alias
# Need one argument
if ($#argv != 1 ) then
	echo 'usage: OpenProc <processname>'
	exit 1
endif
# The pattern we are looking for is called "pat"

set pat = $1

# "ps -c" generated the following output:
#         1440 p0 IW    0:00 csh
#
# If the fifth field (the process name) matches the pattern
# print out the second field ( the terminal)

# Turn off quoting around $pat by toggling
set ttys = (`ps -c | awk '$5 ~ /'$pat'/ {print $2}'`)

# may have zero or more matches

if ( $#ttys > 0 ) then
	# At least one match
	# read in the echo variables
	if ( -f ~/.echo.${HOSTNAME} ) then
		source ~/.echo.${HOSTNAME}	
		alias Open '$ech  "${E}[1t${N}"'
	else
		echo "cannot find ~/.echo.${HOSTNAME}"
		exit
	endif
	# now open each one in turn
	foreach t ( $ttys)
		# don't open the console
		if ( $t != co ) then
			Open >/dev/tty${t}
		endif
	end
endif

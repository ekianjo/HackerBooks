#!/bin/csh -f
# Routine to bounce a window around
# Bruce Barnett
if ( -f ~/.echo.${HOSTNAME} ) then
	source ~/.echo.${HOSTNAME}	
 	alias Move  '${ech}  "${E}[3;\!:1;\!:2t${N}"'
else
	echo "cannot find ~/.echo.${HOSTNAME}"
	exit
endif

# initialize the initial positions and offsets
@ x = 0
@ y = 0
@ xoff = 10
@ yoff = 10
set DELAY = "sleep 1"

# Position to origin
eval Move $x $y
$DELAY

while ( 1 )	# forever

# check x
	if ( $x > 800 ) then
		@ xoff = -10
	else if ( $x <= 0 ) then
		@ xoff = 10
	endif

# check y
	if ( $y > 800 ) then
		@ yoff = -10
	else if ( $y <= 0 ) then
		@ yoff = 10
	endif

# increment x and y
	@ x = $x + $xoff
	@ y = $y + $yoff

# positon to new location
	eval Move $x $y

	$DELAY	# and wait
end


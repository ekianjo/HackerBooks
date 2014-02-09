#!/bin/csh
set d = (`date`)
# like 
#  set d = ( Sun Feb 9 16:08:29 EST 1997 )
# therefore
# d[1] = day of week
set day2="[Mm]on"
switch ( $d[1] )
case "*Sun": 
	echo Sunday; breaksw
case $day2: 
	echo Monday;breaksw;
case Tue: 
	echo Tuesday;breaksw;
case Wed: 
	echo Wednesday;breaksw;
case Th?: 
	echo Thursday;breaksw;
case F*: 
	echo Friday;breaksw;
case [Ss]at: 
	echo Saturday;breaksw;
default:
	echo impossible condition
	exit 2
endsw


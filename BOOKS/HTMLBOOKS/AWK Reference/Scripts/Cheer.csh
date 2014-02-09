#!/bin/csh

foreach i ( 1 2 3 4 5 6 7 8 9 10 11 12 ) 

	# if 9, exit
	if ( $i == 9 ) break
	# if odd, then don't echo
	if ( $i % 2 == 1 ) continue
	# Even numbers only
	echo  $i
	sleep 1
end
echo 'Who do we appreciate?'
sleep 1; echo $USER
sleep 1; echo $USER
sleep 1; echo $USER
sleep 1; echo 'Yeah!!!!!!'

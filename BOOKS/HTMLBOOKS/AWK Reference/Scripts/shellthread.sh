#!/bin/bash


function doloop {

if [ "$done" -eq  1  ]
then
	if [ $thread1 -gt 0 ]
	then
		thread1=0
		echo relaunch thread1
		(sleep 40;echo thread1 done;kill -USR1 $$) & pid1=$!
		trap "done=1;thread1=1" USR1
		done=0
	fi
	if [ $thread2 -gt 0 ]
	then
		thread2=0
		echo relaunch thread2
		(sleep 60;echo thread2 done;kill -USR2 $$) & pid2=$!
		trap "done=1;thread2=1" USR2
		done=0
	fi
fi
echo sleep for 10
sleep 10
}
trap 'kill $pid1 $pid2' 0 1 15


MYPID=$$
done=0
thread1=0
thread2=0
thread3=0
thread4=0

trap "done=1;thread1=1;echo thread1 caught;trap '' USR1" USR1
(sleep 40;echo thread1 done;kill -USR1 $$) & pid1=$!
trap "done=1;thread2=1;echo thread1 caught;trap '' USR2" USR2
(sleep 60;echo thread2 done;kill -USR2 $$) & pid2=$!
	
while true
do
	doloop
done

echo exit the loop


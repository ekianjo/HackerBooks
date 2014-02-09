#!/bin/awk -f
# demonstrate use of exp(), log() and sqrt in AWK
# e.g. what is the difference between using logarithms and regular arithmetic
# note - exp and log are natural log functions - not base 10
#
BEGIN {
# what is the about of error that will be reported?
	ERROR=0.000000000001;
# loop a long while
	for (i=1;i<=2147483647;i++) {
# find log of i
		logi=log(i);
# what is square root of i? 
# divide the log by 2
		logsquareroot=logi/2;
# convert log of i back
		squareroot=exp(logsquareroot);
# find the difference between the logarithmic calculation
# and the built in calculation
		diff=sqrt(i)-squareroot;
# make difference positive 
		if (diff < 0) {
			diff*=-1;
		}
		if (diff > ERROR) {
			printf("%10d, squareroot: %16.8f, error: %16.14f\n", \
				i, squareroot, diff);
		}
	}
	exit;
}

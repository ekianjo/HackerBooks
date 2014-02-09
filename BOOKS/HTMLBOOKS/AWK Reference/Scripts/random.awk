#!/usr/bin/nawk -f
# old AWK doesn't have rand() and srand()
# only new AWK has them
# how random is the random function?
BEGIN {
#	srand();
	i=0;
	while (i++<1000000) {
		x=int(rand()*100 + 0.5);
		y[x]++;
	}
	for (i=0;i<=100;i++) {
		printf("%d\t%d\n",y[i],i);
	}
	exit;
}

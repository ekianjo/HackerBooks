#!/usr/bin/nawk -f
BEGIN {
# Assume we want 6 random numbers between 1 and 36
# We could get this information by reading standard input,
# but this example will use a fixed set of parameters.
#
# First, initialize the seed
    srand();
# How many numbers are needed?
    NUM=6;
# what is the minimum number
    MIN=1;
# and the maximum?
    MAX=36;
# How many numbers will we find? start with 0
    Number=0;
    while (Number < NUM) {
	r=int(((rand() *(1+MAX-MIN))+MIN));
# have I seen this number before?
	if (array[r] == 0) {
# no, I have not
	    Number++;
	    array[r]++;
	}
    }

# now output all numbers, in order
    for (i=MIN;i<=MAX;i++) {
# is it marked in the array?
	if (array[i]) {
# yes
	    printf("%d ",i);
	}
    }
    printf("\n");
    exit;
}

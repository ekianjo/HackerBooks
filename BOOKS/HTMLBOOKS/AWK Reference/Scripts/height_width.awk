#!/bin/awk -f
# this program reads standard input and 
# generates two numbers on standard output:
# the suggested width and height of a window
# It is used for shell applications that want to 
# open windows of the right size, and avoid opening them too big
# first - initialize
BEGIN {
    MINWIDTH=20;
    MAXWIDTH=100;
    MINHEIGHT=5;
    MAXHEIGHT=34;
    HEIGHT=MINHEIGHT;
    WIDTH=MINWIDTH;
}
# for each line
{
# NR = the number of records
    if ((NR > MINHEIGHT) && (NR <= MAXHEIGHT)) {
	HEIGHT=NR;
    }
# length is equal to the length of the line    
    if ((length > MINWIDTH) && (length <= MAXWIDTH)) {
	WIDTH=length;
    }
}
# at end
END {
# add a couple of spaces to the width and height
    if (WIDTH + 4 <= MAXWIDTH) {
	WIDTH+=4;
    }
    if (HEIGHT + 4 <= MAXHEIGHT) {
	HEIGHT+=4;
    }
    printf("%d %d\n",HEIGHT, WIDTH);
}


#!/bin/awk -f
# reports which file is being read
BEGIN {
	f="";
}
{	if (f != FILENAME) {
		print "reading", FILENAME;
		f=FILENAME;
	}
	print;
}

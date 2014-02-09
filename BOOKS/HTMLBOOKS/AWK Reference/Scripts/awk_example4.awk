#!/bin/awk -f
{
	if ( $0 ~ /:/ ) {
		FS=":";
	} else {
		FS=" ";
	}
	#print the third field, whatever format
	print $3
}

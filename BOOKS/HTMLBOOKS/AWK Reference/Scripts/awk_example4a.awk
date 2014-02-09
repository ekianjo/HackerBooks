#!/bin/awk -f
{
	if ( $0 ~ /:/ ) {
		FS=":";
		$0=$0
	} else {
		FS=" ";
		$0=$0
	}
	#print the third field, whatever format
	print $3
}

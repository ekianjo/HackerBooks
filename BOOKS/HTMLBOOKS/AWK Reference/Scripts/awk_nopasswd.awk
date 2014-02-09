#!/bin/awk -f
BEGIN {
	FS=":";
}
{
	if ( $2 == "" ) {
		print $1 ": no password!";
	}
}

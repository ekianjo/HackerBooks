#!/bin/awk -f
BEGIN {
	FS=":";
	OFS=":";
}
{
	$2="";
	print
}

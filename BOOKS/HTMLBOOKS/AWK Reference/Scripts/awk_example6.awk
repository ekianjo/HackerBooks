#!/bin/awk -f
BEGIN {
# change the record separator from newline to nothing	
	RS=""
# change the field separator from whitespace to newline
	FS="\n"
}
{
# print the second and third line of the file
	print $2, $3;
}

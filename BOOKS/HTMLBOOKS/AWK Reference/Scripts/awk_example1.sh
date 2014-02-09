#!/bin/sh
# Linux users have to change $8 to $9
awk '
BEGIN 	{ print "File\tOwner" } 
		{ print $8, "\t", $3}	
END   	{ print " - DONE -" } 
'

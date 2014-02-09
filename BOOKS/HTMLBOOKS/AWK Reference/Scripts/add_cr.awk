#!/bin/awk -f
# this filter adds a carriage return to all lines
# before the newline character
BEGIN {	
	ORS="\r\n"
}
{ print }

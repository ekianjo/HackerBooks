#!/bin/awk -f
{
	if ($1 == "#START") {
		FS=":";
	} else if ($1 == "#STOP") {
		FS=" ";
	} else {
		#print the Roman number in column 3
		print $3
	}
}

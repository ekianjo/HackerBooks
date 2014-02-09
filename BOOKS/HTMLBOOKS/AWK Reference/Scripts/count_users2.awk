#!/bin/awk -f
BEGIN {
	username[""]=0;
}
{
	username[$3]++;
}
END {
	for (i in username) {
		if (i != "") {
			print username[i], i;
		}
	}
}

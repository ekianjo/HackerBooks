#!/bin/awk -f
{
	username[$3]++;
}
END {
	for (i in username) {
		print username[i], i;
	}
}

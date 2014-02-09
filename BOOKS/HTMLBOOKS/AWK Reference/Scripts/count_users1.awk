#!/bin/awk -f
{
	if (NF>7) {
		username[$3]++;
	}
}
END {
	for (i in username) {
		print username[i], i;
	}
}

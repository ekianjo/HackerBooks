#!/usr/bin/awk -f
BEGIN {
	printf("%10s %6s\n", "String", "Number");
}
{
	printf("%10s %6d\n", $1, $2);
}

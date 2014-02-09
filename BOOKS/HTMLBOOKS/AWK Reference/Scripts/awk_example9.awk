#!/usr/bin/awk -f
BEGIN {
	printf("String     Number\n");
}
{
	printf("%10s %6d\n", $1, $2);
}

#!/usr/bin/awk -f
BEGIN {
	format1 ="%10s %6s\n";
	format2 ="%10s %6d\n";
	printf(format1, "String", "Number");
}
{
	printf(format2, $1, $2);
}

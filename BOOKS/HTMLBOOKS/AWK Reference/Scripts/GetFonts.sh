#!/bin/sh
# this script is called GetFonts
# it gets all fonts that have
#	long names
#	Roman slant
#	non-proportional font
# with point size <= MIN and >= MAX
MIN=10
MAX=20
xlsfonts | awk -F- '
BEGIN {
	minsize='$MIN' * 10;
	maxsize='$MAX' * 10;
}
$5 ~ /r/ && \
$12 !~ /p/ && \
$9 >= minsize && \
$9 <= maxsize { 
	print 
}
' 

#!/bin/sh
# Print a warning if any disk is more
# than 95% full.
/usr/ucb/df | tr -d '%' | awk '
# only look at lines where the first field contains a "/"
$1 ~ /\// {	if ($5 > 95) {
		printf("Warning, disk %s is %4.2f%% full\n",$6,$5);
	}
}'

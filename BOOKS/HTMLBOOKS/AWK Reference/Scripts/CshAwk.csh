#!/bin/csh -f
awk '{printf("%s\t%s\t%s\n",\\
$3, $2, $1}'


#!/bin/awk -f
{ if (NR > 100) {
	print NR, $0;
}

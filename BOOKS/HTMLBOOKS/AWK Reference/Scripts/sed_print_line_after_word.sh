#!/bin/sh
sed -n '
# by default - do not print anything
/ONE/ {
# append a line
	N
# if TWO found, print the first line
	/\n.*TWO/ P
}' file


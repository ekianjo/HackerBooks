#!/bin/sh
sed '
/ONE/ {
# append a line
	N
# if TWO found, delete the first line
	/\n.*TWO/ D
}' file


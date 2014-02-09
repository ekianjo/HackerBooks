#!/bin/sh
# scriptname: moveto
# usage: 
#	moveto directory files.....
directory=${1:?"Missing"};shift
mv $* $directory

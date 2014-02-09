#!/bin/sh
arg1="a.out"
arg2=`pwd`
arg3=$HOME
if [ $# -gt 3 ]
then
fi

if [ $# -eq 0 ]
then
	echo must specify at least one argument
	exit 1
else if [ $# -eq 1 ]
then
	arg1="$1";
else if [ $# -eq 2 ]
then
	arg1="$1";
	arg2="$2";
else if [ $# -eq 3 ]
then
	arg1="$1";
	arg2="$2";
	arg3="$3";
else 
	echo too many arguments
	exit 1
fi

mv $arg2/$arg1 $arg3

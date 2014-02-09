#!/bin/sh
arg=`echo "$1" | sed 's:[]\[\^\$\.\*\/]:\\\\&:g'`
sed 's/'"$arg"'//g'


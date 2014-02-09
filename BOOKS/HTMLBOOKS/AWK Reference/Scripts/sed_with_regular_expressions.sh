#!/bin/sh
arg=`sed 's:[\/\.\*\[\]\^\$]:&:g <<EndOfThisMess
$1
EndOfThisMess
`
sed 's/'"$arg"'//g'

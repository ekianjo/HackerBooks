#!/bin/sh
# Scriptname: EchoArgs
# It echoes arguments
#First - make sure we are using the Berkeley style echoes
PATH=/usr/ucb:$path;export PATH
E="echo -n"
# echo the name of the script
${E} $0:
# now echo each argument, but put a space
# before the argument, and place single quotes
# around each argument
${E} " '${1-"?"}'"
${E} " '${2-"?"}'"
${E} " '${3-"?"}'"
${E} " '${4-"?"}'"
${E} " '${5-"?"}'"
${E} " '${6-"?"}'"
${E} " '${7-"?"}'"
echo 


#!/bin/sh
# Given a directory, return the system it is mounted on
# If it is localhost, then echo `hostname`
dir=${1:?'No directory specified'}
cd $dir

# On SunOS 4.x, use /usr/bin/df before /usr/5bin
# On Solaris 5.x, use /usr/ucb/df before /usr/bin
# Solve the problem by specifying the explicit path
PATH=/usr/ucb:/usr/bin:/usr/5bin:$PATH
export PATH

x=`df . | grep -v Filesystem`
# use expr to extract the system name
server=`expr "$x" : '\(.*\)\:'`
# with sed, I could do $server=`echo $x | sed 's/:.*//'`
if [ "$server" ] 
then 
    echo $server
else
    hostname
fi


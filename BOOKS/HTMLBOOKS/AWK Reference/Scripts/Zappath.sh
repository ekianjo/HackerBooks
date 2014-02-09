#!/bin/sh 
# Zappath: created by Bruce Barnett 
# this script edits the output of the C shell "dirs"
# command and shortens the strings to a compact form
#
# Some example editing:
#
# 	remove the automount /tmp_mnt prefix
#	change /usr/export/home to /home
#	change /homedisk to /home
#	change $HOME into ~
# 	change /home/abc to abc
#	change /usr/etc to ./etc
#	change */*/ABC to ./ABC	
# one more thing:
# must change ~ to be -
sed '
s:/tmp_mnt::g
s:/usr/export/home:/home:g
s:/homedisk:/home:g
s:'${HOME}':~:g
s:/home/::g
s:/usr/:./:g
s:[^/ ]*/[^/ ]*/:./:g
s:~:-:g
'



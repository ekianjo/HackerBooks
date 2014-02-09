#!/bin/csh -f
# usage:
#   testdir
# function:
# analyze my account for security problems
# Just search the directory specified.
# if no directory specified,
#   search my home directory

set f = "$HOME"

#if an argument specified, 
# and it is a directory, use it

if ( $#argv == 1 ) then
	if ( -d $1 ) then
		set f = "$1"
	endif
endif


# list any files in my directory
# that are not owned by me

# System V
# set x = `find $f \! -user $LOGNAME -print`
# set LS = "ls -ld"

# SunOS:
set x = `find $f \! -user $USER -print`
set LS = "ls -lgd"

if ( $#x ) then
	echo "Files I don't own:"
	echo $x | xargs $LS
endif

# look for any files that are setuid
set x = `find $f -perm -4000 -print`
if ( $#x ) then
	echo "set UID files:"
	echo $x | xargs $LS
endif

set x = `find $f -type f -perm -2000 -print`
if ( $#x ) then
	echo "set gid files:"
	echo $x | xargs $LS
endif

set x = `find $f -type d -perm -2 -print`
if ( $#x ) then
	echo "World writable directories:"
	echo $x | xargs $LS
endif

set x = `find $f -type d -perm -20 -print`
if ( $#x ) then
	echo "Group writable directories:"
	echo $x | xargs $LS
endif

set x = `find $f -type f -perm -2 -print`
if ( $#x ) then
	echo "World writable files:"
	echo $x | xargs $LS
endif

set x = `find $f -type f -perm -20 -print`
if ( $#x ) then
	echo "Group writable files:"
	echo $x | xargs $LS
endif

# who has root access?

if ( -f /.rhosts && ! -z /.rhosts ) then
	echo "The following have root access:"
	cat /.rhosts
endif
# who has root access?

if ( -f /.rhosts && ! -z /.rhosts ) then
	echo "The following have root access:"
	cat /.rhosts
endif

if ( -f /etc/hosts.equiv ) then
	grep -s '^+$' /etc/hosts.equiv 
	if ( $status ) then
		echo "your machine trusts EVERY HOST on the network"
		echo "Anyone who can become root on a computer"
		echo " can log onto your account"
	else
		echo "Your machines trusts the following hosts"
		echo "Anyone who can become root on these systems "
		echo " can log onto your account."
		cat /etc/hosts.equiv
		# should expand newgroups
	endif
endif

if ( -f ~/.rhosts ) then
	echo "the following accounts can log into your account:"
	cat ~/.rhosts
endif

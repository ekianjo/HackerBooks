#!/bin/csh -f
# usage:
#   write2dir <directory>
#   list people who can write to specified directory
if ( $#argv != 1 ) then
	echo "usage: $0 directory"
	exit 1
endif
set dir = $1
# make sure argument is directory
if ( ! -d $dir ) then
	echo "$0: $dir not a directory"
	exit 1
endif

set LS="/usr/bin/ls -ldg"
#set LS="/usr/5bin/ls -ld"
set p = (`$LS $dir`)
# p = ( drwxr-xr-x   3 barnett  staff [...] )

set perm = $p[1]
set owner = $p[3]
set group = $p[4]

# see if directory is world writable
# if so, output special string
if ( $perm =~ d???????w? ) then
	echo "_EVERYONE"
else if ( $perm =~ d????w???? ) then
	set gid = `gid $group`
	# read passwd file
	set samegid = (`havegid $gid`)
	# read group file
	set samegroup = (`ingroup $gid`)
	foreach i ( $owner $samegid $samegroup )
		# output one user per line
		echo $i
	end
endif	

#!/bin/csh -f
# usage:
#   testsearch
# function:
# gives list of people who can modify commands I execute
set founddot = 0
set u = ( )
set unsafe = ( )
foreach p ( $path )
	if ( $founddot ) then
		set unsafe = ( $unsafe $p )
	else if ( $p == "." ) then
		set founddot = 1
	endif
	# add to array u list of users
	set u = ($u `write2dir $p`)
end
# now output list of users in sorted order
echo "The following people can break into my account:"
echo $u | tr ' ' '\012' | sort | uniq

if ( $#unsafe ) then
	echo "The following directories "
	echo "  have commands that can be interecepted:"
	echo "  $unsafe"
endif

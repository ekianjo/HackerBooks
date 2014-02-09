#!/bin/csh -f
# usage
# ted [-arg value ] file [file ....]
#
set args = ()
again:
if ($#argv > 2) then
	# only do this if the option is "-E<x> <value>"
	# put an "X" before both strings before comparing
	# as if the option was "-f", csh would complain
	if ( X$1 =~ X-[E][a-zA-Z] ) then
		set args = ( $args $1 $2 );shift;shift
		goto again
	endif
endif

foreach i ( $* )
	# get size of file
	if ( -f $i ) then
		set size = (`height_width.awk <$i`)
# too bad -width <columns> doesn't work
#		echo textedit -En $size[1] -width $size[2] $i 
		echo textedit -En $size[1] $args  $i 
		textedit -En $size[1] $args $i &
	else
		echo file $i not found
	endif
end



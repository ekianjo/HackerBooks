#!/bin/csh -f
foreach p ( $path )
    if ( -d $p ) then
	set newp = (`ResolveDir $p`)
	set server = (`Dir_to_System $p`)
	echo "${p}:${newp}:${server}"
    else
	echo "${p}:?:?"
    endif
end


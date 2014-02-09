#!/bin/echo use source to execute this command
# variable a = filename metacharacter
# variable b = command to execute

# source this to define the alias
if ( ! $?FOREACH_def) then
	alias FOREACH 'set a = \!:1; \\
		set b = (\!:2*);\\
		source ~/source_alias/FOREACH.csh;'
	set FOREACH_def
else
    echo $b | grep '#' >/dev/null
    # remember status
    set r = $status
    foreach i ( $a )
	if ( $r == 0 ) then
	    # change '#' to $i
	    set B = `echo $b | sed 's/#/'$i'/g'`
	else
	    # Add a '$i' to the end, if it is missing
	    set B = `echo $b | sed 's/$/ '$i'/'`
	endif
	eval $B
    end
endif


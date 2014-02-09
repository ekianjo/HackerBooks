#!/bin/echo use source to execute this command
# variable a = filename metacharacter
# variable b = command to execute

# source this to define the alias
if ( ! $?FOREACHr_def) then
	alias FOREACHr 'set a = \!:1; \\
	set b = (\!:2*); \\
	source ~/source_alias/FOREACHr.csh;'
	set FOREACHr_def
else
    echo $b | grep '#' >/dev/null
    # remember status
    set r = $status
    foreach i ( $a )
	# Here is the different part
	set j = $i:r
	if ( $r == 0 ) then
	    # change '#' to $j
	    set B = `echo $b | sed 's/#/'$j'/g'`
	else
	    set B = `echo $b | sed 's/$/ '$j'/'`
	endif
	eval $B
    end
endif


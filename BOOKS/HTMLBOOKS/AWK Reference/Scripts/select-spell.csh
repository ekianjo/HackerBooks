#!/bin/csh -f
# Bruce Barnett Thu Mar 30 11:28:22 EST 1989
# This is a script to check spelling of something selected
# calling sequence is
#       select-spell [arg]
# where [arg] can be 1, 2 or 3, or f
# if missing, assume 1
# 1 = get selection from primary selection
# 2 = get selection from secondary selection
# 3 = get selection from clipboard
# f = get selection from primary selection, which is a number of files
# 
# improvements suggested by Martin Kooij
onintr bye
# if no arguments, assume primary selection, not using files
set selection = 1
set usefile = 0
if ( $#argv  !=  0 ) then
        set selection = $argv[1]
endif
if ( $selection !~ [123fF] ) exit 1
if ( $selection =~ [fF] ) then
        set selection = 1
        set usefile = 1
endif
# keep list of used filenames for cleanup afterwards
set usedfiles = (/tmp/getA$$)
#set TED = "textedit -width 38 -Es 0"
set TED = "textedit -width 38"
if ($?DISPLAY) then
# X11
	xv_get_sel $selection  >/tmp/getA$$
else
# sunview
	get_selection $selection  >/tmp/getA$$
endif
if ( $status > 0  || -z /tmp/getA$$ ) exit 1
echo "" >>/tmp/getA$$
if ( $usefile ) then	# read selection for each filename
	foreach f (`cat /tmp/getA$$`)
		set file = "/tmp/$f:t.$$"
		set usedfiles = ( $usedfiles $file )
		spell <$f >$file
		if ( ! -z $file ) then # not zero length
			set height = `wc -l <$file`
			if ( $height > 20 ) then
				set height = 20
			else
				@ height += 2
			endif	
			pushd /tmp >/dev/null
			$TED -height $height $file:t &
			popd
		end
	endif
else
	set file = "/tmp/badspell.$$"
	set usedfiles = ( $usedfiles $file )
        spell -b </tmp/getA$$ >$file
	set height = `wc -l <$file`
	if ( ! -z $file ) then
		if ( $height > 20 ) then
			set height = 20
		else
			@ height =+ 2
		endif
		pushd /tmp >/dev/null
		$TED -height $height $file:t
		popd 
	endif

endif
wait	# for all textedits to quit
bye:
/bin/rm -f /tmp/getA$$ $usedfiles
exit 0


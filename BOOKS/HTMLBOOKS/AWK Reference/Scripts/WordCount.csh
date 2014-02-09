#!/bin/csh
# arguments are $*
foreach i ( $* )
	echo file $i has `wc -l <$i` lines
end


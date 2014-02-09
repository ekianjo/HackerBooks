#!/bin/csh -f
foreach i ( $* )
	textedit $i &
end


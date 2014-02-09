#!/bin/csh -f
foreach i ( $* )
        # get size of file
        set wc = `wc -l <$i`
        if ( $wc < 5 ) set wc = 5
        if ( $wc > 30 ) set wc=30
        
#        echo textedit -En $wc $i 
        textedit -En $wc $i &
end


#!/bin/csh -f
# A simple version of which that prints all 
# locations that contain the command
if ( $#argv != 1 ) then
    echo "Wrong number of arguments - usage: 'which command'"
    exit 1
endif
foreach dir ( $path )
    if ( -x $dir/$1 ) echo $dir/$1
end

# example .path file

if ( -f ~/.path.default ) then
    source ~/.path.default
else
    # this is a default searchpath
    set path = ( ~/bin /usr/ucb /usr/bin /usr/local/bin /local/bin )
endif

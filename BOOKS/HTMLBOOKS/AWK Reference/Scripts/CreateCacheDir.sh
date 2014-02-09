#!/bin/sh
# Argument #1 is the directory where we will cache
# a filename. Actually, not a cache, but a link.
# where is the cache directory?
# Usage
#     CreateCacheDir Cachedir dir1 [dir2 ...]
# Function:
# - Create a symbolic link in cachedir, pointing to the files in dir1, etc.
#
CACHE=${1:?'Target directory not defined'}
if [ ! -d "$CACHE" ]
then
	echo making cache directory "$CACHE"
	mkdir $CACHE
fi

shift

# The rest of the arguments are directories to cache

verbose=false # true to see what happens
debug=false # true if you want extra information
doit=true # false if you don't want to change anything

for D in $*
do
    $verbose && echo caching directory $D
    # list files, but ignore any that end with ~, or # or % (backup copies)
    for f in `cd $D;ls|grep -v '[~#%]$'`
    do
        if [  -f $CACHE/$f ]
	then
	    $debug && echo $CACHE/$f already exists
	else
	    if [ -f $D/$f -a -x $D/$f ]
	    then
	    echo $D/$f
 		$verbose && echo ln -s $D/$f $CACHE/$f 
		$doit && ln -s $D/$f $CACHE/$f 
	    elif [ -d $D/$f ]
	    then
		$verbose && echo linking directory: ln -s $D/$f $CACHE/$f 
		$doit && ln -s $D/$f $CACHE/$f 
	    else
		$verbose && echo linking other: ln -s $D/$f $CACHE/$f 
		$doit && ln -s $D/$f $CACHE/$f 
	    fi
	fi
    done
echo you can now take $D out of your searchpath
	
done


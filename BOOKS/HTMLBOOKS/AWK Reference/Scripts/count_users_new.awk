#!/bin/sh
find . -type f -print | xargs ls  -isl | \
awk '
BEGIN {
# initialize all arrays used in for loop
	count[""]=0;
	fsize[""]=0;
}
{
# validate your input
        if (NF != 10) {
                printf("I was expecting 10 columns, but found %d for the output of ls. Please tweak the script\n",NF);
				exit;
#	ignore
	} else {
# assign field names
		inode=$1;
		flsize=$2;
		linkcount=$4;
		user=$5;
		group=$6; 

# should I count this file?

		doit=0;
		if (linkcount == 1) {
# only one copy - count it
			doit++;
		} else {
# a hard link - only count first one
			seen[inode]++;
			if (seen[inode] == 1) {
				doit++;
			}
		}
# if doit is true, then count the file
		if (doit ) {

# total up counts in one pass
# use description array names
# use array index that unifies the arrays

# first the counts for the number of files

			count[user " *"]++;
			count["* " group]++;
			count[user " " group]++;
			count["* *"]++;

# then the total disk space used

			fsize[user " *"]+=flsize;
			fsize["* " group]+=flsize;
			fsize[user " " group]+=flsize;
			fsize["* *"]+=flsize;
		}
        }
}
END {
# output in a form that can be sorted
        for (i in count) {
		if (i != "") {
        	        print fsize[i], count[i], i;
		}
        }
} ' | \
# numeric sort - biggest numbers first
# sort fields 0 and 1 first (sort starts with 0)
# followed by dictionary sort on fields 2 + 3
sort +0nr -2 +2d | \
# add header
(echo "size count user group";cat -) |\
# convert space to tab - makes it nice output
# the second set of quotes contains a single tab character
tr ' ' '	' 
# done - I hope you like it

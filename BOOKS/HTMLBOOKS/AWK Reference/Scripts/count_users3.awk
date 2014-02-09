#!/bin/sh
find . -type f -print | xargs /bin/ls -islg | \
awk '
BEGIN {
# initialize all arrays used in for loop
	u_count[""]=0;
	g_count[""]=0;
	ug_count[""]=0;
	all_count[""]=0;
}
{
# validate your input
        if (NF != 11) {
#	ignore
	} else {
# assign field names
		inode=$1;
		size=$2;
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

			u_count[user " *"]++;
			g_count["* " group]++;
			ug_count[user " " group]++;
			all_count["* *"]++;

# then the total disk space used

			u_size[user " *"]+=size;
			g_size["* " group]+=size;
			ug_size[user " " group]+=size;
			all_size["* *"]+=size;
		}
        }
}
END {
# output in a form that can be sorted
        for (i in u_count) {
		if (i != "") {
        	        print u_size[i], u_count[i], i;
		}
        }
        for (i in g_count) {
		if (i != "") {
        	        print g_size[i], g_count[i], i;
		}
        }
        for (i in ug_count) {
		if (i != "") {
        	        print ug_size[i], ug_count[i], i;
		}
        }
        for (i in all_count) {
		if (i != "") {
        	        print all_size[i], all_count[i], i;
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

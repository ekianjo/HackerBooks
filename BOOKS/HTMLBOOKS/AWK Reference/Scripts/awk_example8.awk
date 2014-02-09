#!/bin/awk -f
# bad example of AWK programming
# this counts how many files each user owns.
BEGIN {
	number_of_users=0;
}
{
# must make sure you only examine lines with 8 or more fields
	if (NF>7) {
		user=0;
# look for the user in our list of users
		for (i=1; i<=number_of_users; i++) {
#		is the user known?
			if (username[i] == $3) {
# found it - remember where the user is
				user=i;
			}
		}
		if (user == 0) {
# found a new user
			username[++number_of_users]=$3;
			user=number_of_users;
		}
# increase number of counts
		count[user]++;
	}
}
END {
	for (i=1; i<=number_of_users; i++) {
		print count[i], username[i]
	}
}

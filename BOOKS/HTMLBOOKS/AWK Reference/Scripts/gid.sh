#!/bin/sh
# usage:
#   gid <groupname>
#   returns ID number of group
grp=${1:?}
# select one of the two below:
CATGROUP="ypcat group"
#CATGROUP="cat /etc/group"
# if field 1 matches group, 
#  print field 3 of the group file
$CATGROUP | \
 awk -F: ' $1 ~ /^'$grp'$/ {print $3}'

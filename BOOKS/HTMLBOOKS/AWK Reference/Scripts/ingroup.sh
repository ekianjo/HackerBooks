#!/bin/sh
# usage:
#   ingroup <gid>
#   returns everyone in <gid>
gid=${1:?}
# select one of the two below:
CATGROUP="ypcat group"
#CATGROUP="cat /etc/group"
# if field 3 matches gid, 
# print field 4 of the group file
$CATGROUP | \
  awk -F: ' $3 ~ /^'$gid'$/ {print $4}' | \
   tr ',' '\012'

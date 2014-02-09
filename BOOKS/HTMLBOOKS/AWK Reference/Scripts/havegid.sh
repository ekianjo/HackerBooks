#!/bin/sh
# usage:
#   havegid <gid>
#   returns everyone with same gid in the passwd file
gid=${1:?}
#CATPASS="cat /etc/passwd"
CATPASS="ypcat passwd"
# if field 4 matches gid, print username
$CATPASS | \
 awk -F: ' $4 ~ /^'$gid'$/ {print $1}'

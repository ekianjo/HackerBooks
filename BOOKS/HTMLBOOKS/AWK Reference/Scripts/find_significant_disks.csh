#!/bin/csh -f

# find significant disks

echo "the following disk partitions are significant:"
echo "check the export permissions of each one"
df ~ $path | \
 grep '^[a-z/]' | \
 awk '{print $1}' | \
 sort | uniq


#!/bin/sh
# rename: - rename a file
# Usage: rename oldname newname
oldname=$1
newname=$2
mv ${oldname:?"missing"} ${newname:?"missing"}


#!/bin/sh
# Find the unique and final location of a directory
# Usage:
#   ResolveDir directoryname
#
# If the directory is called ".", return "."
dir=${1:?'Missing argument'}

[ "$dir" = "." ] && { echo "."; exit 0; }
cd $dir  >/dev/null 2>&1 && { pwd; exit 0; }
exit 1;


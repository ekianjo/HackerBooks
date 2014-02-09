#!/bin/sh
#NOTE - this script does not work!
column=$1
awk '{print $$column}'

#!/bin/sh
column=$1
awk '{print $'$column'}'

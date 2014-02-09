#!/bin/sh
column=${1:-1}
awk '{print $'$column'}'

#!/bin/sh
sed '=' file | \
sed '{
	N
	s/\n/ /
}'


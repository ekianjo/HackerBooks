#!/bin/sh
sed '/INCLUDE/ {
	r file
	d
}'


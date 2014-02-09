#!/bin/sh
sed '
:again
	s/([ ^I]*)//g
	t again
'

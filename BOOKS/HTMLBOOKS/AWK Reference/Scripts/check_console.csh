#!/bin/csh -f
# check to see if this workstation is secure from single user rebooting
set a = `grep "console" /etc/ttytab | sed 's/#.*$//' |  grep secure | wc -l`

if ( $a == 1  ) then
	echo your workstation is not secure from a single user  reboot
endif

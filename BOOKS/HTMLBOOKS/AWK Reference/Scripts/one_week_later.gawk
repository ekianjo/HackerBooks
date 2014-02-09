#!/usr/local/bin/gawk -f
BEGIN {
#  get current time	
   ts = systime();
# the time is in seconds, so
   one_day = 24 * 60 * 60;
   next_week = ts + (7 * one_day);
   format = "%a %b %e %H:%M:%S %Z %Y";
   print strftime(format, next_week);
   exit;
}

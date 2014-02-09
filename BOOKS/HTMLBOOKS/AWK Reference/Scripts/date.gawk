#! /usr/local/bin/gawk -f
#

BEGIN {
    format = "%a %b %e %H:%M:%S %Z %Y";
    print strftime(format);
}

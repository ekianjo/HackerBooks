#!/bin/awk -f
{
# field 1 is the e-mail address - perhaps
    if ((x=index($1,"@")) > 0) {
        username = substr($1,1,x-1);
        hostname = substr($1,x+1,length($1));
# the above is the same as
#        hostname = substr($1,x+1);
        printf("username = %s, hostname = %s\n", username, hostname);
    }
}

#!/usr/bin/awk -f
# convert upper case letters to lower case
BEGIN {
    LC="abcdefghijklmnopqrstuvwxyz";
    UC="ABCDEFGHIJKLMNOPQRSTUVWXYZ";
}
{
    out="";
# look at each character
    for(i=1;i<=length($0);i++) {
# get the character to be checked
        char=substr($0,i,1);
# is it an upper case letter?
        j=index(UC,char);
            if (j > 0 ) {
# found it
                out = out substr(LC,j,1);
            } else {
                out = out char;
            }
    }
    printf("%s\n", out);
}    

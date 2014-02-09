#!/usr/bin/awk -f
BEGIN {
# this script breaks up the sentence into words, using 
# a space as the character separating the words
    string="This is a string, is it not?";
    search=" ";
    n=split(string,array,search);
    for (i=1;i<=n;i++) {
        printf("Word[%d]=%s\n",i,array[i]);
    }
    exit;
}

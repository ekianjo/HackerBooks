#!/usr/bin/nawk -f
# demonstrate the match function

BEGIN {
    regex="[a-zA-Z0-9]+";
}
{
    if (match($0,regex)) {
#           RSTART is where the pattern starts
#           RLENGTH is the length of the pattern
            before = substr($0,1,RSTART-1);
            pattern = substr($0,RSTART,RLENGTH);
            after = substr($0,RSTART+RLENGTH);
            printf("%s<%s>%s\n", before, pattern, after);
    }
}

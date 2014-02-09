#!/usr/bin/awk -f
# look for a \ as the last character.
# if found, read the next line and append
{
    line = $0;
    while (substr(line,length(line),1) == "\\") {
# chop off the last character
        line = substr(line,1,length(line)-1);
        i=getline;
        if (i > 0) {
            line = line $0;
        } else {
            printf("missing continuation on line %d\n", NR);
        }
    }
    print line;
}

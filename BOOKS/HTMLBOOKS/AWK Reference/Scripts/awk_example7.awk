#!/bin/awk -f
{ 
    if (NF == 6) {
        # do the right thing
    } else {
        if (FILENAME == "-" ) {
            print "SYNTAX ERROR, Wrong number of fields,", \
            "in STDIN, line #:", NR,  "line: ", $0;
        } else {
            print "SYNTAX ERROR, Wrong number of fields,", \
            "Filename: ", FILENAME, "line # ", NR,"line: ", $0;
        }
    }
}

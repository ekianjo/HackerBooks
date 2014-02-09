#!/usr/bin/nawk -f
{
    if (NF != 4) {
        error("Expected 4 fields");
    } else {
        print;
    }
}
function error ( message ) {
    if (FILENAME != "-") {
        printf("%s: ", FILENAME) > "/dev/tty";
    }
    printf("line # %d, %s, line: %s\n", NR, message, $0) >> "/dev/tty";
}

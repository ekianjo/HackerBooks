#!/usr/local/bin/gawk -f
# how long does it take to do a few loops?
BEGIN {
    LOOPS=100;
# do the test twice
    start=systime();
    for (i=0;i<LOOPS;i++) {
    }
    end = systime();
# calculate how long it takes to do a dummy test
    do_nothing = end-start;
# now do the test again with the *IMPORTANT* code inside
    start=systime();
    for (i=0;i<LOOPS;i++) {
# How long does this take?
        while ("date" | getline) {
            date = $0;
        }
        close("date");
    }
    end = systime();
    newtime = (end - start) - do_nothing;

    if (newtime <= 0) {
        printf("%d loops were not enough to test, increase it\n", 
            LOOPS);
        exit;
    } else {
        printf("%d loops took %6.4f seconds to execute\n", 
            LOOPS, newtime);
        printf("That's %10.8f seconds per loop\n", 
            (newtime)/LOOPS);
# since the clock has an accuracy of +/- one second, what is the error
        printf("accuracy of this measurement = %6.2f%%\n",
            (1/(newtime))*100);
    }
    exit;
}

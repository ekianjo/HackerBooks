#!/usr/bin/awk -f
END {
    for (i=0;i<30;i++) {
	printf("i=%d\n", i) > "/tmp/a" i;
    }
}

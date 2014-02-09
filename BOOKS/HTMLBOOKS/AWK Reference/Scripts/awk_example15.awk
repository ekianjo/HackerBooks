#!/usr/bin/nawk -f
BEGIN {
    string = "Another sample of an example sentence";
    pattern="[Aa]n";
    if (gsub(pattern,"AN",string)) {
        printf("Substitution occurred: %s\n", string);
    }

    exit;
}

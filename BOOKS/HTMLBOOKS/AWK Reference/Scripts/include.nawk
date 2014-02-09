#!/usr/bin/nawk -f
{
# a primitive include preprocessor
    if (($1 == "#include") && (NF == 2)) {
# found the name of the file
        filename = $2;
        while (i = getline < filename ) {
            print;
        }
    } else {
        print;
    }
}

#!/bin/sh
# spelling filter version 3
# with marked text
FILE=/tmp/spell.$$
FILE1=${FILE}1
# delete any temporary file or exit or interrupt
trap "/bin/rm $FILE $FILE1" 0 1 2 15
cat >$FILE
# create a sed script for each misspelled word
# i.e. if the word is "misspulled"
# create a like that changes "misspulled" to |>misspuled<|"
# use sed's \< and \> to limit the change to words
# and not middle of words
# an example sed command will be
#    s/\<misspulled\>/|>misspulled<|/g
# the "/g" at the end will change the word 
# if it appears twice on one line
spell < $FILE |awk '{printf("s/\<%s\>/|>%s<|/g\n",$1,$1);}' >$FILE1
# need to use /bin/sed and not /usr/ucb/sed in Solaris
/bin/sed -f $FILE1 <$FILE


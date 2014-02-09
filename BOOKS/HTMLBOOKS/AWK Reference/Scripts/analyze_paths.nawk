#!/usr/bin/nawk -f
# Do this before you read any input
BEGIN {
  FS=":";
}

# do this for each line
(NF==3) {
  if ($3 ~ /\?/ ) {
# then it is a directory that does not exist    
    missing[$1]=1;
    number_of_missing++;
  } else if ( $1 ~ /\./ ) {
# ignore it  - it is the "." directory
  } else {
# count how many times each directory is used
    used_count[$2]++;
# is it a duplicate,
    if ($1 !~ $2) {
      links[$2]++;
# remember it, by catenating two strings
      used[$2] = used[$2] " "  $1;
    }

# Is it a remote system?
    if ($3 !~ HOSTNAME) {
      systems[$3]++;
# if this is the first time we have seen this directory      
	system_to_dir[$3] = 
	   system_to_dir[$3] " " $1;
      remote_systems++;
    }
  }

#  printf("%s\t%s\t%s\n",$1, $2, $3);
}
# Do this at the end of the file
END {
# Any directories that do not have to be included?

  if (number_of_missing>0) {
    printf("Directories that don't exist on this system:\n");
    for (i in missing) {
      printf("\t%s\n", i);
    }
  }

# how many computer systems are needed?

  if (remote_systems) {
    printf("You are dependent upon the following systems:\n");
    for (i in systems ) {
        printf("\tsystem %s, directories: %s\n", i, system_to_dir[i]);
    }
    
  } else {
    printf("Good! You are not dependent upon any other servers,");
for your current directory\n");
    printf(" except for your current directory\n");
  }


# What about duplicate directories?

  for (i in used ) {
    if (used_count[i]>1) {
      printf("\nDirectory %s used %d times (symbolic links: %d)\n", 
	     i, used_count[i],  links[i]);
      if (links[i]>0) {
	printf("\tsymbolic links for '%s' are: %s\n", i, used[i]);
      }
    }
  }

}

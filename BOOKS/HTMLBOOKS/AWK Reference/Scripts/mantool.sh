#! /bin/sh
# mantool: manual page lookup tool
# %W%	%G%
# Bruce Barnett 
#
# This shellscript is used to create textedit-windows displaying the
# various manual pages.
# This allows you to use the OpenLook scrollbars to move through the text
# as well as letting the FIND function key search for appropriate text
# You also get the OpenLook style of scrollbars, cut and paste, 
# as well as secondary selections.
#
# In simple terms, you specify as an argument a descriptor of
# a manual page. This script finds the appropriate page, creates a text file,
# and starts up a textedit window displaying the manual page.
# The title bar of textedit - alone with the icon label -
# follows (hopefully) the unix convention of 
#		mumble(1)
# Therefore you can have several manual pages on the desktop and quickly find
# the one you want.
#
# There is a slight problem. This script must start up another script that
# displays the file, and then deletes the file afterwards. 
# This requires the execution
# of a second script, called helptool.
#

# usage:
# either
# 	mantool  <argument>
# or
#	cmdtool -Wh 10 mantool &
# In the first case, the argument specifies the manual page desired.
# In the second case, a new window is created that prompts for input.
# The user can type in a manual page, or ask for simple help.
# If the user types a blank line, the window will exit.


# System V uses apropo instead of man -k
#APROPOS="apropos"
APROPOS="man -k"
if [ -n "$1" ]
then
	# the command was executed with arguments
	# set variable to only loop once
	LOOPONCE="YES"
	# set variable "what" to all of the arguments
	what="$@"
else
	# prompt for input
	echo "What command do you wish to look up? (type ? for help)"
	read what
fi
# loop here - one time for each response
while [ -n "$what" ] 
# true while a non-zero length argument is typed
do
	# set the positional paramaters using the $what variable
	# What out for arguments like
#	          dd(1), ed(1), sh(1), ascii(5).
	# We must remove all commas and periods so we can parse each argument
	# the arguments are the same, but commas are replaced by spaces
	set `echo "$what"|tr ',.' '  '`

	# the positional parameters $1, $2, $3, etc. are set
	# loop thru each one
	while [ $# -gt 0 ]
	do
		case "$1" in
		\?)
			shift		
			# start of the ? response
			# everything until the matching EOF 
			# is printed to the screen
	                cat <<"EOF"
This will type out the manual page for a command/file
Formats are:

     command
     chapter
     chapter command
     command(chapter)
     -k keyword
     -f filename

If -k keyword, then list all commands/files
   that have keyword or phrase in one-line description

 Chapters are:
      1 - programs you can execute from the command line
      2 - system calls available to a C program
      3 - library calls from a C ir FORTRAN program, categories include:
         3F - fortran     3C - compatible 
         3N - Networking  3M - Math routines
         3X - Extra libraries
      4 - devices
      5 - file formats
      6 - games
      7 - useful tables (ASCII, nroff macros)
      8 - administration programs
      L - local

It is useful to ask for an overview of each chapter.
This is always called 'intro', e.g. 
	intro(1) 
lists all possible commands. I suggest you start there.
You can also type 
	help 
for a list of useful commands.

EOF

			;;
	
		help)
			shift
			# if the user types "help", 
			# give a short summary of commands
                echo " 
USEFUL COMMANDS:
         mv     - move or rename a file
         more   - look at a text file
         cp     - copy a file
         rm     - remove a file
         cd dir - change directory( see csh(1))
         cd     - go to home directory (see csh(1))
         mkdir  - make a new directory
         rmdir  - remove an empty directory
         ls     - list files in a directory
"
	# end of echo
                echo "Ask for the manual page on your shell  (i.e. $SHELL)"
                echo " for more information"
			;;
		[1-8lLlPp]|[1-8lLlPp]?)
			# Matches 1, 1C, 2, 2V, and even (L)ocal or (P)ublic
			# if this is the last (only) argument, 
			# it is asking for a summary
			if [ $# -gt 1 ]
			then

				SECTION=$1;
				CMD=$2;
				shift;shift;
				# need to pass two arguments
				echo helptool $SECTION $CMD
				helptool $SECTION $CMD
			else
				$APROPOS $1| grep "($what[A-Z]*)"|sort|uniq
				shift
			fi
			;;
                -k)   
			KEY=$1;
			WORD=$2;
			shift;shift;

			eval $APROPOS $KEY WORD | more 
			 ;;
                -f)   
			KEY=$1;
			WORD=$2;
			shift;shift;
			eval man $KEY $WORD | more 
			 ;;
		*)
			# can be "cmd" or "cmd(1)"
			# so must quote parentheses
			ARG="$1";shift;
			helptool $ARG
			;;
		esac
	done #	while [ $# -gt 0 ]
	if [ ${LOOPONCE} ]
	then
		what=""
	else		
	        echo "Type return to exit, or next command"
	        read what
	fi
done # while [ -n "$what" ] 

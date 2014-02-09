# C shell aliases to display hosts, directories, and directory stacks
# in the window title bar, icon string, and directory prompt
# created by Bruce Barnett 
# Based on the SunOS 3.5 Release notes
# Usage:
#	if ( -f ~/.header && -f ~/bin/Zappath ) source ~/.header
#
# the SP alias sets the directory prompt
# the setbar alias changes the window title bar and icon string
# define them here as the default case

	alias SP 'set prompt="$cwd:t% "'
	alias setbar 'echo \!* >/dev/null'

# If not a sun cmdtool or shelltool, or not an X terminal, exit.
if ( ! ( $term =~ sun* ) &&  ! ( $term =~ xterm )) goto getout

# if using a raw console, don't do anything
if ( `tty` =~ /dev/console ) goto getout

# set a few variables for later
# but only if the environment variable is not set

if ( ! $?HOSTNAME ) then
	setenv  HOSTNAME `hostname`
endif

# find the home machine
# is there a file that has a machine name in it?
if ( -f  ~/.display ) then
	set mymachine = `sed -e 's/:.*//' <~/.display`
else
	# obviously change this to match your
	# default system. Mine is "grymoire" - of course
	set mymachine = "grymoire"
# alternately, some people use "who am i"
endif

set console = '<< CONSOLE >>'

# figure how how to generate escape, bell, 
# and echo commands without a a line terminator
# I may have done this before. If so, the variable E is set

# have I executed this script before on this system?
if ( $?E ) then
#	echo "already set the echo variables">/dev/tty
else if ( -f ~/.echo.${HOSTNAME} ) then
	source ~/.echo.${HOSTNAME}
else if ( `echo -n |wc -l`  == 0 ) then
#	echo "built in echo is bsd" >/dev/tty
	# then berkeley style echo
	echo 'set ech = "echo -n"' >~/.echo.${HOSTNAME}
	echo "set E = `echo a | tr a '\033'`" >> ~/.echo.${HOSTNAME}
	echo "set B = `echo a | tr a '\007'`" >> ~/.echo.${HOSTNAME}
	echo 'set N = ""' >> ~/.echo.${HOSTNAME}
	source ~/.echo.${HOSTNAME}
else 
#	echo "built in echo is sysV" >/dev/tty
	echo 'set ech = "echo"' >~/.echo.${HOSTNAME}
	echo 'set E = "\033"' >> ~/.echo.${HOSTNAME}
	echo 'set B = "\007"' >> ~/.echo.${HOSTNAME}
	echo 'set N = "\c"' >> ~/.echo.${HOSTNAME}
	source ~/.echo.${HOSTNAME}
endif	


# Are we using shelltool, cmdtool or xterm?
# duplicate these aliases here to avoid problems
if ( $term =~ sun* ) then
	# Sun Aliases
	alias Header '${ech}  "${E}]l\!:1${E}\${N}"'
	alias IHeader '${ech}  "${E}]L\!:1${E}\${N}"'
else if ( $term =~ xterm ) then
	alias Header '${ech}  "${E}]2;\!:1${B}${N}"'
	alias IHeader '${ech}  "${E}]1;\!:1${B}${N}"'
endif

# There are three different combinations:
# 1) A window on a remote machine
# 2) A window on my machine
# 3) A console on my machine

# test for each case:

if (${HOSTNAME} != $mymachine ) then
	# it is a remote machine, therefore:
	# window title has machinename and dirs 
	# icon has machine name only
	# prompt has machine name+directory

       alias setbar 'Header "${HOSTNAME}: `dirs | ~/bin/Zappath`" ; IHeader ${HOSTNAME}'

# use either of these two lines to suit your tastes
# the first one shows the command number and full directory path
# The second shows just the hostname and the tail of the directory name

#	alias SP 'set prompt="[\\!] ${HOSTNAME}:$cwd % "'
	alias SP 'set prompt="${HOSTNAME}:$cwd:t% "'

else if ( `tty`  == "/dev/console" ) then
	goto getout
else if ( `tty`  == "/dev/ttyp0" ) then

# in this case an assumption is made that the first pty 
# window to appear is the console window.
# It's not always true, but it usually works

	# window title has <<CONSOLE>> and dirs 
	# icon has "console" only
	# prompt has directory

	alias setbar 'Header "${console} `dirs | ~/bin/Zappath`"'

# both of these works - pick one that suits you
#	alias SP 'set prompt="[\\!] $cwd % "'
	alias SP 'set prompt="$cwd:t% "'
else
	# a plain window on my localhost
	# window title has dirs 
	# icon has cwd only
	# prompt has directory
	# The next line must be one line, and not split onto two
	alias setbar 'Header "`dirs | ~/bin/Zappath `"; IHeader "`echo $cwd| ~/bin/Zappath`"'
#	alias SP 'set prompt="[\\!] $cwd % "'
	alias SP 'set prompt="$cwd:t% "'
endif

# redo current window
alias . 'dirs|~/bin/Zappath;setbar;jobs'

#  change cd to change prompt, window and icon title
alias cd 'chdir \!*; SP;setbar'
alias pushd 'pushd \!*; SP;setbar'
alias popd 'popd \!*; SP;setbar'

SP;setbar
getout:
# end


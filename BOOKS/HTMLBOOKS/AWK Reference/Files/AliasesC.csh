alias C 'eval "if (\!:1 !~ *.c) then \\
	echo "Error: this is for C programs only" \\
	echo "Extension should be .c on file \!:1, not .\!:1:e" \\
    else \\
	if ( -e \!:1:r ) mv \!:1:r \!:1:r.old\\
	cc -o !:1:r !:1:r.c \!:2* \\
    endif


#!/bin/csh -f
# fragment of code for your .cshrc file
if ( $term =~ sun* ) then
# Sun Aliases
 alias Open '${ech}  "${E}[1t${N}"'
 alias Close '${ech}  "${E}[2t${N}"'
 alias Front '${ech}  "${E}[5t${N}"'
 alias Back '${ech}  "${E}[6t${N}"'
 alias Move  '${ech}  "${E}[3;\e!:1;\e!:2t${N}"'
 alias Resize '${ech}  "${E}[4;\e!:1;\e!:2t${N}"'
 alias Header '${ech}  "${E}]l\e!*${E}\e${N}"'
 alias IHeader '${ech}  "${E}]L\e!*${E}\e${N}"'
else if ( $term =~ xterm ) then
 alias Header '${ech}  "${E}]2;\e!*${B}${N}"'
 alias IHeader '${ech}  "${E}]1;\e!*${B}${N}"'
endif

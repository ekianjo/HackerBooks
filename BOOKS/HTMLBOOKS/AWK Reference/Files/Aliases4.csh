# sort by date:
alias newest 'ls -lt | head -30'
alias oldest 'ls -ltr | head -30'
# sort by size:
alias biggest 'ls -ls|sort -nr | head -30'
alias smallest 'ls -ls|sort -n | head -30'
# sort by time last used
alias popular 'ls -lut | head -30'
alias unpopular 'ls -lutr | head -30'
# Sort by link time
alias lsst 'ls -lct | head -30'
alias lsstr 'ls -lctr | head -30'

HackerBooks
===========

FIRST RELEASE 0.1x CODENAME LUPIN ! By Ekianjo, 2013.
LICENSE: GPLv3 / http://opensource.org/licenses/GPL-3.0

Target hardware: Open Pandora GNU/Linux mini-computer handheld. 
However this application should work fine on all major GNU/Linux distros out there (Tested on OpenSUSE 12.2)
The latest versions now feature an expanded window size for desktop modes. 

## What is HackerBooks ? ##
This is a Python application to download many books related to Programming or Computer Sciences.
All the books proposed for download are freely available (either creative commons or permissive licenses, or copyrighted but made freely available by their authors).
Books are organized by titles, categories, authors, formats and years. Only PDF books are supported at this time, but this may change in the near future.

## How to run it ##
Extremely simple. Go into the terminal and just type : python main.py 
It should start without issue. If you face problems check the notes below regarding compatibility. 

## Usage ##
- Select a book in the list and click/Enter it
- You then see the description of the book in another window. You have the choice to close that window, or to download the book.
- If you choose to download the book, it will take a few moments depending on your connection until the book is received and copied.
- Once the book is available, you can click the "read" button to open it on your device for consultation.
- You can also choose to delete it from your device.
- The "special" menu give you an option to download all books at once, but be careful as it takes time and currently I did not integrate a specific way to stop it while it is running.

### Notes on Cross-Platform Compatibility ###
If you want to use this application, you need gtk 2+ and python 2.7+ on your system. 
Opening a PDF uses evince, therefore you should have it installed on your system for it to work. 
Needless to say, this is probably going to be working out of the box for GNU/Linux systems only. 
If you'd like to see more specific support for Windows/MAC OS please feel free to contribute to this project (or fork it).

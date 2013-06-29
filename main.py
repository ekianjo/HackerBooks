#encoding: utf-8
#!/usr/bin/python

#FIRST RELEASE 0.1 CODENAME LUPIN ! By Ekianjo, 2013. 
#LICENSE: GPLv3 / http://opensource.org/licenses/GPL-3.0


#----- SECOND RELEASE GOALS
#NEED TO ADD SYSTEM IDENTIFICATION
#NEED TO ADD SCROLLABLE WINDOW CONTAINER FOR THE TEXTVIEW. IF NOT CANNOT SEE ALL TEXT.
#ADD BOOK LICENSE INFORMATION
#ALLOW READING OF HTML at least (reader tbc)
#PROGRESS DOWNLOAD BAR
#ADD MORE BOOKS
#ALLOW USAGE OF XOURNAL TO OPEN PDFs
#SEND STATS TO SERVER
#ALLOW FAVORITES
#REPORT DOWNLOAD ERRORS TO SERVER

import gtk #for interface
import urllib, urllib2, os #os for file system operations, urllib for downloading
import subprocess #needed to launch separate application
import pango #used to determine a consistant style across 


hackerbooks = [('Pro Git', 'Git', 'Scott Chacon','pdf','https://github.s3.amazonaws.com/media/progit.en.pdf',
'''
Git is the version control system developed by Linus Torvalds for Linux kernel development. 
It took the open source world by storm since its inception in 2005, and is used by small development shops and giants like Google, Red Hat, and IBM, and of course many open source projects. 

A book by Git experts to turn you into a Git expert.

• Introduces the world of distributed version control
• Shows how to build a Git development workflow'''), 

('Think Complexity', 'General', 'Allen B. Downey','pdf','http://greenteapress.com/compmod/thinkcomplexity.pdf',
'''
This book is about complexity science, data structures and algorithms, intermediate programming in Python, and the philosophy of science:'''
),

    ('The Linux Command Line', 'Command Line', 'William E. Shotts Jr.','pdf','http://downloads.sourceforge.net/project/linuxcommand/TLCL/09.12/TLCL-09.12.pdf?r=http%3A%2F%2Flinuxcommand.org%2Ftlcl.php&ts=1372170077&use_mirror=jaist',
'''
You have experienced the shiny, point-and-click surface of your Linux computer—now dive below and explore its depths with the power of the command line.

The Linux Command Line takes you from your very first terminal keystrokes to writing full programs in Bash, the most popular Linux shell. Along the way you'll learn the timeless skills handed down by generations of gray-bearded, mouse-shunning gurus: file navigation, environment configuration, command chaining, pattern matching with regular expressions, and more.

In addition to that practical knowledge, author William Shotts reveals the philosophy behind these tools and the rich heritage that your desktop Linux machine has inherited from Unix supercomputers of yore.
'''        ),
('Clever Algorithms','Metaheuristics','Jason Browlee','pdf','http://www.lulu.com/shop/jason-brownlee/clever-algorithms-nature-inspired-programming-recipes/ebook/product-17386095.html','to insert here'),
('Think Stats','Statistics','Allen B. Downey','pdf','http://greenteapress.com/thinkstats/thinkstats.pdf'),
("Street-Fighting Mathematics",'Problem Solving','Sanjoy Mahajan','pdf','https://mitpress.mit.edu/sites/default/files/titles/content/9780262514293_Creative_Commons_Edition.pdf',
	'''
In problem solving, as in street fighting, rules are for fools: do whatever works—don't just stand there! Yet we often fear an unjustified leap even though it may land us on a correct result. Traditional mathematics teaching is largely about solving exactly stated problems exactly, yet life often hands us partly defined problems needing only moderately accurate solutions. This engaging book is an antidote to the rigor mortis brought on by too much mathematical rigor, teaching us how to guess answers without needing a proof or an exact calculation.

In Street-Fighting Mathematics, Sanjoy Mahajan builds, sharpens, and demonstrates tools for educated guessing and down-and-dirty, opportunistic problem solving across diverse fields of knowledge—from mathematics to management. Mahajan describes six tools: dimensional analysis, easy cases, lumping, picture proofs, successive approximation, and reasoning by analogy. Illustrating each tool with numerous examples, he carefully separates the tool—the general principle—from the particular application so that the reader can most easily grasp the tool itself to use on problems of particular interest.
'''),
('Algorithmic Game Theory','Game Theory','Noam Nisan and more','pdf','http://www.cambridge.org/journals/nisan/downloads/Nisan_Non-printable.pdf',
    '''
In the last few years game theory has had a substantial impact on computer science, especially on Internet- and e-commerce-related issues. More than 40 of the top researchers in this field have written chapters that go from the foundations to the state of the art. Basic chapters on algorithmic methods for equilibria, mechanism design and combinatorial auctions are followed by chapters on incentives and pricing, cost sharing, information markets and cryptography and security. Students, researchers and practitioners alike need to learn more about these fascinating theoretical developments and their widespread practical application.
'''),
('Think Python','Python','Allen B. Downey','pdf','http://greenteapress.com/thinkpython/thinkpython.pdf',
'''
The goal of this book is to teach you to think like a computer scientist. This way of thinking combines some of the best features of mathematics, engineering, and natural science. Like mathematicians, computer scientists use formal languages to denote ideas (speciﬁcally computations). 

Like engineers, they design things, assembling components into systems and evaluating tradeoffs among alternatives. Like scientists, they observe the behavior of complex systems, form hypotheses, and test predictions.'''),
('A Byte of Vim','Vim','Swaroop CH','pdf','http://files.swaroopch.com/vim/byte_of_vim_v051.pdf',
'''
“A Byte of Vim” is a book which aims to help you to learn how to use the Vim editor (version 7), even if all you know is how to use the computer keyboard.

The first part of this book is meant for new users who want to understand what Vim is and learn how to use it.

The second part of this book is for people who already know how to use Vim and want to learn about features that make Vim so powerful, such as windows and tabs, personal information management, making it a programmer’s editor, how to extend Vim with your own plugins, and more.
'''),
('Advanced Linux Programming','Linux','CodeSourcery', 'pdf','http://www.advancedlinuxprogramming.com/alp-folder/advanced-linux-programming.pdf',
'''
Advanced Linux Programming is intended for the programmer already familiar with the C programming language. Authors Alex Samuel, Jeffrey Oldham, and Mark Mitchell of CodeSourcery, LLC take a tutorial approach and teach the most important concepts and power features of the GNU/Linux system in application programs.

If you're a developer already experienced with programming for the GNU/Linux system, are experienced with another UNIX-like system and are interested in developing GNU/Linux software, or want to make the transition for a non-UNIX environment and are already familiar with the general principles of writing good software, this book is for you. In addition, you will find that this book is equally applicable to C and C++ programming. Even those progamming in other languages will find this book useful since the C language APIs and conventions are the lingua franca of GNU/Linux.
'''),
('Ruby Best Practices','Ruby','Gregory Brown','pdf','http://majesticseacreature.com/rbp-book/pdfs/rbp_1-0.pdf',
'''
In 1993, when Ruby was born, Ruby had nothing. No user base except for me and a few close friends. No tradition. No idioms except for a few inherited from Perl, though I regretted most of them afterward.

But the language forms the community. The community nourishes the culture. In the last decade, users increased—hundreds of thousands of programmers fell in love with Ruby. They put great effort into the language and its community. Projects were born. Idioms tailored for Ruby were invented and introduced. Ruby was influenced by Lisp and other functional programming languages. Ruby formed relationships between technologies and methodologies such as test-driven development and duck typing.

This book introduces a map of best practices of the language as of 2009. I’ve known Greg Brown for years, and he is an experienced Ruby developer who has contributed a lot of projects to the language, such as Ruport and Prawn. I am glad he compiled his knowledge into this book.

His insights will help you become a better Ruby programmer.'''),
('Introduction to Machine Learning','Machine Learning','Alex Smola','pdf','http://alex.smola.org/drafts/thebook.pdf',
'''
Over the past two decades Machine Learning has become one of the main-stays of information technology and with that, a rather central, albeit usually hidden, part of our life. With the ever increasing amounts of data becoming available there is good reason to believe that smart data analysis will become even more pervasive as a necessary ingredient for technological progress.'''),
('Dive Into Python 3','Python','Mark Pilgrim','pdf','https://github.com/downloads/diveintomark/diveintopython3/dive-into-python3.pdf',
	'''
Dive Into Python 3 covers Python 3 and its differences from Python 2. Compared to Dive Into Python, it’s about 20% revised and 80% new material.'''),
('Building Skills in Python','Python','Steven F. Lott','pdf','http://www.itmaybeahack.com/book/python-2.6/latex/BuildingSkillsinPython.pdf',
'''
How do you learn Python? By doing a series of exercises, each of which adds a single new feature of the language. This 450+ page book has 42 chapters that will help you build Python programming skills through a series of exercises. This book includes six projects from straight-forward to sophisticated that will help solidify your Python skills.

The 2.6 edition was significantly revised and expanded to cover Python 2.6 and some elements of Python 3.1. Many chapters have been updated, reorganized and added since the 2.5 edition.

The current release has benefitted from a great deal of support from readers who sent detailed lists of errors and suggestions. Professional programmers who need to learn Python are this book’s primary audience. We provide specific help for you in a number of ways.

Since Python is simple, we can address newbie programmers who don’t have deep experience in a number of other languages. We will call out some details in specific newbie sections. 
'''),
('How to Think Like A Computer Scientist','Python','Allen B. Downey (more)', 'pdf', 'http://www.ict.ru.ac.za/Resources/cspw/thinkcspy3/thinkcspy3.pdf',
'''
Despite Python’s appeal to many different communities, you may still wonder why Python? or why teach programming with Python? Answering these questions is no simple task—especially when popular opinion is on the side of more masochistic alternatives such as C++ and Java. However, I think the most direct answer is that programming in Python is simply a lot of fun and more productive.

One of the reasons why I like Python is that it provides a really nice balance between the practical and the conceptual. Since Python is interpreted, beginners can pick up the language and start doing neat things almost immediately without getting lost in the problems of compilation and linking. Furthermore, Python comes with a large library of modules that can be used to do all sorts of tasks ranging from web-programming to graphics. Having such a practical focus is a great way to engage students and it allows them to complete significant projects. However, Python can also serve as an excellent foundation for introducing important computer science concepts. Since Python fully supports procedures and classes, students can be gradually introduced to topics such as procedural abstraction, data structures, and object-oriented programming — all of which are applicable to later courses on Java or C++.
'''),
('Functional C','C','Pieter Hartel','pdf','http://eprints.eemcs.utwente.nl/1077/02/book.pdf',
'''
The Computer Science Departments of many universities teach a functional language as the first programming language. Using a functional language with its high level of abstraction helps to emphasize the principles of programming. Func-tional programming is only one of the paradigms with which a student should be acquainted. Imperative, Concurrent, Object-Oriented, and Logic programming are also important. Depending on the problem to be solved, one of the paradigms will be chosen as the most natural paradigm for that problem.
This book is the course material to teach a second paradigm: imperative programming, using C as the programming language. The book has been written so that it builds on the knowledge that the students have acquired during their rst course on functional programming, using SML. The prerequisite of this book is that the principles of programming are already understood; this book does not specically aim to teach `problem solving' or `programming'.'''),

('Mastering Node','NodeJS','TJ Holowaychuk','pdf','http://github.com/visionmedia/masteringnode/raw/master/book.pdf',
'''
Mastering node is an open source eBook by node hackers for node hackers. I started this as a side project and realized that I don't have time :) so go nuts, download it, build it, fork it, extend it and share it. If you come up with something you wish to contribute back, send me a pull request.'''),
('''Mobile Developer's Guide to the Galaxy''','Mobile Development', 'Robert Virkus (more)', 'pdf', 'http://www.enough.de/fileadmin/uploads/dev_guide_pdfs/Guide_12thEdition_WEB.pdf',
'''
The free, non-commercial book that provides an overview on the different mobile technologies and platforms for developers and decision-makers. Learn everything about how to create solutions for iOS, Android, BlackBerry, Java ME or Windows Phone.

More than 20 writers from the mobile community share their know-how, across more than 250 pages, in dealing with topics such as accessibility in mobile apps, LBS, mobile analytics, prototyping, cross-platform development, native development, mobile web and app marketing. This project was initiated in 2009 and we have since published a number of updated versions. As of today, we have distributed over 50,000 hardcopies. The 12th, and latest, edition was published in February 2013.''')
,('Getting Started with Open Source Development','Open Source','Rachna Kapur (more)','pdf','http://public.dhe.ibm.com/software/dw/db2/express-c/wiki/Getting_started_with_open_source_development_p2.pdf',
'''
Keeping your skills current in today's world is becoming increasingly challenging. There are too many new technologies being developed, and little time to learn them all. The DB2® on Campus Book Series has been developed to minimize the time and effort required to learn many of these new technologies.

Who should read this book?
This book is a good starting point for beginners to the open source world. It is specially written to equip students, and open source enthusiasts with the norms and best practices of open source. You should read this book if you want to:

• Educate yourself on the objectives of open source
• Understand open source software licensing requirements 
• Get an introduction to the norms followed in the open source world
• Join the open source movement and begin contributing. ''')
,('Programming from the Ground Up','Assembly','Jonathan Bartlett','pdf','http://ftp.twaren.net/Unix/NonGNU//pgubook/ProgrammingGroundUp-1-0-booksize.pdf',
'''
Most introductory books on programming frustrate me to no end. At the end of them you can still ask "how does the computer really work?" and not have a good answer. They tend to pass over topics that are difﬁcult even though they are important. I will take you through the difﬁcult issues because that is the only way to move on to masterful programming. 
My goal is to take you from knowing nothing about programming to understanding how to think, write, and learn like a programmer. You won’t know everything, but you will have a background for how everything ﬁts together. At the end of this book, you should be able to do the following:

• Understand how a program works and interacts with other programs
• Read other people’s programs and learn how they work
• Learn new programming languages quickly
• Learn advanced concepts in computer science quickly
'''),
('BashGuide','Bash','Lhunath','pdf','http://folk.ntnu.no/geirha/bashguide.pdf',
'''
This guide aims to aid people interested in learning to work with BASH1. It aspires to teach good practice techniques for using BASH, and writing simple scripts. This guide is targeted at beginning users. It assumes no advanced knowledge -- just the ability to login to a Unix-like system and open a command-line (terminal) interface. It will help if you know how to use a text editor; we will not be covering editors, nor do we endorse any particular editor choice.

Familiarity with the fundamental Unix tool set, or with other programming languages or programming concepts, is not required, but those who have such knowledge may understand some of the examples more quickly. If something is unclear to you, you are invited to report this (usehttp://mywiki.wooledge.org/BashGuideFeedback, or the #bash channel on irc.freenode.org) so that it may be clariﬁed in this document for future readers. You are invited to contribute to the development of this document by extending it or correcting invalid or incomplete information.'''),
('Essential C','C','Nick Parlante','pdf','http://cslibrary.stanford.edu/101/EssentialC.pdf',
'''
This Stanford CS Education document tries to summarize all the basic features of the C language. The coverage is pretty quick, so it is most appropriate as review or for someone with some programming background in another language. Topics include variables, int types, floating point types, promotion, truncation, operators, control structures (if, while, for), functions, value parameters, reference parameters, structs, pointers, arrays, the preprocessor, and the standard C library functions.''')
,('An Introduction to Programming in Emacs Lisp', 'Emacs', 'Robert J. Chassell','pdf','https://www.gnu.org/software/emacs/emacs-lisp-intro/emacs-lisp-intro.pdf',
'''
Most of the GNU Emacs integrated environment is written in the programming language called Emacs Lisp. The code written in this programming language is the software—the sets of instructions—that tell the computer what to do when you give it commands. Emacs is designed so that you can write new code in Emacs Lisp and easily install it as an extension to the editor. (GNU Emacs is sometimes called an “extensible editor”, but it does much more than provide editing capabilities. It is better to refer to Emacs as an “extensible computing environment”. However, that phrase is quite a mouthful. It is easier to refer to Emacs simply as an editor. Moreover, everything you do in Emacs—find the Mayan date and phases of the moon, simplify polynomials, debug code, manage files, read letters, write books—all these activities are kinds of editing in the most general sense of the word.)

Although Emacs Lisp is usually thought of in association only with Emacs, it is a full computer programming language. You can use Emacs Lisp as you would any other programming language. 
'''),
('The Not So Short Introduction to LaTeX','LaTeX','Tobias Oetiker (more)','pdf','http://tobi.oetiker.ch/lshort/lshort.pdf',
'''
LATEX is a typesetting system that is very suitable for producing scientiﬁc and mathematical documents of high typographical quality. It is also suitable for producing all sorts of other documents, from simple letters to complete books. LATEX uses TEX [2] as its formatting engine.

This short introduction describes LATEX 2ε and should be suﬃcient for most applications of LATEX. Refer to [1, 3] for a complete description of the LATEX system.'''),
('Modern Perl','Perl','Chromatic','pdf','http://www.onyxneon.com/books/modern_perl/modern_perl_a4.pdf',
'''
In 1987, Perl 1.0 changed the world. In the decades since then, the language has grown from a simple tool for system administration somewhere between shell scripting and C programming to a powerful, general purpose language steeped in a rich heritage.

Even so, most Perl 5 programs in the world take far too little advantage of the language. You can write Perl 5 programs as if they were Perl 4 programs (or Perl 3 or 2 or 1), but programs written to take advantage of everything amazing the worldwide Perl 5 community has invented, polished, and discovered are shorter, faster, more powerful, and easier to maintain than their alternatives. They solve difficult problems with speed and elegance. They take advantage of the CPAN and its unparalleled library of reusable code. They get things done.

This productivity can be yours, whether you've dabbled with Perl for a decade or someone just handed you this book and said "Fix this code by Friday." Modern Perl is suitable for programmers of every level. It's more than a Perl tutorial—only Modern Perl focuses on Perl 5.12 and 5.14, to demonstrate the latest and most effective time-saving features. Only Modern Perl explains how and why the language works, to let you unlock the full power of Perl. When you have to solve a problem now, reach for Perl. When you have to solve a problem right, reach for Modern Perl.''')

, ("Mining of Massive Datasets","Big Data","Anand Rajaraman (more)","pdf",'http://infolab.stanford.edu/~ullman/mmds/book.pdf',
	'''
At the highest level of description, this book is about data mining. However, it focuses on data mining of very large amounts of data, that is, data so large it does not fit in main memory. 
Because of the emphasis on size, many of our examples are about the Web or data derived from the Web. Further, the book takes an algorithmic point of view: data mining is about applying algorithms to data, rather than using data to "train" a machine-learning engine of some sort.''')
, ('How Computers Work','Computing','Roger Young','pdf','http://www.fastchip.net/howcomputerswork/bookbpdf.pdf',
	'''
Computers are the most complex machines that have ever been created. Very few people really know how they work. This book will tell you how they work and no technical knowledge is required. It explains the operation of a simple, but fully functional, computer in complete detail. The simple computer described consists mainly of a processor and main memory. Relays, which are explained, are used in the circuitry instead of transistors for simplicity. This book does not cover peripherals like modems, mice, disk drives, or monitors.

Did you ever wonder what a bit, a pixel, a latch, a word (of memory), a data bus, an address bus, a memory, a register, a processor, a timing diagram, a clock (of a processor), an instruction, or machine code is? Though most explanations of how computers work are a lot of analogies or require a background in electrical engineering, this book will tell you precisely what each of them is and how each of them works without requiring any previous knowledge of computers or electronics. 
''')

, ('How to Write Parallel Programs','Parallel Programming','Nicholas Carriero (more)','pdf','http://lindaspaces.com/book/book.pdf',
	'''
This book is the raw material for a hands-on, "workshop" type course for undergraduates or graduate students in parallel programming. It can also serves as the core of a more conventional course; and it might profitably be read (we hope and believe) by any professional or researcher who needs an up-to-date synthesis of this fast-growing, fast-changing and fast-maturing field.

The programming examples and exercises use C-Linda (Linda is a registered trademark of Scientific Computing Associates.); C-Linda running on a parallel machine or a network is the ideal lab environment for the workshop course we've described. A C-Linda simulator running on a standard workstation is an adequate environment. Relying on some other parallel language or programming system is perfectly okay as well. The called-for translations between the book and the lab environment might be slightly painful (particularly if the non-Linda parallel language you choose is any variant of the ubiquitous message-passing or remote-procedure-call models), but these translation exercises are always illuminating, and anyway, they build character.''')


    ]



#not used currently. Some additional work needed. 
class AlertWindow(gtk.Window):
	def __init__(self):
		super(AlertWindow,self).__init__()
		self.set_size_request(300,200)
		self.set_position(gtk.WIN_POS_CENTER)
		self.set_border_width(8)
		self.set_title("Information")

		self.table = gtk.Table(2, 2, True)
		info = gtk.Button("Information")
		info.connect("clicked", self.on_info)

		self.table.attach(info, 0, 1, 0, 1)
		self.add(self.table)

		self.show_all()

	def on_info(self,widget):
		md = gtk.MessageDialog(self, 
            gtk.DIALOG_DESTROY_WITH_PARENT, gtk.MESSAGE_INFO, 
            gtk.BUTTONS_CLOSE, "Download completed")
		md.run()
		md.destroy()

		


	def autrechose(self):
		pass

class InfoBooks(gtk.Window):
    def __init__(self):
        super(InfoBooks,self).__init__()

        #set info window size attributes
        self.set_size_request(600,400)
        self.set_position(gtk.WIN_POS_CENTER)
        self.set_border_width(8)
        self.set_title(mainwindow.caca+" : Book Information")

        #check if book was already downloaded or not
        if self.check_book_exists():
        	print "book exists"

        #connect the close window function
        self.connect("destroy",self.close_window)

        #layout of the contents
        table = gtk.Table(8, 4, False)
        table.set_col_spacings(10)
        
        #title of the text field
        #title = gtk.Label("Book Information")
        halign = gtk.Alignment(0, 0, 0, 0)
        #halign.add(title)
        table.attach(halign, 0, 1, 0, 1, gtk.FILL, gtk.FILL, 0, 0);

        #get information to put into the text field. Textbuffer is the object that goes in textview field.
        textbuffer = gtk.TextBuffer()
        #textbuffer.set_text(self.findbookinfo())
        
        #set properties for the textview object.
        wins = gtk.TextView(buffer=textbuffer)

        #sets pango text attributes to define some standard style at display that does not depend on the OS settings only.
        h_tag = textbuffer.create_tag( "h", size_points=16, weight=pango.WEIGHT_BOLD) 
        position = textbuffer.get_end_iter()
        textbuffer.insert_with_tags( position, "\n"+mainwindow.caca+"\n", h_tag) 
        position = textbuffer.get_end_iter()
        n_tag = textbuffer.create_tag( "n", size_points=8,weight=pango.WEIGHT_NORMAL) 
        textbuffer.insert_with_tags( position, self.findbookinfo(), n_tag) 

        wins.set_left_margin(20)
        wins.set_right_margin(20)
        
        wins.set_pixels_inside_wrap(3)

        wins.set_wrap_mode(gtk.WRAP_WORD)
        wins.set_editable(False)
        wins.modify_fg(gtk.STATE_NORMAL, gtk.gdk.Color(5140, 5140, 5140))
        wins.set_cursor_visible(False)
        table.attach(wins, 0, 2, 1, 3, gtk.FILL | gtk.EXPAND, gtk.FILL | gtk.EXPAND, 1, 1)

        #Download button attributes and connection
        
        self.download = gtk.Button("Download")
        if self.check_book_exists()==True:
			self.download.set_sensitive(False)
        self.download.set_size_request(50, 30)
        table.attach(self.download, 3, 4, 1, 2, gtk.FILL, gtk.SHRINK, 1, 1)
        self.download.connect_object("clicked", self.downloadbook, None)

        #Close button attributes and connection to signals
        valign = gtk.Alignment(0, 0, 0, 0)
        close = gtk.Button("Close")
        close.set_size_request(70, 30)
        valign.add(close)
        table.set_row_spacing(1, 3)
        table.attach(valign, 3, 4, 2, 3, gtk.FILL, gtk.FILL | gtk.EXPAND, 1, 1)
        close.connect_object("clicked", self.close_window, None)
        
        # "delete"
        #make sure this button only appears if the book is downloaded. 
        halign2 = gtk.Alignment(0, 1, 0, 0)
        self.delete = gtk.Button("Delete")
        if self.check_book_exists()==False:
			self.delete.set_sensitive(False)
        self.delete.set_size_request(70, 30)
        self.delete.connect_object("clicked", self.delete_book, None)
        halign2.add(self.delete)
        
        table.set_row_spacing(3, 6)
        table.attach(halign2, 0, 1, 4, 5, gtk.FILL, gtk.FILL, 0, 0)
        
        #read button attributes 
        self.readbtn = gtk.Button("Read")
        if self.check_book_exists()==False:
		    self.readbtn.set_sensitive(False)
        self.readbtn.set_size_request(70, 30)
        table.attach(self.readbtn, 3, 4, 4, 5, gtk.FILL, gtk.FILL, 0, 0);
        self.readbtn.connect_object("clicked", self.open_book, None)
        
        #add the finalized table layout to the window
        self.add(table)

        #display all
        self.show_all()

    def delete_book(self,widget):
    	filename=mainwindow.caca+".pdf"
    	try:
	    	os.remove(filename)
	    	print "book was deleted"
	    	md = gtk.MessageDialog(self, gtk.DIALOG_DESTROY_WITH_PARENT, gtk.MESSAGE_INFO, gtk.BUTTONS_CLOSE, "You just deleted the book.")
	    	md.run()
	    	md.destroy()
	    	self.readbtn.set_sensitive(False)
	    	self.download.set_sensitive(True)
	    	self.delete.set_sensitive(False)

    	except:
    		print "File was not deleted"

    	
	#check if book exists first

    def open_book(self, widget):
    	try:
    		#need to separate the arguments in an array to give arguments instead of a single command!!
	    	command=["evince", "{0}.pdf".format(mainwindow.caca)]
	    	print command
    		subprocess.Popen(command)
    		
        except:
			print "reading did not work"

    def check_internet(self):
		try:
			response=urllib2.urlopen('http://www.google.com',timeout=2)
			print "you are connected"
			return True

		except urllib2.URLError as err: 

			md = gtk.MessageDialog(self, gtk.DIALOG_DESTROY_WITH_PARENT, gtk.MESSAGE_INFO, gtk.BUTTONS_CLOSE, "You are Offline - Please Connect.")
			md.run()
			md.destroy()
			return False

    def close_window(self, widget):
        self.destroy()

    def findbookinfo(self):
        try:
	        for books in hackerbooks:
	            #returns the description of the book
	            if books[0]==mainwindow.caca: return books[5]
        except:
        	return ""

    def check_book_exists(self):
    	bookname = mainwindow.caca+".pdf"
    	if os.path.isfile(bookname):
    		return True
    	else:
    		return False

    def downloadbook(self,widget):
        #if os.getcwd().split('\\')[-1]!="BOOKS":
        #if not os.path.exists("BOOKS"):
        #    os.makedirs("BOOKS")
        #os.chdir("BOOKS")
            
        #try:
        #    os.mkdir("BOOKS")
        #except:
        #    os.chdir("BOOKS")
        
        if self.check_internet():
	        
	        for books in hackerbooks:
	            #select the right book that is to download
	            if books[0]==mainwindow.caca: 
	                print books[4]
	                try:
	                    #downloads the book and renames it to the full name and adds pdf extension
	                    #TODO: ADD PROGRESS BAR
	                    #TODO: ALLOW FOR HTML FILES AS WELL SINCE MANY BOOKS DONT HAVE PDF
	                    md = gtk.MessageDialog(self, gtk.DIALOG_DESTROY_WITH_PARENT, gtk.MESSAGE_INFO, gtk.BUTTONS_CLOSE, "Download Completed")
	                    
	                    urllib.urlretrieve(books[4],books[0]+".pdf")
	                    
	                    #print "Download finished"
	                    md.run()
	                    md.destroy()
	                    self.readbtn.set_sensitive(True)
	                    self.download.set_sensitive(False)
	                    self.delete.set_sensitive(True)
	                    #TODO: CONFIRM THE FILE IS DOWNLOADED AND CONFIRM SIZE.
	                    #TODO: CHANGE PROPERTIES SO THAT ONE CAN LAUNCH THE PDF TO READ OR THE HTML FILE, AND MAKE THE DOWNLOAD BUTTON GREY
	                except:
	                    print "Download did not work"
    	else:
    		print "you are offline"
    
class HackerBooks(gtk.Window): 
    def __init__(self):
        super(HackerBooks, self).__init__()
        
        self.create_directory()

        self.set_size_request(750, 400)
        self.set_position(gtk.WIN_POS_CENTER)
        
        self.connect("destroy", gtk.main_quit)
        self.set_title("Hacker Books")
        #self.caca="yooo"

        vbox = gtk.VBox(False, 8)
        
        #sw is a scrolled window
        sw = gtk.ScrolledWindow()
        sw.set_shadow_type(gtk.SHADOW_ETCHED_IN)
        sw.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
        
        vbox.pack_start(sw, True, True, 0)

        store = self.create_model()

        treeView = gtk.TreeView(store)
        treeView.connect("row-activated", self.on_activated)
        treeView.set_rules_hint(True)
        sw.add(treeView)

        self.create_columns(treeView)
        self.statusbar = gtk.Statusbar()
        
        vbox.pack_start(self.statusbar, False, False, 0)

        self.add(vbox)
        self.show_all()

    def create_directory(self):
    	if os.path.isdir("BOOKS")==False:
    		os.makedirs("BOOKS")

    	os.chdir("BOOKS")


    def create_model(self):
        store = gtk.ListStore(str, str, str, str)

        for books in hackerbooks:
            store.append([books[0], books[1], books[2],books[3]])

        return store

    def create_columns(self, treeView):
    
        #display Ttitle
        rendererText = gtk.CellRendererText()
        column = gtk.TreeViewColumn("Title", rendererText, text=0)
        column.set_sort_column_id(0)    
        treeView.append_column(column)
        
        #display topic
        rendererText = gtk.CellRendererText()
        column = gtk.TreeViewColumn("Subject", rendererText, text=1)
        column.set_sort_column_id(1)
        treeView.append_column(column)

        #display author
        rendererText = gtk.CellRendererText()
        column = gtk.TreeViewColumn("Author", rendererText, text=2)
        column.set_sort_column_id(2)
        treeView.append_column(column)

        #display format
        rendererText = gtk.CellRendererText()
        column = gtk.TreeViewColumn("Format", rendererText, text=3)
        column.set_sort_column_id(3)
        treeView.append_column(column)

    def on_activated(self, widget, row, col):
        
        model = widget.get_model()
        #text = model[row][0] + ", " + model[row][1] + ", " + model[row][2]
        #self.statusbar.push(0, text)
        
        #stores the info about the book selected
        mainwindow.caca=model[row][0]
        
        #print mainwindow.caca
        InfoBooks()



mainwindow=HackerBooks()
gtk.main()

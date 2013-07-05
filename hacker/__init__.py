#encoding: utf-8
#!/usr/bin/python

global hackerbooks

hackerbooks = [('Pro Git', 'Git', 'Scott Chacon','pdf','https://github.s3.amazonaws.com/media/progit.en.pdf',
'''
Git is the version control system developed by Linus Torvalds for Linux kernel development. 
It took the open source world by storm since its inception in 2005, and is used by small development shops and giants like Google, Red Hat, and IBM, and of course many open source projects. 

A book by Git experts to turn you into a Git expert.

• Introduces the world of distributed version control
• Shows how to build a Git development workflow''','2009'), 

('Think Complexity', 'General', 'Allen B. Downey','pdf','http://greenteapress.com/compmod/thinkcomplexity.pdf',
'''
This book is about complexity science, data structures and algorithms, intermediate programming in Python, and the philosophy of science:''','2012'
),

    ('The Linux Command Line', 'Command Line', 'William E. Shotts Jr.','pdf','http://downloads.sourceforge.net/project/linuxcommand/TLCL/09.12/TLCL-09.12.pdf?r=http%3A%2F%2Flinuxcommand.org%2Ftlcl.php&ts=1372170077&use_mirror=jaist',
'''
You have experienced the shiny, point-and-click surface of your Linux computer—now dive below and explore its depths with the power of the command line.

The Linux Command Line takes you from your very first terminal keystrokes to writing full programs in Bash, the most popular Linux shell. Along the way you'll learn the timeless skills handed down by generations of gray-bearded, mouse-shunning gurus: file navigation, environment configuration, command chaining, pattern matching with regular expressions, and more.

In addition to that practical knowledge, author William Shotts reveals the philosophy behind these tools and the rich heritage that your desktop Linux machine has inherited from Unix supercomputers of yore.
''','2009'),
('Think Stats','Statistics','Allen B. Downey','pdf','http://greenteapress.com/thinkstats/thinkstats.pdf',
'''
Think Stats: Probability and Statistics for Programmers is a textbook for a new kind of introductory prob-stat class. It emphasizes the use of statistics to explore large datasets. It takes a computational approach. 

The book lends itself to a project-based approach. In my class, students work on a semester-long project that requires them to pose a statistical question, find a dataset that can address it, and apply each of the techniques they learn to their own data.
''','2011'),
("Street-Fighting Mathematics",'Problem Solving','Sanjoy Mahajan','pdf','https://mitpress.mit.edu/sites/default/files/titles/content/9780262514293_Creative_Commons_Edition.pdf',
	'''
In problem solving, as in street fighting, rules are for fools: do whatever works—don't just stand there! Yet we often fear an unjustified leap even though it may land us on a correct result. Traditional mathematics teaching is largely about solving exactly stated problems exactly, yet life often hands us partly defined problems needing only moderately accurate solutions. This engaging book is an antidote to the rigor mortis brought on by too much mathematical rigor, teaching us how to guess answers without needing a proof or an exact calculation.

In Street-Fighting Mathematics, Sanjoy Mahajan builds, sharpens, and demonstrates tools for educated guessing and down-and-dirty, opportunistic problem solving across diverse fields of knowledge—from mathematics to management. Mahajan describes six tools: dimensional analysis, easy cases, lumping, picture proofs, successive approximation, and reasoning by analogy. Illustrating each tool with numerous examples, he carefully separates the tool—the general principle—from the particular application so that the reader can most easily grasp the tool itself to use on problems of particular interest.
''','2010'),
('Algorithmic Game Theory','Game Theory','Noam Nisan and more','pdf','http://www.cambridge.org/journals/nisan/downloads/Nisan_Non-printable.pdf',
    '''
In the last few years game theory has had a substantial impact on computer science, especially on Internet- and e-commerce-related issues. More than 40 of the top researchers in this field have written chapters that go from the foundations to the state of the art. Basic chapters on algorithmic methods for equilibria, mechanism design and combinatorial auctions are followed by chapters on incentives and pricing, cost sharing, information markets and cryptography and security. Students, researchers and practitioners alike need to learn more about these fascinating theoretical developments and their widespread practical application.
''','2007'),
('Think Python','Python','Allen B. Downey','pdf','http://greenteapress.com/thinkpython/thinkpython.pdf',
'''
The goal of this book is to teach you to think like a computer scientist. This way of thinking combines some of the best features of mathematics, engineering, and natural science. Like mathematicians, computer scientists use formal languages to denote ideas (speciﬁcally computations). 

Like engineers, they design things, assembling components into systems and evaluating tradeoffs among alternatives. Like scientists, they observe the behavior of complex systems, form hypotheses, and test predictions.''',
'2013'),
('A Byte of Vim','Vim','Swaroop CH','pdf','http://files.swaroopch.com/vim/byte_of_vim_v051.pdf',
'''
“A Byte of Vim” is a book which aims to help you to learn how to use the Vim editor (version 7), even if all you know is how to use the computer keyboard.

The first part of this book is meant for new users who want to understand what Vim is and learn how to use it.

The second part of this book is for people who already know how to use Vim and want to learn about features that make Vim so powerful, such as windows and tabs, personal information management, making it a programmer’s editor, how to extend Vim with your own plugins, and more.
''','2008'),
('Advanced Linux Programming','Linux','CodeSourcery', 'pdf','http://www.advancedlinuxprogramming.com/alp-folder/advanced-linux-programming.pdf',
'''
Advanced Linux Programming is intended for the programmer already familiar with the C programming language. Authors Alex Samuel, Jeffrey Oldham, and Mark Mitchell of CodeSourcery, LLC take a tutorial approach and teach the most important concepts and power features of the GNU/Linux system in application programs.

If you're a developer already experienced with programming for the GNU/Linux system, are experienced with another UNIX-like system and are interested in developing GNU/Linux software, or want to make the transition for a non-UNIX environment and are already familiar with the general principles of writing good software, this book is for you. In addition, you will find that this book is equally applicable to C and C++ programming. Even those progamming in other languages will find this book useful since the C language APIs and conventions are the lingua franca of GNU/Linux.
''','2001'),
('Ruby Best Practices','Ruby','Gregory Brown','pdf','http://majesticseacreature.com/rbp-book/pdfs/rbp_1-0.pdf',
'''
In 1993, when Ruby was born, Ruby had nothing. No user base except for me and a few close friends. No tradition. No idioms except for a few inherited from Perl, though I regretted most of them afterward.

But the language forms the community. The community nourishes the culture. In the last decade, users increased—hundreds of thousands of programmers fell in love with Ruby. They put great effort into the language and its community. Projects were born. Idioms tailored for Ruby were invented and introduced. Ruby was influenced by Lisp and other functional programming languages. Ruby formed relationships between technologies and methodologies such as test-driven development and duck typing.

This book introduces a map of best practices of the language as of 2009. I’ve known Greg Brown for years, and he is an experienced Ruby developer who has contributed a lot of projects to the language, such as Ruport and Prawn. I am glad he compiled his knowledge into this book.

His insights will help you become a better Ruby programmer.''','2009'),
('Introduction to Machine Learning','Machine Learning','Alex Smola','pdf','http://alex.smola.org/drafts/thebook.pdf',
'''
Over the past two decades Machine Learning has become one of the main-stays of information technology and with that, a rather central, albeit usually hidden, part of our life. With the ever increasing amounts of data becoming available there is good reason to believe that smart data analysis will become even more pervasive as a necessary ingredient for technological progress.''','2008'),
('Dive Into Python 3','Python','Mark Pilgrim','pdf','https://github.com/downloads/diveintomark/diveintopython3/dive-into-python3.pdf',
	'''
Dive Into Python 3 covers Python 3 and its differences from Python 2. Compared to Dive Into Python, it’s about 20% revised and 80% new material.''','2009'),
('Building Skills in Python','Python','Steven F. Lott','pdf','http://www.itmaybeahack.com/book/python-2.6/latex/BuildingSkillsinPython.pdf',
'''
How do you learn Python? By doing a series of exercises, each of which adds a single new feature of the language. This 450+ page book has 42 chapters that will help you build Python programming skills through a series of exercises. This book includes six projects from straight-forward to sophisticated that will help solidify your Python skills.

The 2.6 edition was significantly revised and expanded to cover Python 2.6 and some elements of Python 3.1. Many chapters have been updated, reorganized and added since the 2.5 edition.

The current release has benefitted from a great deal of support from readers who sent detailed lists of errors and suggestions. Professional programmers who need to learn Python are this book’s primary audience. We provide specific help for you in a number of ways.

Since Python is simple, we can address newbie programmers who don’t have deep experience in a number of other languages. We will call out some details in specific newbie sections. 
''','2010'),
('How to Think Like A Computer Scientist','Python','Allen B. Downey (more)', 'pdf', 'http://www.ict.ru.ac.za/Resources/cspw/thinkcspy3/thinkcspy3.pdf',
'''
Despite Python’s appeal to many different communities, you may still wonder why Python? or why teach programming with Python? Answering these questions is no simple task—especially when popular opinion is on the side of more masochistic alternatives such as C++ and Java. However, I think the most direct answer is that programming in Python is simply a lot of fun and more productive.

One of the reasons why I like Python is that it provides a really nice balance between the practical and the conceptual. Since Python is interpreted, beginners can pick up the language and start doing neat things almost immediately without getting lost in the problems of compilation and linking. Furthermore, Python comes with a large library of modules that can be used to do all sorts of tasks ranging from web-programming to graphics. Having such a practical focus is a great way to engage students and it allows them to complete significant projects. However, Python can also serve as an excellent foundation for introducing important computer science concepts. 
''','2012'),
('Functional C','C','Pieter Hartel','pdf','http://eprints.eemcs.utwente.nl/1077/02/book.pdf',
'''
The Computer Science Departments of many universities teach a functional language as the first programming language. Using a functional language with its high level of abstraction helps to emphasize the principles of programming. Func-tional programming is only one of the paradigms with which a student should be acquainted. Imperative, Concurrent, Object-Oriented, and Logic programming are also important. Depending on the problem to be solved, one of the paradigms will be chosen as the most natural paradigm for that problem.
This book is the course material to teach a second paradigm: imperative programming, using C as the programming language. The book has been written so that it builds on the knowledge that the students have acquired during their rst course on functional programming, using SML. The prerequisite of this book is that the principles of programming are already understood; this book does not specically aim to teach `problem solving' or `programming'.''',
'1999'),

('Mastering Node','NodeJS','TJ Holowaychuk','pdf','http://github.com/visionmedia/masteringnode/raw/master/book.pdf',
'''
Mastering node is an open source eBook by node hackers for node hackers. I started this as a side project and realized that I don't have time :) so go nuts, download it, build it, fork it, extend it and share it. If you come up with something you wish to contribute back, send me a pull request.''',
''),
('''Mobile Developer's Guide to the Galaxy''','Mobile Development', 'Robert Virkus (more)', 'pdf', 'http://www.enough.de/fileadmin/uploads/dev_guide_pdfs/Guide_12thEdition_WEB.pdf',
'''
The free, non-commercial book that provides an overview on the different mobile technologies and platforms for developers and decision-makers. Learn everything about how to create solutions for iOS, Android, BlackBerry, Java ME or Windows Phone.

More than 20 writers from the mobile community share their know-how, across more than 250 pages, in dealing with topics such as accessibility in mobile apps, LBS, mobile analytics, prototyping, cross-platform development, native development, mobile web and app marketing. This project was initiated in 2009 and we have since published a number of updated versions. As of today, we have distributed over 50,000 hardcopies. The 12th, and latest, edition was published in February 2013.''',
'2013')
,('Getting Started with Open Source Development','Open Source','Rachna Kapur (more)','pdf','http://public.dhe.ibm.com/software/dw/db2/express-c/wiki/Getting_started_with_open_source_development_p2.pdf',
'''
Keeping your skills current in today's world is becoming increasingly challenging. There are too many new technologies being developed, and little time to learn them all. The DB2® on Campus Book Series has been developed to minimize the time and effort required to learn many of these new technologies.

Who should read this book?
This book is a good starting point for beginners to the open source world. It is specially written to equip students, and open source enthusiasts with the norms and best practices of open source. You should read this book if you want to:

• Educate yourself on the objectives of open source
• Understand open source software licensing requirements 
• Get an introduction to the norms followed in the open source world
• Join the open source movement and begin contributing. ''',
'2010')
,('Programming from the Ground Up','Assembly','Jonathan Bartlett','pdf','http://ftp.twaren.net/Unix/NonGNU//pgubook/ProgrammingGroundUp-1-0-booksize.pdf',
'''
Most introductory books on programming frustrate me to no end. At the end of them you can still ask "how does the computer really work?" and not have a good answer. They tend to pass over topics that are difﬁcult even though they are important. I will take you through the difﬁcult issues because that is the only way to move on to masterful programming. 
My goal is to take you from knowing nothing about programming to understanding how to think, write, and learn like a programmer. You won’t know everything, but you will have a background for how everything ﬁts together. At the end of this book, you should be able to do the following:

• Understand how a program works and interacts with other programs
• Read other people’s programs and learn how they work
• Learn new programming languages quickly
• Learn advanced concepts in computer science quickly
''',
'2003'),
('BashGuide','Bash','Lhunath','pdf','http://folk.ntnu.no/geirha/bashguide.pdf',
'''
This guide aims to aid people interested in learning to work with BASH1. It aspires to teach good practice techniques for using BASH, and writing simple scripts. This guide is targeted at beginning users. It assumes no advanced knowledge -- just the ability to login to a Unix-like system and open a command-line (terminal) interface. It will help if you know how to use a text editor; we will not be covering editors, nor do we endorse any particular editor choice.

Familiarity with the fundamental Unix tool set, or with other programming languages or programming concepts, is not required, but those who have such knowledge may understand some of the examples more quickly. If something is unclear to you, you are invited to report this (usehttp://mywiki.wooledge.org/BashGuideFeedback, or the #bash channel on irc.freenode.org) so that it may be clariﬁed in this document for future readers. You are invited to contribute to the development of this document by extending it or correcting invalid or incomplete information.''',
'2013'),
('Essential C','C','Nick Parlante','pdf','http://cslibrary.stanford.edu/101/EssentialC.pdf',
'''
This Stanford CS Education document tries to summarize all the basic features of the C language. The coverage is pretty quick, so it is most appropriate as review or for someone with some programming background in another language. Topics include variables, int types, floating point types, promotion, truncation, operators, control structures (if, while, for), functions, value parameters, reference parameters, structs, pointers, arrays, the preprocessor, and the standard C library functions.''',
'2003')
,('An Introduction to Programming in Emacs Lisp', 'Emacs', 'Robert J. Chassell','pdf','https://www.gnu.org/software/emacs/emacs-lisp-intro/emacs-lisp-intro.pdf',
'''
Most of the GNU Emacs integrated environment is written in the programming language called Emacs Lisp. The code written in this programming language is the software—the sets of instructions—that tell the computer what to do when you give it commands. Emacs is designed so that you can write new code in Emacs Lisp and easily install it as an extension to the editor. (GNU Emacs is sometimes called an “extensible editor”, but it does much more than provide editing capabilities. It is better to refer to Emacs as an “extensible computing environment”. However, that phrase is quite a mouthful. It is easier to refer to Emacs simply as an editor. Moreover, everything you do in Emacs—find the Mayan date and phases of the moon, simplify polynomials, debug code, manage files, read letters, write books—all these activities are kinds of editing in the most general sense of the word.)

Although Emacs Lisp is usually thought of in association only with Emacs, it is a full computer programming language. You can use Emacs Lisp as you would any other programming language. 
''',
'2009'),
('The Not So Short Introduction to LaTeX','LaTeX','Tobias Oetiker (more)','pdf','http://tobi.oetiker.ch/lshort/lshort.pdf',
'''
LATEX is a typesetting system that is very suitable for producing scientiﬁc and mathematical documents of high typographical quality. It is also suitable for producing all sorts of other documents, from simple letters to complete books. LATEX uses TEX [2] as its formatting engine.

This short introduction describes LATEX 2ε and should be suﬃcient for most applications of LATEX. Refer to [1, 3] for a complete description of the LATEX system.''',
'2011'),
('Modern Perl','Perl','Chromatic','pdf','http://www.onyxneon.com/books/modern_perl/modern_perl_a4.pdf',
'''
In 1987, Perl 1.0 changed the world. In the decades since then, the language has grown from a simple tool for system administration somewhere between shell scripting and C programming to a powerful, general purpose language steeped in a rich heritage.

Even so, most Perl 5 programs in the world take far too little advantage of the language. You can write Perl 5 programs as if they were Perl 4 programs (or Perl 3 or 2 or 1), but programs written to take advantage of everything amazing the worldwide Perl 5 community has invented, polished, and discovered are shorter, faster, more powerful, and easier to maintain than their alternatives. They solve difficult problems with speed and elegance. They take advantage of the CPAN and its unparalleled library of reusable code. They get things done.

This productivity can be yours, whether you've dabbled with Perl for a decade or someone just handed you this book and said "Fix this code by Friday." Modern Perl is suitable for programmers of every level. It's more than a Perl tutorial—only Modern Perl focuses on Perl 5.12 and 5.14, to demonstrate the latest and most effective time-saving features. Only Modern Perl explains how and why the language works, to let you unlock the full power of Perl. When you have to solve a problem now, reach for Perl. When you have to solve a problem right, reach for Modern Perl.''',
'2012')

, ("Mining of Massive Datasets","Big Data","Anand Rajaraman (more)","pdf",'http://infolab.stanford.edu/~ullman/mmds/book.pdf',
	'''
At the highest level of description, this book is about data mining. However, it focuses on data mining of very large amounts of data, that is, data so large it does not fit in main memory. 

Because of the emphasis on size, many of our examples are about the Web or data derived from the Web. Further, the book takes an algorithmic point of view: data mining is about applying algorithms to data, rather than using data to "train" a machine-learning engine of some sort.''',
'2013')
, ('How Computers Work','Computing','Roger Young','pdf','http://www.fastchip.net/howcomputerswork/bookbpdf.pdf',
	'''
Computers are the most complex machines that have ever been created. Very few people really know how they work. This book will tell you how they work and no technical knowledge is required. It explains the operation of a simple, but fully functional, computer in complete detail. The simple computer described consists mainly of a processor and main memory. Relays, which are explained, are used in the circuitry instead of transistors for simplicity. This book does not cover peripherals like modems, mice, disk drives, or monitors.

Did you ever wonder what a bit, a pixel, a latch, a word (of memory), a data bus, an address bus, a memory, a register, a processor, a timing diagram, a clock (of a processor), an instruction, or machine code is? Though most explanations of how computers work are a lot of analogies or require a background in electrical engineering, this book will tell you precisely what each of them is and how each of them works without requiring any previous knowledge of computers or electronics. 
''',
'2002')

, ('How to Write Parallel Programs','Parallel Programming','Nicholas Carriero (more)','pdf','http://lindaspaces.com/book/book.pdf',
	'''
This book is the raw material for a hands-on, "workshop" type course for undergraduates or graduate students in parallel programming. It can also serves as the core of a more conventional course; and it might profitably be read (we hope and believe) by any professional or researcher who needs an up-to-date synthesis of this fast-growing, fast-changing and fast-maturing field.

The programming examples and exercises use C-Linda (Linda is a registered trademark of Scientific Computing Associates.); C-Linda running on a parallel machine or a network is the ideal lab environment for the workshop course we've described. A C-Linda simulator running on a standard workstation is an adequate environment. Relying on some other parallel language or programming system is perfectly okay as well. The called-for translations between the book and the lab environment might be slightly painful (particularly if the non-Linda parallel language you choose is any variant of the ubiquitous message-passing or remote-procedure-call models), but these translation exercises are always illuminating, and anyway, they build character.''',
'1992')
,('Beautiful Code, Compelling Evidence','Haskell','Jeff Heard','pdf','http://vis.renci.org/jeff/wp-content/uploads/2009/01/beautifulcode.pdf',
'''
This is a tutorial I presented at ICFP last year on visualization and graphics in Haskell.  
It talks at length about why functional programming is a good idea for graphics, and then presents the basic tools that exist today.
''',
'2008'),
('Version Control by Example','Version Control','Eric Sink','pdf','http://www.ericsink.com/vcbe/vcbe_a4_lo.pdf',
'''
This book uses practical examples to explain version control with both centralized and decentralized systems.  Topics covered include:

• Basic version control commands and concepts
• Introduction to Distributed Version Control Systems (DVCS)
• Advanced branching workflows
• Strengths and weaknesses of DVCS vs. centralized tools
• Best practices
• How distributed version control works under the hood

Featuring these open source version control tools:

• Apache Subversion
• Mercurial
• Git
• Veracity

''',
'2011'),
('Learning Statistics with R','R','Daniel Navarro','pdf','http://health.adelaide.edu.au/psychology/ccs/docs/lsr/lsr-0.3.pdf',
'''
Since 2011 I (Dan) have been teaching an introductory statistics class for psychology students, using the R statistical package as the primary tool. 
Because I was a little unhappy with the textbooks available at the time, I started writing my own. The book is still a work in progress, but it has reached a "first draft" stage, at 542 pages. 
''',
'2013')

,('Smooth CoffeeScript','CoffeeScript','E. Hoigaard','pdf','http://autotelicum.github.io/Smooth-CoffeeScript/Smooth%20CoffeeScript%20Web%20Optimized.pdf',
'''
Smooth CoffeeScript is a book about CoffeeScript and programming. Start with programming fundamentals, learn about functional programming with Underscore and problem solving, study object orientation and modularity. It covers client/server web apps with Canvas and WebSockets.

No previous programming knowledge is required. CoffeeScript lets you write web oriented applications simply and elegantly. It is closely related to JavaScript but without its quirky corners. 
''','2011'),
('Text Algorithms','Text Processing','Maxime Crochemore','pdf','http://igm.univ-mlv.fr/~mac/REC/text-algorithms.pdf',
'''
One of the simplest and natural types of information representation is by means of written texts. Data to be processed often does not decompose into independent records. This type of data is characterized by the fact that it can be written down as a long sequence of characters. Such linear sequence is called a text. The texts are central in "word processing" systems, which provide facilities for the manipulation of texts. Such systems usually process objects which are quite large. For example, this book contains probably more than a million characters. Text algorithms occur in many areas of science and information processing. Many text editors and programming languages have facilities for processing texts. In biology, text algorithms arise in the study of molecular sequences. The complexity of text algorithms is also one of the central and most studied problems in theoretical computer science. It could be said that it is the domain where the practice and theory are very close together.

'''	,'1997'),
('Producing Open Source Software','Open Source','Karl Fogel','pdf','http://producingoss.com/en/producingoss.pdf',
'''
At parties, people no longer give me a blank stare when I tell them I write free software. "Oh, yes, open source—like Linux?" they say. I nod eagerly in agreement. "Yes, exactly! That's what I do." It's nice not to be completely fringe anymore. In the past, the next question was usually fairly predictable: "How do you make money doing that?" To answer, I'd summarize the economics of open source: that there are organizations in whose interest it is to have certain software exist, but that they don't need to sell copies, they just want to make sure the software is available and maintained, as a tool instead of a commodity.

Lately, however, the next question has not always been about money. The business case for open source software is no longer so mysterious, and many non-programmers already understand—or at least are not surprised—that there are people employed at it full time. Instead, the question I have been hearing more and more often is "Oh, how does that work?"

I didn't have a satisfactory answer ready, and the harder I tried to come up with one, the more I realized how complex a topic it really is. Running a free software project is not exactly like running a business (imagine having to constantly negotiate the nature of your product with a group of volunteers, most of whom you've never met!). Nor, for various reasons, is it exactly like running a traditional non-profit organization, nor a government. 
'''	,'2013'),
('Making Games with Python & Pygame','Python / Pygame', 'Al Sweigart','pdf','http://inventwithpython.com/makinggames.pdf',
'''
“Making Games with Python & Pygame” covers the Pygame library with the source code for 11 games. “Making Games” was written as a sequel for the same age range as “Invent with Python”. Once you have an understanding of the basics of Python programming, you can now expand your abilities using the Pygame library to make games with graphics, animation, and sound.

The book features the source code to 11 games. The games are clones of classics such as Nibbles, Tetris, Simon, Bejeweled, Othello, Connect Four, Flood It, and others.
''','2012'),
('''Beej's Guide to C Programming''','C','''Brian 'Beej' Hall''','pdf','http://beej.us/guide/bgc/output/print/bgc_A4.pdf',
'''
The bad news is that if you're a beginner in this whole thing, all C code you see looks obfuscated! The good news is, it's not going to be that way for long.
What we'll try to do over the course of this guide is lead you from complete and utter sheer lost confusion on to the sort of enlightened bliss that can only be obtained though pure C programming. Right on.

As with most Beej's Guides, this one tries to cater to people who are just starting on the topic. That's you! If that's not you for whatever reason the best I can hope to provide is some pastey entertainment for your reading pleasure. The only thing I can reasonably promise is that this guide won't end on a cliffhanger...or will it?

'''
,'2007' ),
('The New C Standard','C','Derek M. Jones','pdf','http://www.coding-guidelines.com/cbook/cbook1_2.pdf',
'''
This book contains a detailed analysis of the International Standard for the C language, excluding the library from a number of perspectives. The organization of the material is unusual in that it is based on the actual text of the published C Standard. The unit of discussion is the individual sentences from the C
Standard (2043 of them). 

Readers are assumed to have more than a passing familiarity with C.

''',
'2009'),
('Think Bayes','Bayesian Statistics','Allen B. Downey','pdf','http://www.greenteapress.com/thinkbayes/thinkbayes.pdf',
'''
Think Bayes is an introduction to Bayesian statistics using computational methods. This version of the book is a rough draft. I am making this draft available for comments, but it comes with the warning that it is probably full of errors. 
''','2012'	),
('Free Software, Free Society','Freedom','Richard Stallman','pdf','http://www.gnu.org/doc/fsfs-ii-2.pdf',
'''
This book collects the writing of Richard Stallman in a manner that will make its subtlety and power clear. The essays span a wide range, from copyright to the history of the free software movement. They include many arguments not well known, and among these, an especially insightful account of the changed circumstances that render copyright in the digital world suspect. They will serve as a resource for those who seek to understand the thought of this most powerful man--powerful in his ideas, his passion, and his integrity, even if powerless in every other way. They will inspire other who would take these ideas, and build upon them.
''','2010'),
('The Future of Ideas','Internet','Lawrence Lessig','pdf','http://web.archive.org/web/20110716220221/http://www.the-future-of-ideas.com/download/lessig_FOI.pdf',
'''
The Internet revolution has come. Some say it has gone. What was responsible for its birth? Who is responsible for its demise? In The Future of Ideas, Lawrence Lessig explains how the Internet revolution has produced a counterrevolution of devastating power and effect. The explosion of innovation we have seen in the environment of the Internet was not conjured from some new, previously unimagined technological magic; instead, it came from an ideal as old as the nation. Creativity flourished there because the Internet protected an innovation commons. The Internet's very design built a neutral platform upon which the widest range of creators could experiment. The legal architecture surrounding it protected this free space so that culture and information, the ideas of our era, could flow freely and inspire an unprecedented breadth of expression. But this structural design is changing, both legally and technically.

This shift will destroy the opportunities for creativity and innovation that the Internet originally engendered. ''',
'2001'),
('Learning Go','Go','Miek Gieben','pdf','http://www.miek.nl/files/go/20130612-go.pdf',
'''
This is an introduction to the Go language from Google. Its aim is to provide a guide to this new and innovative language.

The intended audience of this book is people who are familiar with programming and know some programming languages, be it C[3], C++[23], Perl[5], Java[16], Erlang[4], Scala[17] or Haskell[1]. This is not a book that teaches you how to program, this is a book that just teaches you how to use Go.

As with learning new things, probably the best way to do this is to discover it for yourself by creating your own programs. Each chapter therefore includes a number of exercises (and answers) to acquaint you with the language.
''',
'2012'),
('Data Structures & Algorithms Analysis in C++','C++','Clifford A. Schaffer','pdf','http://people.cs.vt.edu/~shaffer/Book/C++3e20130328.pdf',
'''
We study data structures so that we can learn to write more efficient programs. But why must programs be efficient when new computers are faster every year?
The reason is that our ambitions grow with our capabilities. Instead of rendering efficiency needs obsolete, the modern revolution in computing power and storage capability merely raises the efficiency stakes as we attempt more complex tasks. The quest for program efficiency need not and should not conflict with sound design and clear coding. Creating efficient programs has little to do with “program-ming tricks” but rather is based on good organization of information and good algorithms. A programmer who has not mastered the basic principles of clear design is not likely to write efficient programs. Conversely, concerns related to develop-
ment costs and maintainability should not be used as an excuse to justify inefficient performance. Generality in design can and should be achieved without sacrificing performance, but this can only be done if the designer understands how to measure performance and does so as an integral part of the design and implementation process. 

''',
'2013'),
('Data Structures & Algorithms Analysis in Java','Java','Clifford A. Schaffer','pdf','http://people.cs.vt.edu/~shaffer/Book/JAVA3e20130328.pdf',
'''
We study data structures so that we can learn to write more efficient programs. But why must programs be efficient when new computers are faster every year?
The reason is that our ambitions grow with our capabilities. Instead of rendering efficiency needs obsolete, the modern revolution in computing power and storage capability merely raises the efficiency stakes as we attempt more complex tasks. The quest for program efficiency need not and should not conflict with sound design and clear coding. Creating efficient programs has little to do with “program-ming tricks” but rather is based on good organization of information and good algorithms. A programmer who has not mastered the basic principles of clear design is not likely to write efficient programs. Conversely, concerns related to develop-
ment costs and maintainability should not be used as an excuse to justify inefficient performance. Generality in design can and should be achieved without sacrificing performance, but this can only be done if the designer understands how to measure performance and does so as an integral part of the design and implementation process.
''',
'2013'),
('Big Fat Rails','Ruby on Rails','Mitch Guthrie','pdf','http://www.bigfatrails.com/ebooks/bigfatrails-0.7.4.beta.pdf',
'''
There are many resources out there for learning Rails. I've used many myself. The reason to add one more to an already long list may seem needless at best and stupid at worst. The driving factor is simply this: The more resources available to the beginner the better chance they have to become proficient at the subject.

When I'm learning something new I always find several resources to learn from. Often buying many books on the subject. Each resource provides a different point of view, teaching method, or simply a format which I learn better from. It is my intention to provide another resource that may help others better understand everything available to them. 
''',
'2012'	),
('An Introduction to R','R','W.N. Venables (more)','pdf','http://cran.r-project.org/doc/manuals/R-intro.pdf',
'''
This introduction to R is derived from an original set of notes describing the S and SPlus environments written in 1990–2 by Bill Venables and David M. Smith when at the University of Adelaide.
''',
'2013'),
('Version Control with Subversion','Subversion','Ben Collins-Sussman (more)','pdf','http://svnbook.red-bean.com/en/1.7/svn-book.pdf',
'''
In the world of open source software, the Concurrent Versions System (CVS) was the tool of choice for version control for many years. And rightly so. CVS was open source software itself, and its nonrestrictive modus operandi and support for networked operation allowed dozens of geographically dispersed programmers to share their work. It fit the collaborative nature of the open source world very well. CVS and its semi-chaotic development model have since become cornerstones of open source culture.

But CVS was not without its flaws, and simply fixing those flaws promised to be an enormous effort. Enter Subversion. Subversion was designed to be a successor to CVS, and its originators set out to win the hearts of CVS users in two ways—by creating an open source system with a design (and “look and feel”) similar to CVS, and by attempting to avoid most of CVS's noticeable flaws. While the result wasn't—and isn't—the next great evolution in version control design, Subversion is very powerful, very usable, and very flexible.
''','2011'
	),
('Introduction to Good Usability','Usability','Peter Conradie','pdf','http://www.peterpixel.nl/projects/ebook/introduction_to_good_usability.pdf',
'''
Over the past year I have written a few posts about design guidelines. They have also proven to be the most successful ones. I have therefor decided to put a few of them together, add some more and bundle it as an ebook. So without much further ado, I present:

''','2008'),
('Using R for Data Analysis and Graphics','R','J.H. Maindonald','pdf','http://cran.r-project.org/doc/contrib/usingR.pdf',
'''
These notes are designed to allow individuals who have a basic grounding in statistical methodology to work through examples that demonstrate the use of R for a range of types of data manipulation, graphical presentation and statistical analysis. Books that provide a more extended commentary on the methods illustrated in these examples include Maindonald and Braun (2003).

''','2008'),
('Programming Computer Vision with Python','Computer Vision','Jan Erik Solem','pdf','http://programmingcomputervision.com/downloads/ProgrammingComputerVision_CCdraft.pdf',
'''
Today, images and video are everywhere. Online photo sharing sites and social networks have them in the billions. Search engines will produce images of just about any conceivable query. Practically all phones and computers come with built in cameras. It is not uncommon for people to have many gigabytes of photos and videos on their devices.
Programming a computer and designing algorithms for understanding what is in these images is the field of computer vision. Computer vision powers applications like image search, robot navigation, medical image analysis, photo management and many more.

The idea behind this book is to give an easily accessible entry point to hands-on computer vision with enough understanding of the underlying theory and algorithms to be a foundation for students, researchers and enthusiasts. The Python programming language, the language choice of this book, comes with many freely available powerful modules for handling images, mathematical computing and data mining.
''',
'2012'),
('Markdown Cheat Sheet','MarkDown','Mark Boszko','pdf','http://stationinthemetro.com/storage/dev/Markdown_Cheat_Sheet_v1-1.pdf',
'''
This is a cheat sheet to cover most of the markups used in the Markdown markup language. 
It is now widely used in several blog management systems, and readme files on github, for example. 
''',''),
('Algorithms Course Material','Algorithms','Jeff Erikson','pdf','http://compgeom.cs.uiuc.edu/~jeffe/teaching/algorithms/everything.pdf',
'''
This page contains all my lecture notes for the algorithms classes required for all computer science undergraduate and graduate students at the University of Illinois, Urbana-Champaign. I have taught incarnations of this course eight times: Spring 1999, Fall 2000, Spring 2001, Fall 2002, Spring 2004, Fall 2005, Fall 2006, Spring 2007, Fall 2008, Spring 2009, Spring 2010, and Fall 2010. These notes are numbered roughly in the order I use them in my undergraduate class.
This PDF file is 814 pages long.''','2011'),
('Coding Freedom','Freedom','Gabriella Coleman','pdf','http://gabriellacoleman.org/Coleman-Coding-Freedom.pdf','''
Who are computer hackers? What is free software? And what does the emergence of a community dedicated to the production of free and open source software–and to hacking as a technical, aesthetic, and moral project–reveal about the values of contemporary liberalism? Exploring the rise and political significance of the free and open source software (F/OSS) movement in the United States and Europe, Coding Freedom details the ethics behind hackers’ devotion to F/OSS, the social codes that guide its production, and the political struggles through which hackers question the scope and direction of copyright and patent law. In telling the story of the F/OSS movement, the book unfolds a broader narrative involving computing, the politics of access, and intellectual property.

E. Gabriella Coleman tracks the ways in which hackers collaborate and examines passionate manifestos, hacker humor, free software project governance, and festive hacker conferences. ''',
'2013'),
('Free as in Freedom','Freedom','Sam Williams','pdf','http://static.fsf.org/nosvn/faif-2.0.pdf',
'''
In 2002, Sam Williams wrote Free as in Freedom, a biography of Richard M. Stallman. In its epilogue, Williams expressed hope that choosing to distribute his book under the GNU Free Documentation License would enable and encourage others to share corrections and their own perspectives through modifications to his work.

Free as in Freedom (2.0) is Stallman’s revision of the original biography. While preserving Williams’s viewpoint, it includes factual corrections and extensive new commentary by Stallman, as well as new prefaces by both authors written for the occasion. It is a rare kind of biography, where the reader has the benefit of both the biographer’s original words and the subject’s response.
''','2010'),
('''Don't just roll the dice''','Software Pricing','Neil Davidson','pdf','http://neilgd.wpengine.com/wp-content/uploads/2011/12/dontjustrollthedice.pdf','''
How do you price your software? Is it art, science or magic? How much attention should you pay to your competitors? This short handbook will provide you with the theory, practical advice and case studies you need to stop yourself from reaching for the dice.

At Business of Software 2007 Michael Pryor held an impromptu session on how to price your software. So many people turned up, and so many people kept on arriving, that by the time they’d introduced themselves there was no time left to talk about software pricing. I’ve had similar experiences; in fact, “How do I price my software?” is probably the most common question I’m asked by software entrepreneurs and product managers. This handbook is an attempt to answer that question.” Neil Davidson, Author. About the Author Neil Davidson is co-founder and joint CEO of Red Gate Software. Red Gate was founded in 1999 and now employs some 150 people. It was Cambridge News business of the year in 2006 and has been in the Sunday Times top 100 companies to work for three years running. It was founded with no VC money and little debt. Neil is also founder of the annual Business of Software conference and runs the Business of Software social network. ''',
'2011'),
('Introduction to Embedded Systems','Embedded Systems','Edward Ashford Lee (more)','pdf','http://leeseshia.org/releases/LeeSeshia_DigitalV1_08.pdf',
'''
This book is intended for students at the advanced undergraduate level or the introductory graduate level, and for practicing engineers and computer scientists who wish to understand the engineering principles of embedded systems. 

This book strives to identify and introduce the durable intellectual ideas of embedded systems as a technology and as a subject of study. The emphasis is on modeling, design, and analysis of cyber-physical systems, which integrate computing, networking, and physical processes. This book is divided into three major parts, focused on modeling, design, and analysis.
''',
'2011'),
('Linux Kernel Crash Book','Linux','Igor Ljubuncic','pdf','https://www.dropbox.com/s/ktbz9fy7qbwsyfa/www.dedoimedo.com-crash-book.pdf','''
“Linux Kernel Crash Book”, by Igor Ljubuncic, starts with crash tools via collection all the way to analysis, plus some extras and general tips. Linux kernel crash analysis is not an everyday topic. It is very likely a niche topic, which will interest only system administrators and professionals dabbling in the kernel. 

This condition may stop you from reading the book, as you may not be either the person maintaining server boxes nor the code developer trying to debug his drivers.

However, you may also consider this book as a very extensive learning lesson in what goes behind the curtains of a typical Linux system. While you may not find immediate use to the contents presented in this book, the general knowledge and problem solving methods and tools you find here should serve you universally. Come the day, come the opportunity, you will find this book of value.
	''',''),
('The R Inferno',"R",'Patrick Burns','pdf','http://www.burns-stat.com/pages/Tutor/R_inferno.pdf',
'''
An essential guide to the trouble spots and oddities of R. In spite of the quirks exposed here, R is the best computing environment for most data analysis tasks. R is free, open-source, and has thousands of contributed packages. It is used in such diverse fields as ecology, finance, genomics and music. If you are using spreadsheets to understand data, switch to R. You will have safer – and ultimately, more convenient – computations.
''','2011'),
('An Introduction to Programming in Go', 'Go','Caleb Doxsey','pdf','http://www.golang-book.com/assets/pdf/gobook.pdf',
'''
This book is a short, concise introduction to computer programming using the language Go. Designed by Google, Go is a general purpose programming language with modern features, clean syntax and a robust well-documented common library, making it an ideal language to learn as your first programming language.
''','2012'
	),
('Git Magic','Git','Ben Lynn','pdf','http://www-cs-students.stanford.edu/~blynn/gitmagic/book.pdf',
'''
As Arthur C. Clarke observed, any sufficiently advanced technology is indistinguishable from magic. This is a great way to approach Git: newbies can ignore its inner workings and view Git as a gizmo that can amaze friends and infuriate enemies with its wondrous abilities. Rather than go into details, we provide rough instructions for particular effects. After repeated use, gradually you will understand how each trick works, and how to tailor the recipes for your needs. 
''',
'2007'),
("Harry Potter and the Methods of Rationality",'Rationality','Eliezer Yudkowsky','pdf','http://hpmor.com/wordpress/wp-content/uploads/2012/03/Harry-Potter-and-the-Methods-of-Rationality.pdf',
'''
Harry Potter fanfic-in-progress, Harry Potter and the Methods of Rationality.
''','2013'
),
('TeX for the Impatient','TeX','Paul Abrahams (more)','pdf','http://mirror.ctan.org/info/impatient/book.pdf',
'''
TEX, a software system created by Donald E. Knuth, sets the standard for typesetting in mathematics, science, and engineering. “TEX for the Impatient” is a handbook that arose from the need to help technical writers learn TEX more quickly and once having learned it, to find fast answers to common questions. Clear, concise, and accessible, this book is organized for easy retrieval of information, thoroughly indexed, and carefully designed for learning by example.

TEX for the Impatient is intended to serve scientists, mathematicians, and technical typists for whom TEX is a useful tool rather than a primary interest, as well as computer people who have a strong interest in TEX for its own sake. We also intend it to serve both newcomers to TEX and those who are already familiar with TEX. We assume that our readers are comfortable working with computers and that they want to get the information they need as quickly as possible. Our aim is to provide that information clearly, concisely, and accessibly. This book therefore provides a bright searchlight, a stout walking-stick, and detailed maps for exploring and using TEX.''',
'2003'),
('Data-Intensive Text Processing with MapReduce','MapReduce','Jimmy Lin (more)','pdf','http://www.umiacs.umd.edu/~jimmylin/MapReduce-book-final.pdf',
'''
MapReduce [45] is a programming model for expressing distributed computations on massive amounts of data and an execution framework for large-scale data processing on clusters of commodity servers. It was originally developed by Google and built on well-known principles in parallel and distributed processing dating back several decades. MapReduce has since enjoyed widespread adoption via an open-source implementation called Hadoop, whose development was led by Yahoo (now an Apache project). Today, a vibrant software ecosystem has sprung up around Hadoop, with significant activity in both industry and academia.

This book is about scalable approaches to processing large amounts of text with MapReduce. Given this focus, it makes sense to start with the most basic question: Why? There are many answers to this question, but we focus on two. First, “big data” is a fact of the world, and therefore an issue that real-world systems must grapple with. Second, across a wide range of text processing applications, more data translates into more effective algorithms, and thus it makes sense to take advantage of the plentiful amounts of data that surround us.

''',
'2010'),
('GNU Make Manual','GNU Make','FSF','pdf','https://www.gnu.org/software/make/manual/make.pdf',
'''
Official Manual for GNU Make by the Free Software Foundation
''',
'2010'	),
('Basics of Compiler Design','Compilers','Torben Mogensen','pdf','http://www.diku.dk/hjemmesider/ansatte/torbenm/Basics/basics_lulu2.pdf',
'''
In order to reduce the complexity of designing and building computers, nearly all of these are made to execute relatively simple commands (but do so very quickly). A program for a computer must be built by combining these very simple commands into a program in what is called machine language. Since this is a tedious and error-prone process most programming is, instead, done using a high-level programming language. This language can be very different from the machine language that the computer can execute, so some means of bridging the gap is required. This is where the compiler comes in.

A compiler translates (or compiles) a program written in a high-level programming language that is suitable for human programmers into the low-level machine language that is required by computers. During this process, the compiler will also attempt to spot and report obvious programmer mistakes.

''',
'2010'),
('Logic, Programming and Prolog','Prolog','Ulf Nilsson (more)','pdf','https://www.ida.liu.se/~ulfni/lpp/bok/bok.pdf',
'''
The main objective of both editions of this textbook is to provide a uniform account of both the foundations of logic programming and simple programming techniques in the programming language Prolog. The discussion of the foundations also facilitates a systematic survey of variants of the logic programming scheme, like constraint logic programming, deductive databases or concurrent logic programming. This book is not primarily intended to be a theoretical handbook on logic programming. Nor is it intended to be a book on advanced Prolog programming or on constraint logic programming. For each of these topics there are more suitable books around. Because of the diversity of the field there is of course a risk that nothing substantial is said about anything. We have tried to compensate for this risk by limiting our attention to (what we think are) the most important areas of logic programming and by providing the interested reader with pointers containing suggestions for further reading.
''',
'2000'),
('PyGTK 2.0 Tutorial','PyGTK','John Finlay','pdf','http://www.pygtk.org/dist/pygtk2-tut.pdf',
'''
PyGTK 2.0 is a set of Python modules which provide a Python interface to GTK+ 2.X. Throughout the rest of this document PyGTK refers to the 2.X version of PyGTK and GTK and GTK+ refer to the 2.X version of GTK+. The primary web site for PyGTK is www.pygtk.org. The primary author of PyGTK is: • James Henstridge (james@daa.com.au) who is assisted by the developers listed in the AUTHORS ﬁle in the PyGTK distribution and the PyGTK community.
''','2012'),
('Python Programming', 'Python','Wikibooks','pdf','https://upload.wikimedia.org/wikipedia/commons/9/91/Python_Programming.pdf',
'''
Python is a high-level, structured, open-source programming language that can be used for a wide variety of programming tasks. Python was created by Gudio Van Rossum in the early 1990s, its following has grown steadily and interest is increased markedly in the last few years or so. It is named after Monty Python's Flying Circus comedy program.

Python is used extensively for system administration (many vital components of Linux Distributions are written in it), also its a great language to teach programming to novice. NASA has used Python for its software systems and has adopted it as the standard scripting language for its Integrated Planning System. Python is also extensively used by Google to implement many components of its Web Crawler and Search Engine & Yahoo! for managing its discussion groups.
''','2012'),
('LaTeX','LaTeX','Wikibooks','pdf','https://upload.wikimedia.org/wikipedia/commons/2/2d/LaTeX.pdf',
'''
This is a book from Wikibooks about LaTeX, one of the most popular Macro packages for TeX.  
''','2013')
]

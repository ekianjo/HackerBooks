#encoding: utf-8
#overview
#first: window with tree like list of all books and directory to download the books to.  
#clicking on book name shows info about book + cover with 2 buttons: download / back to list
#download triggers wget event and launches zenity script to show progress. 
#after download the book should appear in a different way in the list to be launched directly from the app for reading.


#!/usr/bin/python

import gtk
import urllib, os


hackerbooks = [('Pro Git', 'Git', 'Scott Chacon','pdf','https://github.s3.amazonaws.com/media/progit.en.pdf',
'''Git is the version control system developed by Linus Torvalds for Linux kernel development. 
It took the open source world by storm since its inception in 2005, and is used by small development shops and giants like Google, Red Hat, and IBM, and of course many open source projects. 
A book by Git experts to turn you into a Git expert.

Introduces the world of distributed version control
Shows how to build a Git development workflow'''), 

('Think Complexity', 'General', 'Allen B. Downey','pdf','http://greenteapress.com/compmod/thinkcomplexity.pdf',
'''This book is about complexity science, data structures and algorithms, intermediate programming in Python, and the philosophy of science:'''
),

    ('The Linux Command Line', 'Command Line', 'William E. Shotts Jr.','pdf','http://downloads.sourceforge.net/project/linuxcommand/TLCL/09.12/TLCL-09.12.pdf?r=http%3A%2F%2Flinuxcommand.org%2Ftlcl.php&ts=1372170077&use_mirror=jaist',
'''You have experienced the shiny, point-and-click surface of your Linux computer—now dive below and explore its depths with the power of the command line.

The Linux Command Line takes you from your very first terminal keystrokes to writing full programs in Bash, the most popular Linux shell. Along the way you'll learn the timeless skills handed down by generations of gray-bearded, mouse-shunning gurus: file navigation, environment configuration, command chaining, pattern matching with regular expressions, and more.

In addition to that practical knowledge, author William Shotts reveals the philosophy behind these tools and the rich heritage that your desktop Linux machine has inherited from Unix supercomputers of yore.
'''        ),
('Clever Algorithms','Metaheuristics','Jason Browlee','pdf','http://www.lulu.com/shop/jason-brownlee/clever-algorithms-nature-inspired-programming-recipes/ebook/product-17386095.html'),
('Think Stats','Statistics','Allen B. Downey','pdf','http://greenteapress.com/thinkstats/thinkstats.pdf'),
("Street-Fighting Mathematics",'Problem Solving','Sanjoy Mahajan','pdf','https://mitpress.mit.edu/sites/default/files/titles/content/9780262514293_Creative_Commons_Edition.pdf','''
    In problem solving, as in street fighting, rules are for fools: do whatever works—don't just stand there! Yet we often fear an unjustified leap even though it may land us on a correct result. Traditional mathematics teaching is largely about solving exactly stated problems exactly, yet life often hands us partly defined problems needing only moderately accurate solutions. This engaging book is an antidote to the rigor mortis brought on by too much mathematical rigor, teaching us how to guess answers without needing a proof or an exact calculation.

In Street-Fighting Mathematics, Sanjoy Mahajan builds, sharpens, and demonstrates tools for educated guessing and down-and-dirty, opportunistic problem solving across diverse fields of knowledge—from mathematics to management. Mahajan describes six tools: dimensional analysis, easy cases, lumping, picture proofs, successive approximation, and reasoning by analogy. Illustrating each tool with numerous examples, he carefully separates the tool—the general principle—from the particular application so that the reader can most easily grasp the tool itself to use on problems of particular interest.

Street-Fighting Mathematics grew out of a short course taught by the author at MIT for students ranging from first-year undergraduates to graduate students ready for careers in physics, mathematics, management, electrical engineering, computer science, and biology. They benefited from an approach that avoided rigor and taught them how to use mathematics to solve real problems. '''),
('Algorithmic Game Theory','Game Theory','Noam Nisan and more','pdf','http://www.cambridge.org/journals/nisan/downloads/Nisan_Non-printable.pdf',
    '''In the last few years game theory has had a substantial impact on computer science, especially on Internet- and e-commerce-related issues. More than 40 of the top researchers in this field have written chapters that go from the foundations to the state of the art. Basic chapters on algorithmic methods for equilibria, mechanism design and combinatorial auctions are followed by chapters on incentives and pricing, cost sharing, information markets and cryptography and security. Students, researchers and practitioners alike need to learn more about these fascinating theoretical developments and their widespread practical application.
'''),
('Think Python','Python','Allen B. Downey','pdf','http://greenteapress.com/thinkpython/thinkpython.pdf',
'''The goal of this book is to teach you to think like a computer scientist. This way of thinking combines some of the best features of mathematics, engineering, and natural science. Like mathematicians, computer scientists use formal languages to denote ideas (speciﬁcally computations). Like
engineers, they design things, assembling components into systems and evaluating tradeoffs among alternatives. Like scientists, they observe the behavior of complex systems, form hypotheses, and
test predictions.'''),
('A Byte of Vim','Vim','Swaroop CH','pdf','http://files.swaroopch.com/vim/byte_of_vim_v051.pdf',
'''“A Byte of Vim” is a book which aims to help you to learn how to use the Vim editor (version 7), even if all you know is how to use the computer keyboard.
The first part of this book is meant for new users who want to understand what Vim is and learn how to use it.
The second part of this book is for people who already know how to use Vim and want to learn about features that make Vim so powerful, such as windows and tabs, personal information management, making it a programmer’s editor, how to extend Vim with your own plugins, and more.
'''),
('Advanced Linux Programming','Linux','CodeSourcery', 'pdf','http://www.advancedlinuxprogramming.com/alp-folder/advanced-linux-programming.pdf',
'''Advanced Linux Programming is intended for the programmer already familiar with the C programming language. Authors Alex Samuel, Jeffrey Oldham, and Mark Mitchell of CodeSourcery, LLC take a tutorial approach and teach the most important concepts and power features of the GNU/Linux system in application programs.

If you're a developer already experienced with programming for the GNU/Linux system, are experienced with another UNIX-like system and are interested in developing GNU/Linux software, or want to make the transition for a non-UNIX environment and are already familiar with the general principles of writing good software, this book is for you. In addition, you will find that this book is equally applicable to C and C++ programming. Even those progamming in other languages will find this book useful since the C language APIs and conventions are the lingua franca of GNU/Linux.
'''),
('Ruby Best Practices','Ruby','Gregory Brown','pdf','http://majesticseacreature.com/rbp-book/pdfs/rbp_1-0.pdf',
'''In 1993, when Ruby was born, Ruby had nothing. No user base except for me and a few close friends. No tradition. No idioms except for a few inherited from Perl, though I regretted most of them afterward.

But the language forms the community. The community nourishes the culture. In the last decade, users increased—hundreds of thousands of programmers fell in love with Ruby. They put great effort into the language and its community. Projects were born.
Idioms tailored for Ruby were invented and introduced. Ruby was influenced by Lisp and other functional programming languages. Ruby formed relationships between technologies and methodologies such as test-driven development and duck typing.

This book introduces a map of best practices of the language as of 2009. I’ve known Greg Brown for years, and he is an experienced Ruby developer who has contributed a lot of projects to the language, such as Ruport and Prawn. I am glad he compiled his
knowledge into this book.

His insights will help you become a better Ruby programmer.'''),
('Introduction to Machine Learning','Machine Learning','Alex Smola','pdf','http://alex.smola.org/drafts/thebook.pdf',
'''Over the past two decades Machine Learning has become one of the main-
stays of information technology and with that, a rather central, albeit usually
hidden, part of our life. With the ever increasing amounts of data becoming
available there is good reason to believe that smart data analysis will become
even more pervasive as a necessary ingredient for technological progress.''')
    ]








class InfoBooks(gtk.Window):
    def __init__(self):
        super(InfoBooks,self).__init__()

        self.set_size_request(600,400)
        self.set_position(gtk.WIN_POS_CENTER)
        self.set_border_width(8)

        self.connect("destroy",self.close_window)
        self.set_title("Book Information")



        table = gtk.Table(8, 4, False)
        table.set_col_spacings(10)

        title = gtk.Label("Description")

        halign = gtk.Alignment(0, 0, 0, 0)
        halign.add(title)
        
        table.attach(halign, 0, 1, 0, 1, gtk.FILL, gtk.FILL, 0, 0);

        textbuffer = gtk.TextBuffer()
        

        #self.book=self.findbookinfo()
        #print self.book

        textbuffer.set_text(self.findbookinfo())

        wins = gtk.TextView(buffer=textbuffer)
        wins.set_wrap_mode(gtk.WRAP_WORD)
        wins.set_editable(False)
        wins.modify_fg(gtk.STATE_NORMAL, gtk.gdk.Color(5140, 5140, 5140))
        wins.set_cursor_visible(False)
        table.attach(wins, 0, 2, 1, 3, gtk.FILL | gtk.EXPAND, gtk.FILL | gtk.EXPAND, 1, 1)

        download = gtk.Button("Download")
        download.set_size_request(50, 30)
        table.attach(download, 3, 4, 1, 2, gtk.FILL, gtk.SHRINK, 1, 1)
        download.connect_object("clicked", self.downloadbook, None)

        valign = gtk.Alignment(0, 0, 0, 0)
        close = gtk.Button("Close")
        close.set_size_request(70, 30)

        valign.add(close)
        table.set_row_spacing(1, 3)
        table.attach(valign, 3, 4, 2, 3, gtk.FILL, gtk.FILL | gtk.EXPAND, 1, 1)
        close.connect_object("clicked", self.close_window, None)

        halign2 = gtk.Alignment(0, 1, 0, 0)
        help = gtk.Button("Help")
        help.set_size_request(70, 30)
        halign2.add(help)
        table.set_row_spacing(3, 6)
        table.attach(halign2, 0, 1, 4, 5, gtk.FILL, gtk.FILL, 0, 0)
        
        ok = gtk.Button("OK")
        ok.set_size_request(70, 30)
        table.attach(ok, 3, 4, 4, 5, gtk.FILL, gtk.FILL, 0, 0);
                          
        self.add(table)

        self.show_all()

    def close_window(self, widget):
        self.destroy()


    def findbookinfo(self):
        for books in hackerbooks:
            if books[0]==mainwindow.caca: return books[5]

    def downloadbook(self,widget):
        try:
            os.mkdir("BOOKS")
        except:
            os.chdir("BOOKS")
        
        for books in hackerbooks:
            if books[0]==mainwindow.caca: 
                print books[4]
                urllib.urlretrieve(books[4],books[0]+".pdf")


        print "download finished"

    
class HackerBooks(gtk.Window): 
    def __init__(self):
        super(HackerBooks, self).__init__()
        
        self.set_size_request(450, 250)
        self.set_position(gtk.WIN_POS_CENTER)
        
        self.connect("destroy", gtk.main_quit)
        self.set_title("Hacker Books")
        self.caca="yooo"

        vbox = gtk.VBox(False, 8)
        
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


    def create_model(self):
        store = gtk.ListStore(str, str, str, str)

        for books in hackerbooks:
            store.append([books[0], books[1], books[2],books[3]])

        return store


    def create_columns(self, treeView):
    
        rendererText = gtk.CellRendererText()
        column = gtk.TreeViewColumn("Title", rendererText, text=0)
        column.set_sort_column_id(0)    
        treeView.append_column(column)
        
        rendererText = gtk.CellRendererText()
        column = gtk.TreeViewColumn("Language", rendererText, text=1)
        column.set_sort_column_id(1)
        treeView.append_column(column)

        rendererText = gtk.CellRendererText()
        column = gtk.TreeViewColumn("Author", rendererText, text=2)
        column.set_sort_column_id(2)
        treeView.append_column(column)

        rendererText = gtk.CellRendererText()
        column = gtk.TreeViewColumn("Format", rendererText, text=3)
        column.set_sort_column_id(3)
        treeView.append_column(column)


    def on_activated(self, widget, row, col):
        
        model = widget.get_model()
        text = model[row][0] + ", " + model[row][1] + ", " + model[row][2]
        self.statusbar.push(0, text)
        mainwindow.caca=model[row][0]
        print mainwindow.caca
        InfoBooks()



mainwindow=HackerBooks()
gtk.main()

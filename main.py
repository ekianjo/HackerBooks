#encoding: utf-8
#!/usr/bin/python

#FIRST RELEASE 0.1 CODENAME LUPIN ! By Ekianjo, 2013. 
#LICENSE: GPLv3 / http://opensource.org/licenses/GPL-3.0


#----- SECOND RELEASE GOALS
#ADD INFO on HOW MANY BOOKS ARE DOWNLOADED AND HOW MUCH SIZE THEY TAKE AND DISPLAY IN STATUS BAR
#NEED TO ADD SYSTEM IDENTIFICATION
#NEED TO ADD SCROLLABLE WINDOW CONTAINER FOR THE TEXTVIEW. IF NOT CANNOT SEE ALL TEXT.
#ADD BOOK LICENSE INFORMATION
#ADD BOOK YEAR INFO ?
#ALLOW READING OF HTML at least (reader tbc)
#PROGRESS DOWNLOAD BAR
#ADD MORE BOOKS
#ALLOW USAGE OF XOURNAL TO OPEN PDFs
#SEND STATS TO SERVER
#ALLOW FAVORITES
#REPORT DOWNLOAD ERRORS TO SERVER

import gtk #for the graphical user interface
import urllib, urllib2, os #os for file system operations, urllib for downloading and verifying the online connection. 
import subprocess #needed to launch separate application, in this case evince. 
import pango #used to determine a consistant style across the different systems. 


from hacker import *


class InfoBooks(gtk.Window):
    def __init__(self):
        super(InfoBooks,self).__init__()

        #set info window size attributes
        self.set_size_request(650,400)
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
        self.download.set_size_request(90, 40)
        table.attach(self.download, 3, 4, 1, 2, gtk.FILL, gtk.SHRINK, 1, 1)
        self.download.connect_object("clicked", self.downloadbook, None)

        #Close button attributes and connection to signals
        valign = gtk.Alignment(0, 0, 0, 0)
        close = gtk.Button("Close")
        close.set_size_request(90, 40)
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
        self.delete.set_size_request(90, 40)
        self.delete.connect_object("clicked", self.delete_book, None)
        halign2.add(self.delete)
        
        table.set_row_spacing(3, 6)
        table.attach(halign2, 0, 1, 4, 5, gtk.FILL, gtk.FILL, 0, 0)
        
        #read button attributes 
        self.readbtn = gtk.Button("Read")
        if self.check_book_exists()==False:
		    self.readbtn.set_sensitive(False)
        self.readbtn.set_size_request(90, 40)
        table.attach(self.readbtn, 3, 4, 4, 5, gtk.FILL, gtk.FILL, 0, 0);
        self.readbtn.connect_object("clicked", self.open_book, None)
        
        #add the finalized table layout to the window
        self.add(table)

        #display all
        self.show_all()

    #deletes a book from the ones already downloaded
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

	#checks if the internet connection is active
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

	#closes the info window
    def close_window(self, widget):
        self.destroy()

    #returns the book information 
    def findbookinfo(self):
        try:
	        for books in hackerbooks:
	            #returns the description of the book
	            if books[0]==mainwindow.caca: return books[5]
        except:
        	return ""

    #checks if the book exists in the folder where they are downloaded
    def check_book_exists(self):
    	bookname = mainwindow.caca+".pdf"
    	if os.path.isfile(bookname):
    		return True
    	else:
    		return False

    #downloads the book
    def downloadbook(self,widget):

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
    
#main window start. 
class HackerBooks(gtk.Window): 
    def __init__(self):
        super(HackerBooks, self).__init__()
        
        self.create_directory()
        
        #if displaymode is 0, show all, 1, show downloaded only
        self.displaymode=0


        self.set_size_request(750, 400)
        self.set_position(gtk.WIN_POS_CENTER)
        
        self.connect("destroy", gtk.main_quit)
        self.set_title("Hacker Books")
        #self.caca="yooo"

        vbox = gtk.VBox(False, 8)

        #Definition of menu bar
        mb=gtk.MenuBar()
        filemenu=gtk.Menu()
        filem=gtk.MenuItem("File")
        filem.set_submenu(filemenu)

        #about menu
        aboutmenu=gtk.Menu()
        aboutm=gtk.MenuItem("About")
        aboutm.set_submenu(aboutmenu)
        version=gtk.MenuItem("Version")
        version.connect("activate",self.about_this_application)
        aboutmenu.append(version)

        #Show menu
        showmenu=gtk.Menu()
        showm=gtk.MenuItem("Display")
        showm.set_submenu(showmenu)
        showall=gtk.MenuItem("Show All Books")
        showall.connect("activate",self.all_books)
        showmenu.append(showall)
        showgotbooks=gtk.MenuItem('Show Downloaded Books')
        showgotbooks.connect("activate",self.downloaded_books_only)
        showmenu.append(showgotbooks)
        showleftbooks=gtk.MenuItem('Show Books Left to Download')
        showleftbooks.connect("activate",self.left_to_download)
        showmenu.append(showleftbooks)

        #File menu
        exit=gtk.MenuItem('Exit')
        exit.connect("activate",gtk.main_quit)
        filemenu.append(exit)

        #adding it back in the menu together
        mb.append(filem)
        mb.append(showm)
        mb.append(aboutm)

        #packs the vbox
        vbox.pack_start(mb,False,False)
        
        #sw is a scrolled window
        sw = gtk.ScrolledWindow()
        sw.set_shadow_type(gtk.SHADOW_ETCHED_IN)
        sw.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
        
        vbox.pack_start(sw, True, True, 0)

        self.store = self.create_model()

        self.treeView = gtk.TreeView(self.store)
        self.treeView.connect("row-activated", self.on_activated)
        self.treeView.set_rules_hint(True)
        sw.add(self.treeView)

        self.create_columns(self.treeView)
        self.statusbar = gtk.Statusbar()
        
        #packs the statusbar
        vbox.pack_start(self.statusbar, False, False, 0)

        #add the vbox in the window
        self.add(vbox)
        self.show_all()


    def about_this_application(self,widget):
        aboutthis = gtk.AboutDialog()
        aboutthis.set_program_name("HackerBooks")
        aboutthis.set_version("0.1.1")
        aboutthis.set_copyright("(c) Ekianjo 2013")
        aboutthis.set_comments("HackerBooks is a small application to download and manage free books about Programming and Computer Science")
        aboutthis.set_website("https://github.com/ekianjo/HackerBooks")
        aboutthis.set_logo(gtk.gdk.pixbuf_new_from_file("../icon.png"))
        aboutthis.run()
        aboutthis.destroy()

    #enables the display of all books regardless of whether they were downloaded or not
    def all_books(self,widget):
    	#displaymode is now all books.
    	self.displaymode=0
    	self.treeView.set_model(self.create_model())

   	#enables only the display of books already available offline
    def downloaded_books_only(self,widget):
    	#ensure that the displaymode is now set to only downloaded books.
    	self.displaymode=1
    	self.treeView.set_model(self.create_model())

    def left_to_download(self,widget):
        self.displaymode=2
        self.treeView.set_model(self.create_model())


   	#creates the folder where books are saved if necessary
    def create_directory(self):
    	if os.path.isdir("BOOKS")==False:
    		os.makedirs("BOOKS")

    	os.chdir("BOOKS")


    def create_model(self):
        self.store = gtk.ListStore(str, str, str, str)

        for books in hackerbooks:
            bookname=books[0]+".pdf"
            if self.displaymode==1:
        		if os.path.isfile(bookname):
        			print bookname
	        		self.store.append([books[0], books[1], books[2],books[3]])
            elif self.displaymode==2:
                if os.path.isfile(bookname)==False:
                    self.store.append([books[0], books[1], books[2],books[3]])
            else:
	        	self.store.append([books[0], books[1], books[2],books[3]])
        return self.store

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

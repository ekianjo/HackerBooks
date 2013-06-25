#overview
#first: window with tree like list of all books and directory to download the books to.  
#clicking on book name shows info about book + cover with 2 buttons: download / back to list
#download triggers wget event and launches zenity script to show progress. 
#after download the book should appear in a different way in the list to be launched directly from the app for reading.


#!/usr/bin/python
import gtk

hackerbooks = [('book1', 'c', 'author','pdf'), ('book2', 'python', 'author','mobi'),
    ('book3', 'c', 'author3','pdf')]
    
class HackerBooks(gtk.Window): 
    def __init__(self):
        super(HackerBooks, self).__init__()
        
        self.set_size_request(350, 250)
        self.set_position(gtk.WIN_POS_CENTER)
        
        self.connect("destroy", gtk.main_quit)
        self.set_title("ListView")

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
        column = gtk.TreeViewColumn("Format", rendererText, text=2)
        column.set_sort_column_id(2)
        treeView.append_column(column)


    def on_activated(self, widget, row, col):
        
        model = widget.get_model()
        text = model[row][0] + ", " + model[row][1] + ", " + model[row][2]
        self.statusbar.push(0, text)

HackerBooks()
gtk.main()

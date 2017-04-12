from gi.repository import Gtk
from gi.repository import Gdk
from NavBar import NavBar

class HomeView:
    def __init__(self, parent):
       
	
        # Creates a new button with the label "Hello World".
        self.button = Gtk.Button("Game 1")
        self.button.set_can_focus(False)
        self.button.set_size_request(150,150)
	self.button.set_name("HomeView_Game1Button")
	#for child in self.button.get_children():
	 #   child.set_label("<span size='10000' color='#2F343F'><b>SPELLING Spell the word listening to audio.</b></span>")
	  #  child.set_use_markup(True)

        self.button2 = Gtk.Button("Game 2")
        self.button2.set_can_focus(False)
        self.button2.set_size_request(150,150)
	self.button2.set_name("HomeView_Game2Button")

        self.button3 = Gtk.Button("Game 3")
        self.button3.set_can_focus(False)
        self.button3.set_size_request(150,150)
	self.button3.set_name("HomeView_Game3Button")

        # image = gtk.Image()
        # image.set_from_file("background.png")
        # image.show()
        # self.nextButton.add(image)
        # #make a gdk.color for red
        # map = self.nextButton.get_colormap()
        # color = map.alloc_color("#2F343F")

        # #copy the current style and replace the background
        # style = self.nextButton.get_style().copy()
        # style.bg[gtk.STATE_NORMAL] = color

        # #set the button's style to the one you created
        # self.nextButton.set_style(style)

        self.vbox = Gtk.VBox(False, 0)
        self.vbox.show()

	self.navBar = NavBar(False)
        self.vbox.pack_start(self.navBar, False, False, 0)

        self.selectGame = Gtk.Label("")
	self.selectGame.set_name("HomeView_SelectGame")
        self.selectGame.set_size_request(150,30)
        self.selectGame.set_markup("<span size='25000' color='#2F343F'><b><u>SELECT A GAME</u></b></span>")
        self.selectGame.show()

        valign2 = Gtk.Alignment(xscale = 1.0, yscale=1.0)
        valign2.add(self.selectGame)
        self.vbox.pack_start(valign2, True, True, 0)
        valign2.show()

        self.hbox = Gtk.HBox(False, 0)
        self.hbox.pack_start(self.button, True, True, 10)
        self.hbox.pack_start(self.button2, True, True, 10)
        self.hbox.pack_start(self.button3, True, True, 10)
        self.vbox.pack_start(self.hbox, True, True, 10)
        self.hbox.show()


        # The final step is to display this newly created widget.
        self.button.show()
        self.button2.show()
        self.button3.show()
	print("I am here")

	parent.set_canvas(self.vbox)
	

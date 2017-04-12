# @author: Angel Shiwakoti
# @createdOn: 04/11/2017
# This class created the required number of textfields based
# on the number of characters in a given word.

from gi.repository import Gtk
from gi.repository import Gdk
import re

class NavBar(Gtk.Alignment):
    def __init__(self, showBackButton):

        # Call init method for superclass
        Gtk.Alignment.__init__(self)

	self.showButton = showBackButton

 	self.gameName = Gtk.Label("")
        self.gameName.set_markup("<span size='17000' color='#F5F6F7'><b>SPELLING ACTIVITY</b></span>")

	self.hbox = Gtk.Box(spacing = 0)
	self.eb = Gtk.EventBox()
        self.eb.add(self.gameName)
        self.eb.set_size_request(150,50)
        self.eb.modify_bg(Gtk.StateType.NORMAL, Gdk.color_parse("#2F343F"))

	self.button = Gtk.Button("< Back")
        #self.button.set_can_focus(False)
        self.button.set_size_request(120,50)
	self.button.set_name("NavBar_BackButton")
	
	# Load the css file
	style_provider = Gtk.CssProvider()
	css_file = open("style.css", 'rb')

	# Read the css code and close the file 
	css = css_file.read()
	css_file.close()
	
	# Load the css for rendering
	style_provider.load_from_data(css)
	Gtk.StyleContext.add_provider_for_screen(Gdk.Screen.get_default(),style_provider, 
	Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)
	
	#color = Gdk.RGBA()
	#color.parse("#2F343F")
	#color.to_string()
	#self.button.override_background_color(Gtk.StateFlags.NORMAL, color)	

	self.displayBackButton()

	self.add(self.hbox)

	self.gameName.show()
	self.hbox.show()
	self.show()


    def displayBackButton(self):
	if self.showButton:
	    self.hbox.pack_start(self.button, False, False, 0)
	    self.hbox.pack_start(self.eb, True, True, 0)
	    self.button.show()
	    self.eb.show()
	else:
	    self.hbox.pack_start(self.eb, True, True, 0)
	    self.eb.show()

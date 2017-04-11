from GameView import GameView
from GameController import GameController
from gi.repository import Gtk
from gi.repository import Gdk

class HomeController:
    def __init__(self, view, parent):

        self.view = view

	self.parent = parent
	
	self.view.button.connect_object("clicked", self.render_game1, "")

    # Render the first game
    def render_game1(self, button):
        self.view = GameView(self.parent)
        self.controller = GameController(self.view, self.parent)

    def delete_event(self, widget, event, data=None):
        print "delete event occurred"
        # Change FALSE to TRUE and the main window will not be destroyed
        # with a "delete_event".
        return False

    def destroy(self, widget, data=None):
        print "destroy signal occurred"
        gtk.main_quit()

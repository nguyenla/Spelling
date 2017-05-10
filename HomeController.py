from GameView import GameView
from GameController import GameController
from Game2View import Game2View
from Game3Controller import Game3Controller
from Game3View import Game3View
from Game2Controller import Game2Controller
from gi.repository import Gtk
from gi.repository import Gdk

class HomeController:
    def __init__(self, view, parent):

        self.view = view

	self.parent = parent
	
	self.view.button.connect_object("clicked", self.render_game1, "")
	self.view.button2.connect_object("clicked", self.render_game2, "")
	self.view.button3.connect_object("clicked", self.render_game3, "")

    # Render the first game
    def render_game1(self, button):
        self.view = GameView(self.parent)
        self.controller = GameController(self.view, self.parent)

    # Render the second game
    def render_game2(self, button):
        self.view = Game2View(self.parent)
        self.controller = Game2Controller(self.view, self.parent)

    # Render the third game
    def render_game3(self, button):
        self.view = Game3View(self.parent)
        self.controller = Game3Controller(self.view, self.parent)

    def delete_event(self, widget, event, data=None):
        print "delete event occurred"
        # Change FALSE to TRUE and the main window will not be destroyed
        # with a "delete_event".
        return False

    def destroy(self, widget, data=None):
        print "destroy signal occurred"
        gtk.main_quit()

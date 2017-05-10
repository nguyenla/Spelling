from gi.repository import Gtk
from NavBar import NavBar
from TypeBoxVert import TypeBoxVert

class Game3View:
    def __init__(self, parent):
        
	self.parent = parent
        #create the buttons for the game. Make sure you can't select them
        self.skip = Gtk.Button("SKIP")
        self.skip.set_can_focus(False)
	self.skip.set_size_request(500,60)
	self.skip.set_name("Game3View_SkipButton")

        self.word1 = Gtk.Button("word1")
        self.word1.set_can_focus(False)
    	self.word1.set_size_request(500,60)
    	self.word1.set_name("Game3View_WordButton")

        self.word2 = Gtk.Button("word2")
        self.word2.set_can_focus(False)
        self.word2.set_size_request(500,60)
        self.word2.set_name("Game3View_WordButton")

        self.word3 = Gtk.Button("word3")
        self.word3.set_can_focus(False)
        self.word3.set_size_request(500,60)
        self.word3.set_name("Game3View_WordButton")

        self.word4 = Gtk.Button("word4")
        self.word4.set_can_focus(False)
        self.word4.set_size_request(500,60)
        self.word4.set_name("Game3View_WordButton")

        self.word5 = Gtk.Button("word5")
        self.word5.set_can_focus(False)
        self.word5.set_size_request(500,60)
        self.word5.set_name("Game3View_WordButton")

	    #create the labels for the game
        self.def1 = Gtk.Label("def1")

        self.label = Gtk.Label("LEVEL 1")
        self.label.set_size_request(200,50)
        self.label.set_name("Game3View_LevelLabel")

        self.scoreLabel = Gtk.Label("SCORE: 0")
        self.scoreLabel.set_size_request(200,50)
        self.scoreLabel.set_name("Game3View_ScoreLabel")

        self.resultLabel = Gtk.Label("")
        self.skipLabel = Gtk.Label("Skips left: 0")
        
	#create a vertical box and add it to the window
        self.vbox = Gtk.VBox(False, 0)
        self.vbox.show()

	self.navBar = NavBar(True)
        self.vbox.pack_start(self.navBar, False, False, 0)

        self.button1Hbox = Gtk.Alignment(xscale = 0.0, yscale=1.0)
        self.button2Hbox = Gtk.Alignment(xscale = 0.0, yscale=1.0)
        self.button3Hbox = Gtk.Alignment(xscale = 0.0, yscale=1.0)
        self.button4Hbox = Gtk.Alignment(xscale = 0.0, yscale=1.0)
        self.button5Hbox = Gtk.Alignment(xscale = 0.0, yscale=1.0)
        self.skipHbox = Gtk.Alignment(xscale = 0.0, yscale=1.0)
        self.levelHbox = Gtk.HBox(False, 0)

        self.button1Hbox.add(self.word1)
        self.button2Hbox.add(self.word2)
        self.button3Hbox.add(self.word3)
        self.button4Hbox.add(self.word4)
        self.button5Hbox.add(self.word5)
        self.levelHbox.pack_start(self.label, False, False, 0)
        self.levelHbox.pack_end(self.scoreLabel, False, False, 0)
	self.skipHbox.add(self.skip)

	    #put the horizontal box in the vertical box. This allows for proper
        #placement of the defintion on the screen
        self.vbox.pack_start(self.levelHbox, False, False, 0)
        self.vbox.add(self.def1)
        #stacks the word buttons and result label vertically on the screen,
        self.vbox.pack_start(self.button1Hbox, False, False, 0)
        self.vbox.pack_start(self.button2Hbox, False, False, 5)
        self.vbox.pack_start(self.button3Hbox, False, False, 0)
        self.vbox.pack_start(self.button4Hbox, False, False, 5)
        self.vbox.pack_start(self.button5Hbox, False, False, 0)
        self.vbox.pack_start(self.resultLabel, True, True, 0)

        self.vbox.add(self.skipHbox)

        # Makes everything visible on the screen
        self.skip.show()
        self.word1.show()
        self.word2.show()
        self.word3.show()
        self.word4.show()
        self.word5.show()
        self.button1Hbox.show()
        self.button2Hbox.show()
        self.button3Hbox.show()
        self.button4Hbox.show()
        self.button5Hbox.show()
        self.def1.show()
        self.label.show()
        self.scoreLabel.show()
        self.resultLabel.show()
        self.skipLabel.show()
	self.levelHbox.show()
	self.skipHbox.show()

        self.parent.set_canvas(self.vbox)

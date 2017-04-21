from gi.repository import Gtk
from gi.repository import Gdk
from NavBar import NavBar

class Game2View:
    def __init__(self, parent):
        #Generate the necessary buttons
        self.word1 = Gtk.Button("word1")
        self.word1.set_can_focus(False)
    	self.word1.set_size_request(500,60)
    	self.word1.set_name("Game2View_Word1Button")

        self.word2 = Gtk.Button("word2")
        self.word2.set_can_focus(False)
        self.word2.set_size_request(500,60)
        self.word2.set_name("Game2View_Word2Button")

        self.word3 = Gtk.Button("word3")
        self.word3.set_can_focus(False)
    	self.word3.set_size_request(500,60)
    	self.word3.set_name("Game2View_Word3Button")

        self.word4 = Gtk.Button("word4")
        self.word4.set_can_focus(False)
    	self.word4.set_size_request(500,60)
    	self.word4.set_name("Game2View_Word4Button")

        self.skip = Gtk.Button("SKIP\n(3 Left)")
        self.skip.set_name("Game2View_SkipButton")
        self.skip.set_size_request(500,60)
        self.skip.set_can_focus(False)

        self.next = Gtk.Button("NEXT LEVEL")
        self.skip.set_can_focus(False)

        #Generate the necessary labels
        self.levelLabel = Gtk.Label("LEVEL 1")
        self.levelLabel.set_size_request(200,50)
        self.levelLabel.set_name("Game2View_LevelLabel")

        self.scoreLabel = Gtk.Label("SCORE: 0")
        self.scoreLabel.set_size_request(200,50)
        self.scoreLabel.set_name("Game2View_ScoreLabel")

        self.resultLabel = Gtk.Label("")

        self.instructionLabel = Gtk.Label("")
        self.instructionLabel.set_markup("<span size='17000'><b>SELECT THE MISSPELLED WORD</b></span>")

        self.levelLabel.set_markup("<span size='15000'><b>LEVEL 1</b></span>")
        self.scoreLabel.set_markup("<span size='15000'><b>SCORE: 0</b></span>")


        self.vbox = Gtk.VBox(False, 10)
        self.vbox.show()

        self.navBar = NavBar(True)
        self.vbox.pack_start(self.navBar, False, False, 0)

        #Pack the first box with everything
        self.button1Hbox = Gtk.Alignment(xscale = 0.0, yscale=1.0)
        self.button2Hbox = Gtk.Alignment(xscale = 0.0, yscale=1.0)
        self.button3Hbox = Gtk.Alignment(xscale = 0.0, yscale=1.0)
        self.button4Hbox = Gtk.Alignment(xscale = 0.0, yscale=1.0)
        self.skipHbox = Gtk.Alignment(xscale = 0.0, yscale=1.0)
        self.levelHbox = Gtk.HBox(False, 0)

        self.button1Hbox.add(self.word1)
        self.button2Hbox.add(self.word2)
        self.button3Hbox.add(self.word3)
        self.button4Hbox.add(self.word4)
        self.skipHbox.add(self.skip)
        self.levelHbox.pack_start(self.levelLabel, False, False, 0)
        self.levelHbox.pack_end(self.scoreLabel, False, False, 0)
        self.vbox.pack_start(self.levelHbox, False, False, 0)
        self.vbox.add(self.instructionLabel)
        self.vbox.pack_start(self.button1Hbox, False, False, 5)
        self.vbox.pack_start(self.button2Hbox, False, False, 0)
        self.vbox.pack_start(self.button3Hbox, False, False, 5)
        self.vbox.pack_start(self.button4Hbox, False, False, 0)
        self.vbox.pack_start(self.resultLabel, False, False, 0)

        self.vbox.add(self.skipHbox)

        # The final step is to display this newly created widget.
        self.skip.show()
        self.word1.show()
        self.word2.show()
        self.word3.show()
        self.word4.show()
        self.levelLabel.show()
        self.scoreLabel.show()
        self.resultLabel.show()
        self.button1Hbox.show()
        self.button2Hbox.show()
        self.button3Hbox.show()
        self.button4Hbox.show()
        self.skipHbox.show()
        self.levelHbox.show()
        self.instructionLabel.show()

        parent.set_canvas(self.vbox)

from gi.repository import Gtk
from TypeBox import TypeBox
from NavBar import NavBar

class GameView:
    def __init__(self, parent):
        self.parent = parent
        self.set_up_screen()

    # This function displays the screen at the beginning of each level
    def set_up_screen(self):
        # Generate the necessary buttons
        # The "PLAY" button
        self.left_button = Gtk.Button("Play Word")
        self.left_button.set_can_focus(False)
        self.left_button.set_size_request(20,30)

        # The "NEXT" button
        self.right_button = Gtk.Button("SKIP")
        self.right_button.set_can_focus(False)
        self.left_button.set_size_request(20,30)

        # The boxes for the letters
        self.typeBox = TypeBox()

        # Generate the necessary labels: Level, Score, correct/ incorrect feedback
        self.levelLabel = Gtk.Label("LEVEL 1")
        self.levelLabel.set_size_request(200,50)
        self.levelLabel.set_name("Game1View_LevelLabel")

        self.scoreLabel = Gtk.Label("SCORE: 0")
        self.scoreLabel.set_size_request(200,50)
        self.scoreLabel.set_name("Game1View_ScoreLabel")

        self.resultLabel = Gtk.Label("")
        self.resultLabel.set_name("Game1View_ResultLabel")

        # ------------------------- ARRANGING ON THE SCREEN ------------------#
        # A VBox to pack the labels and the typebox vertically
        self.vbox = Gtk.VBox(False, 10)
        self.vbox.show()

        self.navBar = NavBar(True)
        self.vbox.pack_start(self.navBar, False, False, 0)

        # Create VBoxes and HBoxes to hold elements on the screen
        self.levelHbox = Gtk.HBox(False, 0)
        self.levelHbox.pack_start(self.levelLabel, False, False, 0)
        self.levelHbox.pack_end(self.scoreLabel, False, False, 0)
        self.vbox.pack_start(self.levelHbox, True, True, 0)
        #self.vbox.add(self.levelHbox)

        #self.vbox.pack_start(self.scoreLabel, True, True, 0)
        #self.vbox.pack_start(self.levelLabel, True, True, 0)
        self.vbox.pack_start(self.typeBox.hbox, True, True, 0)
        self.vbox.pack_start(self.resultLabel, True, True, 0)

        # A HBox to keep the two buttons "PLAY" and "NEXT"
        self.hbox = Gtk.HBox(False, 0)
        self.hbox.pack_start(self.left_button, True, True, 0)
        self.hbox.pack_start(self.right_button, True, True, 0)

        self.vbox.add(self.hbox)
        self.hbox.show()

        # The final step is to display this newly created widget.
        self.left_button.show()
        self.right_button.show()
        self.typeBox.show()
        self.levelLabel.show()
        self.levelHbox.show()
        self.scoreLabel.show()
        self.resultLabel.show()

        self.parent.set_canvas(self.vbox)

    def show_review_screen(self):
        # Remove all widgets on the screen
        self.typeBox.createTextBoxes(0)
        # self.vbox.remove(self.typeBox.hbox)
        # self.vbox.remove(self.resultLabel)
        # self.vbox.remove(self.levelLabel)
        # self.vbox.remove(self.hbox)

        self.left_button.set_label("Retry")
        self.right_button.set_label("Next Level")
        self.levelLabel.set_text("Level review")

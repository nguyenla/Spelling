from gi.repository import Gtk
from TypeBox import TypeBox

class GameView:
    def __init__(self, parent):
        self.parent = parent
        self.set_up_screen()

    # This function displays the screen at the beginning of each level
    def set_up_screen(self):
        # The "PLAY" button
        self.left_button = Gtk.Button("Play Word")
        self.left_button.set_can_focus(False)
        self.left_button.set_size_request(20,30)

        # The "NEXT" button
        self.right_button = Gtk.Button("SKIP")
        self.right_button.set_can_focus(False)

        # The boxes for the letters
        self.typeBox = TypeBox()

        # 3 labels: Level, Score, correct/ incorrect feedback
        self.label = Gtk.Label("LEVEL 1")
        self.scoreLabel = Gtk.Label("SCORE: 0")
        self.resultLabel = Gtk.Label("")

        # A VBox to pack the labels and the typebox vertically
        self.vbox = Gtk.VBox(False, 0)
        self.vbox.show()

        self.vbox.pack_start(self.scoreLabel, True, True, 0)
        self.vbox.pack_start(self.label, True, True, 0)
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
        self.label.show()
        self.scoreLabel.show()
        self.resultLabel.show()

        self.parent.set_canvas(self.vbox)

    def show_review_screen(self):
        # Remove all widgets on the screen
        self.typeBox.createTextBoxes(0)
        # self.vbox.remove(self.typeBox.hbox)
        # self.vbox.remove(self.resultLabel)
        # self.vbox.remove(self.label)
        # self.vbox.remove(self.hbox)

        self.left_button.set_label("Retry")
        self.right_button.set_label("Next Level")
        self.label.set_text("Level review")

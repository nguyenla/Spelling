# @author: Angel Shiwakoti
# @createdOn: 01/31/2017
# This class created the required number of textfields based
# on the number of characters in a given word.

from gi.repository import Gtk
import re

class TypeBox(Gtk.HBox):
    def __init__(self):

        # Call init method for superclass
        Gtk.HBox.__init__(self)

        # Array to hold textFields
        self.textFields = []

        # hBox holds all the textFields
        self.hbox = Gtk.HBox(False, 0)
        self.hbox.show()


    # This method creates the necessary amount of textfields
    # based on the number of characters in current word
    def createTextBoxes(self, size):
        self.numBoxes = size
        requiredCount = self.resetContent()
        for index in range(requiredCount):
            self.textFields.append(Gtk.Entry())

        # disable the highlighting of the boxes
        for box in self.textFields:
            box.set_can_focus(False)
        self.showBoxes()


    # This method resets the text for existing textfields.
    # If there are more than required textfields previously
    # created, this method removes them.
    def resetContent(self):
        if (len(self.textFields) == 0):
            return self.numBoxes

        # If we have more text boxes than we need
        elif (len(self.textFields) > self.numBoxes):
            removeCount = len(self.textFields) - self.numBoxes
            for index in range(removeCount):
                self.hbox.remove(self.textFields.pop())

        self.resetTextBox()
        return self.numBoxes - len(self.textFields)


    # This method shows all the existing textfields.
    def showBoxes(self):
        for textField in self.textFields:
            textField.set_size_request(60,35)
            textField.set_width_chars(4)
            self.hbox.pack_start(textField, True, False, 5)
            textField.set_property("editable", False)
            textField.set_alignment(xalign = 0.5)
	    textField.set_max_length(1)
            textField.set_name("TypeBox_TextField")
            textField.show()

    def addWord(self, word):
        self.resetTextBox()
        for index in range(len(word)):
            self.textFields[index].set_text(word[index])

    # Reset the text of all textbox to ""
    def resetTextBox(self):
        for textField in self.textFields:
            textField.set_text("")

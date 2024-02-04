from db.db_utils import insert_entry, print_table
from PySide6.QtWidgets import QApplication
from ui.gui import MainWindow
import sys

app = QApplication(sys.argv)
window = MainWindow()

# Creates variables for widget shorthand
home_widget = window.stacked_widget.widget(0)
add_widget = window.stacked_widget.widget(1)
edit_widget = window.stacked_widget.widget(2)
visualize_widget = window.stacked_widget.widget(3)

# Gets and returns current values input from user
def get_entry():
    if add_widget.ui.titleEdit.text() != '' and add_widget.ui.authorEdit.text() != '' and add_widget.ui.yearEdit.text() != '':
        add_widget.ui.responseLabel.setText("Book added successfully!")
    else:
        add_widget.ui.responseLabel.setText("Missing required field.")

    entry_items = (add_widget.ui.titleEdit.text(),
                   add_widget.ui.authorEdit.text(),
                   add_widget.ui.yearEdit.text(),
                   add_widget.ui.genreBox.currentText(),
                   int(add_widget.ui.ratingSlider.value()))
    return entry_items

# Empties out text fields
def clear_text():
    add_widget.ui.titleEdit.setText("")
    add_widget.ui.authorEdit.setText("")
    add_widget.ui.yearEdit.setText("")

def main_window_start():
    window.show()

def page_function():
    # Hooks up buttons for Add Book page
    add_widget.ui.submitButton.clicked.connect(lambda: insert_entry(get_entry()))
    add_widget.ui.printButton.clicked.connect(lambda: print_table())
    add_widget.ui.submitButton.clicked.connect(lambda: clear_text())
    add_widget.ui.submitButton.clicked.connect(add_widget.ui.titleEdit.setFocus)

# Makes menu navigation through buttons work
def menu_navigation():
    # Navigates to home page
    window.menu_widget.ui.homeButton.clicked.connect(lambda: window.stacked_widget.setCurrentIndex(0))
    # Navigates to add book page and sets focus on first line edit
    window.menu_widget.ui.addButton.clicked.connect(lambda: window.stacked_widget.setCurrentIndex(1))
    window.menu_widget.ui.addButton.clicked.connect(add_widget.ui.titleEdit.setFocus)
    # Navigates to edit book page
    window.menu_widget.ui.editButton.clicked.connect(lambda: window.stacked_widget.setCurrentIndex(2))
    # Navigates to visualization page
    window.menu_widget.ui.visualizeButton.clicked.connect(lambda: window.stacked_widget.setCurrentIndex(3))

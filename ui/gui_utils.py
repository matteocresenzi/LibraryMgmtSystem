from db.db_utils import insert_entry, print_table, select_table, delete_item
from PySide6.QtWidgets import QApplication, QTableWidgetItem
from ui.gui import MainWindow
import sys

app = QApplication(sys.argv)
window = MainWindow()

# Creates variables for widget shorthand
home_widget = window.stacked_widget.widget(0)
add_widget = window.stacked_widget.widget(1)
edit_widget = window.stacked_widget.widget(2)
visualize_widget = window.stacked_widget.widget(3)

# Array for helping back button functionality
last_page_array = [0]
# Selected row default to 0
selected_row = 0

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

# Used for back buttons
def set_back_index():
    cur_page = window.stacked_widget.currentIndex()
    last_page_array[0] = cur_page

# If a cell is clicked index changes, otherwise 0
def selected_items():
    global selected_row

    if not home_widget.ui.tableWidget.selectedItems():
        selected_row = 0
    else:
        selected_row = home_widget.ui.tableWidget.currentRow() + 1
    return selected_row

# Deletes entry from database
def delete_entry():
    if selected_row != 0:
        delete_item(selected_row)
        home_widget.ui.responseLabel.setText(f'Book {selected_row} deleted!')
    else:
        home_widget.ui.responseLabel.setText('Nothing to Delete.')
    home_widget.ui.tableWidget.removeRow(selected_row - 1)

# Populates table on home page
def table_populate():
    home_widget.ui.tableWidget.setRowCount(0)

    data = select_table()

    # Enumeration still doesn't make sense
    for row, rowData in enumerate(data):
        home_widget.ui.tableWidget.insertRow(row)
        for col, value in enumerate(rowData):
            item = QTableWidgetItem(value)
            home_widget.ui.tableWidget.setItem(row, col, item)

def page_function():
    # Hooks up buttons for Home page
    home_widget.ui.addButton.clicked.connect(lambda: set_back_index())
    home_widget.ui.addButton.clicked.connect(lambda: window.stacked_widget.setCurrentIndex(1))
    home_widget.ui.editButton.clicked.connect(lambda: set_back_index())
    home_widget.ui.editButton.clicked.connect(lambda: window.stacked_widget.setCurrentIndex(2))
    home_widget.ui.deleteButton.clicked.connect(lambda: delete_entry())
    home_widget.ui.exitButton.clicked.connect(lambda: sys.exit())
    home_widget.ui.tableWidget.itemSelectionChanged.connect(lambda: selected_items())

    # Hooks up buttons for Add Book page
    add_widget.ui.submitButton.clicked.connect(lambda: insert_entry(get_entry()))
    add_widget.ui.submitButton.clicked.connect(lambda: clear_text())
    add_widget.ui.submitButton.clicked.connect(add_widget.ui.titleEdit.setFocus)
    add_widget.ui.printButton.clicked.connect(lambda: print_table())
    add_widget.ui.backButton.clicked.connect(lambda: window.stacked_widget.setCurrentIndex(last_page_array[0]))
    add_widget.ui.backButton.clicked.connect(lambda: table_populate())

# Makes menu navigation through buttons work
def menu_navigation():
    # Navigates to home page and stores index in back array
    window.menu_widget.ui.homeButton.clicked.connect(lambda: set_back_index())
    window.menu_widget.ui.homeButton.clicked.connect(lambda: window.stacked_widget.setCurrentIndex(0))
    window.menu_widget.ui.homeButton.clicked.connect(lambda: table_populate())

    # Navigates to add book page and sets focus on first line edit and stores index in back array
    window.menu_widget.ui.addButton.clicked.connect(lambda: set_back_index())
    window.menu_widget.ui.addButton.clicked.connect(lambda: window.stacked_widget.setCurrentIndex(1))
    window.menu_widget.ui.addButton.clicked.connect(add_widget.ui.titleEdit.setFocus)

    # Navigates to edit book page and stores index in back array
    window.menu_widget.ui.editButton.clicked.connect(lambda: set_back_index())
    window.menu_widget.ui.editButton.clicked.connect(lambda: window.stacked_widget.setCurrentIndex(2))

    # Navigates to visualization page and stores index in back array
    window.menu_widget.ui.visualizeButton.clicked.connect(lambda: set_back_index())
    window.menu_widget.ui.visualizeButton.clicked.connect(lambda: window.stacked_widget.setCurrentIndex(3))

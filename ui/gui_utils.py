from db.db_utils import insert_entry, print_table
from PySide6.QtWidgets import QApplication
from ui.gui import AddBookWindow
import sys

app = QApplication(sys.argv)
add_book_window = AddBookWindow()

def init_add_book_window():
    add_book_window.show()
    add_book_window.ui.submitButton.clicked.connect(main_insert)
    add_book_window.ui.printButton.clicked.connect(print_table)
    add_book_window.ui.submitButton.clicked.connect(add_book_window.clear_text)
    add_book_window.ui.submitButton.clicked.connect(add_book_window.ui.titleEdit.setFocus)

def main_insert():
    insert_entry(add_book_window.get_entry())

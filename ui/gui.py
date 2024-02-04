from PySide6.QtWidgets import QMainWindow
from ui.ui_add_book import Ui_MainWindow
from db.db_utils import insert_entry


class AddBookWindow(QMainWindow):
    def __init__(self):
        super(AddBookWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Personal Library")

    # Gets and returns current values input from user
    def get_entry(self):
        if self.ui.titleEdit.text() != '' and self.ui.authorEdit.text() != '' and self.ui.yearEdit.text() != '':
            self.ui.responseLabel.setText("Book added successfully!")
        else:
            self.ui.responseLabel.setText("Missing required field.")

        entry_items = (self.ui.titleEdit.text(),
                       self.ui.authorEdit.text(),
                       self.ui.yearEdit.text(),
                       self.ui.genreBox.currentText(),
                       int(self.ui.ratingSlider.value()))
        return entry_items

    def insert_book(self):
        insert_entry(self.get_entry())

    # Empties out text fields
    def clear_text(self):
        self.ui.titleEdit.setText("")
        self.ui.authorEdit.setText("")
        self.ui.yearEdit.setText("")

from PySide6.QtWidgets import QApplication, QMainWindow
from ui.ui_bookentry import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def get_entry(self):
        entry_items = (self.ui.lineEdit.text(),
                       self.ui.lineEdit_2.text(),
                       self.ui.lineEdit_3.text(),
                       self.ui.comboBox.currentText(),
                       int(self.ui.spinBox.text()))
        return entry_items

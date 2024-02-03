from PySide6.QtWidgets import QApplication
from gui import MainWindow
from db.db_utils import run_db_commands, insert_entry, print_table
import sys

app = QApplication(sys.argv)
window = MainWindow()

def print_values():
    print(f'\n{window.ui.lineEdit.text()}')
    print(window.ui.lineEdit_2.text())
    print(window.ui.lineEdit_3.text())
    print(window.ui.comboBox.currentText())
    print(window.ui.spinBox.text())

def main_insert():
    insert_entry(window.get_entry())

def main():
    run_db_commands()
    # app = QApplication(sys.argv)

    # window = MainWindow()
    window.show()
    window.ui.pushButton.clicked.connect(main_insert)
    window.ui.pushButton_2.clicked.connect(print_table)
    sys.exit(app.exec())

if __name__ == '__main__':
    main()

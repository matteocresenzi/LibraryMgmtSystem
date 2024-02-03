from PySide6.QtWidgets import QApplication
from gui import MainWindow
from db.database import Database
import sys


def main():
    db = Database("bookDb")
    db.create_connection()
    db.check_database()
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == '__main__':
    main()

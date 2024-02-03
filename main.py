from PySide6.QtWidgets import QApplication
from gui import MainWindow
from db.database import Database
import sys


def main():

    # Create database bookDb
    db = Database("bookDb")
    db.create_connection()
    # Checks if DB is valid
    db.check_database()
    # Closes DB Connection
    # db.close_connection()

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == '__main__':
    main()

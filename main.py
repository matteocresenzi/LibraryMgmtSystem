from PySide6 import QtCore, QtGui, QtWidgets
from gui import MainWindow
import sys


def main():
    app = QtWidgets.QApplication([])

    widget = MainWindow()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())


if __name__ == '__main__':
    main()

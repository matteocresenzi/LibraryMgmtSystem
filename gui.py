from PySide6 import QtCore, QtGui, QtWidgets


class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.button = QtWidgets.QPushButton("Submit")
        self.text = QtWidgets.QLabel("What book would you like to enter?")
        self.text.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.entry = QtWidgets.QLineEdit()
        self.entry.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.entry)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.clicked)

    @QtCore.Slot()
    def clicked(self):
        self.text.setText("Clicked")

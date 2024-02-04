# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_book.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSlider,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.menuBar = QWidget(self.centralwidget)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 800, 40))
        self.menuBar.setLayoutDirection(Qt.LeftToRight)
        self.menuBar.setAutoFillBackground(True)
        self.homeButton = QPushButton(self.menuBar)
        self.homeButton.setObjectName(u"homeButton")
        self.homeButton.setGeometry(QRect(130, 5, 100, 30))
        self.homeButton.setLayoutDirection(Qt.LeftToRight)
        self.addButton = QPushButton(self.menuBar)
        self.addButton.setObjectName(u"addButton")
        self.addButton.setGeometry(QRect(240, 5, 100, 30))
        self.addButton.setLayoutDirection(Qt.LeftToRight)
        self.editButton = QPushButton(self.menuBar)
        self.editButton.setObjectName(u"editButton")
        self.editButton.setGeometry(QRect(350, 5, 100, 30))
        self.editButton.setLayoutDirection(Qt.LeftToRight)
        self.loanButton = QPushButton(self.menuBar)
        self.loanButton.setObjectName(u"loanButton")
        self.loanButton.setGeometry(QRect(460, 5, 100, 30))
        self.loanButton.setLayoutDirection(Qt.LeftToRight)
        self.visualizeButton = QPushButton(self.menuBar)
        self.visualizeButton.setObjectName(u"visualizeButton")
        self.visualizeButton.setGeometry(QRect(570, 5, 100, 30))
        self.visualizeButton.setLayoutDirection(Qt.LeftToRight)
        self.printButton = QPushButton(self.centralwidget)
        self.printButton.setObjectName(u"printButton")
        self.printButton.setGeometry(QRect(275, 470, 250, 30))
        self.printButton.setAutoFillBackground(False)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(353, 360, 94, 20))
        self.label_5.setScaledContents(False)
        self.label_5.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.titleEdit = QLineEdit(self.centralwidget)
        self.titleEdit.setObjectName(u"titleEdit")
        self.titleEdit.setGeometry(QRect(275, 140, 250, 30))
        self.titleEdit.setFocusPolicy(Qt.StrongFocus)
        self.titleEdit.setMaxLength(50)
        self.backButton = QPushButton(self.centralwidget)
        self.backButton.setObjectName(u"backButton")
        self.backButton.setGeometry(QRect(275, 440, 120, 30))
        self.backButton.setAutoFillBackground(False)
        self.authorEdit = QLineEdit(self.centralwidget)
        self.authorEdit.setObjectName(u"authorEdit")
        self.authorEdit.setGeometry(QRect(275, 200, 250, 30))
        self.authorEdit.setFocusPolicy(Qt.StrongFocus)
        self.authorEdit.setMaxLength(50)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(277, 240, 111, 20))
        self.label_3.setScaledContents(False)
        self.label_3.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.yearEdit = QLineEdit(self.centralwidget)
        self.yearEdit.setObjectName(u"yearEdit")
        self.yearEdit.setGeometry(QRect(275, 260, 250, 30))
        self.yearEdit.setFocusPolicy(Qt.StrongFocus)
        self.yearEdit.setMaxLength(5)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(277, 120, 51, 20))
        self.label.setScaledContents(False)
        self.label.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.genreBox = QComboBox(self.centralwidget)
        self.genreBox.addItem("")
        self.genreBox.addItem("")
        self.genreBox.addItem("")
        self.genreBox.setObjectName(u"genreBox")
        self.genreBox.setGeometry(QRect(272, 320, 262, 30))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(277, 180, 71, 20))
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(280, 300, 61, 21))
        self.label_4.setScaledContents(False)
        self.label_4.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.ratingSlider = QSlider(self.centralwidget)
        self.ratingSlider.setObjectName(u"ratingSlider")
        self.ratingSlider.setGeometry(QRect(287, 380, 225, 25))
        self.ratingSlider.setMinimum(1)
        self.ratingSlider.setMaximum(5)
        self.ratingSlider.setOrientation(Qt.Horizontal)
        self.ratingSlider.setTickPosition(QSlider.TicksAbove)
        self.ratingSlider.setTickInterval(1)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(272, 380, 16, 20))
        self.label_6.setScaledContents(False)
        self.label_6.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(520, 380, 16, 20))
        self.label_7.setScaledContents(False)
        self.label_7.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.submitButton = QPushButton(self.centralwidget)
        self.submitButton.setObjectName(u"submitButton")
        self.submitButton.setGeometry(QRect(405, 440, 120, 30))
        self.submitButton.setAutoFillBackground(False)
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(337, 90, 125, 20))
        font = QFont()
        font.setPointSize(24)
        self.label_8.setFont(font)
        self.label_8.setScaledContents(False)
        self.responseLabel = QLabel(self.centralwidget)
        self.responseLabel.setObjectName(u"responseLabel")
        self.responseLabel.setGeometry(QRect(200, 520, 400, 21))
        font1 = QFont()
        font1.setPointSize(20)
        self.responseLabel.setFont(font1)
        self.responseLabel.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.homeButton.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.addButton.setText(QCoreApplication.translate("MainWindow", u"Add Book", None))
        self.editButton.setText(QCoreApplication.translate("MainWindow", u"Edit Book", None))
        self.loanButton.setText(QCoreApplication.translate("MainWindow", u"Loans", None))
        self.visualizeButton.setText(QCoreApplication.translate("MainWindow", u"Visualize", None))
        self.printButton.setText(QCoreApplication.translate("MainWindow", u"Print Entry", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Personal Rating", None))
        self.titleEdit.setText("")
        self.backButton.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.authorEdit.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Publication Year", None))
        self.yearEdit.setInputMask("")
        self.yearEdit.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Title", None))
        self.genreBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Science Fiction", None))
        self.genreBox.setItemText(1, QCoreApplication.translate("MainWindow", u"History", None))
        self.genreBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Math", None))

        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Author", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Genre", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.submitButton.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Add a Book", None))
        self.responseLabel.setText("")
    # retranslateUi


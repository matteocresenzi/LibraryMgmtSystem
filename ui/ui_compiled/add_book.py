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
    QPushButton, QSizePolicy, QSlider, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(800, 560)
        self.label_8 = QLabel(Form)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(337, 70, 125, 20))
        font = QFont()
        font.setPointSize(24)
        self.label_8.setFont(font)
        self.label_8.setScaledContents(False)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(277, 100, 51, 20))
        self.label.setScaledContents(False)
        self.label.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(520, 360, 16, 20))
        self.label_7.setScaledContents(False)
        self.label_7.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.responseLabel = QLabel(Form)
        self.responseLabel.setObjectName(u"responseLabel")
        self.responseLabel.setGeometry(QRect(200, 500, 400, 20))
        font1 = QFont()
        font1.setPointSize(20)
        self.responseLabel.setFont(font1)
        self.responseLabel.setAlignment(Qt.AlignCenter)
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(280, 280, 61, 21))
        self.label_4.setScaledContents(False)
        self.label_4.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.titleEdit = QLineEdit(Form)
        self.titleEdit.setObjectName(u"titleEdit")
        self.titleEdit.setGeometry(QRect(275, 120, 250, 30))
        self.titleEdit.setFocusPolicy(Qt.StrongFocus)
        self.titleEdit.setMaxLength(50)
        self.printButton = QPushButton(Form)
        self.printButton.setObjectName(u"printButton")
        self.printButton.setGeometry(QRect(275, 450, 250, 30))
        self.printButton.setAutoFillBackground(False)
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(277, 220, 111, 20))
        self.label_3.setScaledContents(False)
        self.label_3.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(272, 360, 16, 20))
        self.label_6.setScaledContents(False)
        self.label_6.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(353, 340, 94, 20))
        self.label_5.setScaledContents(False)
        self.label_5.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.submitButton = QPushButton(Form)
        self.submitButton.setObjectName(u"submitButton")
        self.submitButton.setGeometry(QRect(405, 420, 120, 30))
        self.submitButton.setAutoFillBackground(False)
        self.yearEdit = QLineEdit(Form)
        self.yearEdit.setObjectName(u"yearEdit")
        self.yearEdit.setGeometry(QRect(275, 240, 250, 30))
        self.yearEdit.setFocusPolicy(Qt.StrongFocus)
        self.yearEdit.setMaxLength(5)
        self.ratingSlider = QSlider(Form)
        self.ratingSlider.setObjectName(u"ratingSlider")
        self.ratingSlider.setGeometry(QRect(287, 360, 225, 25))
        self.ratingSlider.setMinimum(1)
        self.ratingSlider.setMaximum(5)
        self.ratingSlider.setOrientation(Qt.Horizontal)
        self.ratingSlider.setTickPosition(QSlider.TicksAbove)
        self.ratingSlider.setTickInterval(1)
        self.backButton = QPushButton(Form)
        self.backButton.setObjectName(u"backButton")
        self.backButton.setGeometry(QRect(275, 420, 120, 30))
        self.backButton.setAutoFillBackground(False)
        self.genreBox = QComboBox(Form)
        self.genreBox.addItem("")
        self.genreBox.addItem("")
        self.genreBox.addItem("")
        self.genreBox.setObjectName(u"genreBox")
        self.genreBox.setGeometry(QRect(272, 300, 262, 30))
        self.authorEdit = QLineEdit(Form)
        self.authorEdit.setObjectName(u"authorEdit")
        self.authorEdit.setGeometry(QRect(275, 180, 250, 30))
        self.authorEdit.setFocusPolicy(Qt.StrongFocus)
        self.authorEdit.setMaxLength(50)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(277, 160, 71, 20))
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Add a Book", None))
        self.label.setText(QCoreApplication.translate("Form", u"Title", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"5", None))
        self.responseLabel.setText("")
        self.label_4.setText(QCoreApplication.translate("Form", u"Genre", None))
        self.titleEdit.setText("")
        self.printButton.setText(QCoreApplication.translate("Form", u"Print Entry", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Publication Year", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"1", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Personal Rating", None))
        self.submitButton.setText(QCoreApplication.translate("Form", u"Submit", None))
        self.yearEdit.setInputMask("")
        self.yearEdit.setText("")
        self.backButton.setText(QCoreApplication.translate("Form", u"Back", None))
        self.genreBox.setItemText(0, QCoreApplication.translate("Form", u"Science Fiction", None))
        self.genreBox.setItemText(1, QCoreApplication.translate("Form", u"History", None))
        self.genreBox.setItemText(2, QCoreApplication.translate("Form", u"Math", None))

        self.authorEdit.setText("")
        self.label_2.setText(QCoreApplication.translate("Form", u"Author", None))
    # retranslateUi


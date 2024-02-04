# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menu_bar.ui'
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
from PySide6.QtWidgets import (QApplication, QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(800, 40)
        self.menuBar = QWidget(Form)
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

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.homeButton.setText(QCoreApplication.translate("Form", u"Home", None))
        self.addButton.setText(QCoreApplication.translate("Form", u"Add Book", None))
        self.editButton.setText(QCoreApplication.translate("Form", u"Edit Book", None))
        self.loanButton.setText(QCoreApplication.translate("Form", u"Loans", None))
        self.visualizeButton.setText(QCoreApplication.translate("Form", u"Visualize", None))
    # retranslateUi


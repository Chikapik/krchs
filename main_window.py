# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(731, 187)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(731, 187))
        MainWindow.setMaximumSize(QtCore.QSize(731, 187))
        font = QtGui.QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 70, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.numberEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.numberEdit.setGeometry(QtCore.QRect(110, 70, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.numberEdit.setFont(font)
        self.numberEdit.setText("")
        self.numberEdit.setObjectName("numberEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(430, 70, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.spinBox_1 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_1.setGeometry(QtCore.QRect(380, 70, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spinBox_1.setFont(font)
        self.spinBox_1.setMinimum(2)
        self.spinBox_1.setMaximum(36)
        self.spinBox_1.setProperty("value", 10)
        self.spinBox_1.setObjectName("spinBox_1")
        self.spinBox_2 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_2.setGeometry(QtCore.QRect(490, 70, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spinBox_2.setFont(font)
        self.spinBox_2.setMinimum(2)
        self.spinBox_2.setMaximum(36)
        self.spinBox_2.setObjectName("spinBox_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(550, 70, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.convertButton = QtWidgets.QPushButton(self.centralwidget)
        self.convertButton.setGeometry(QtCore.QRect(600, 60, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.convertButton.setFont(font)
        self.convertButton.setObjectName("convertButton")
        self.answerLabel = QtWidgets.QLabel(self.centralwidget)
        self.answerLabel.setGeometry(QtCore.QRect(20, 120, 691, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.answerLabel.setFont(font)
        self.answerLabel.setText("")
        self.answerLabel.setObjectName("answerLabel")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(350, 70, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 20, 381, 21))
        self.label_6.setObjectName("label_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Преобразование в систему счисления"))
        self.label.setText(_translate("MainWindow", "Перевести"))
        self.label_2.setText(_translate("MainWindow", "-ной в"))
        self.label_3.setText(_translate("MainWindow", "-ную"))
        self.convertButton.setText(_translate("MainWindow", "Перевести"))
        self.label_5.setText(_translate("MainWindow", "из"))
        self.label_6.setText(_translate("MainWindow", "Перевод чисел в разные системы счисления:"))

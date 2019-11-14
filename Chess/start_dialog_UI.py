# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'start_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_StartDialog(object):
    def setupUi(self, StartDialog):
        StartDialog.setObjectName("StartDialog")
        StartDialog.resize(400, 100)
        self.horizontalLayoutWidget = QtWidgets.QWidget(StartDialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 381, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.create_new_game = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.create_new_game.sizePolicy().hasHeightForWidth())
        self.create_new_game.setSizePolicy(sizePolicy)
        self.create_new_game.setMinimumSize(QtCore.QSize(180, 60))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.create_new_game.setFont(font)
        self.create_new_game.setCheckable(False)
        self.create_new_game.setAutoExclusive(False)
        self.create_new_game.setObjectName("create_new_game")
        self.horizontalLayout.addWidget(self.create_new_game)
        self.load_game = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.load_game.sizePolicy().hasHeightForWidth())
        self.load_game.setSizePolicy(sizePolicy)
        self.load_game.setMinimumSize(QtCore.QSize(180, 60))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.load_game.setFont(font)
        self.load_game.setCheckable(False)
        self.load_game.setAutoExclusive(True)
        self.load_game.setObjectName("load_game")
        self.horizontalLayout.addWidget(self.load_game)

        self.retranslateUi(StartDialog)
        QtCore.QMetaObject.connectSlotsByName(StartDialog)

    def retranslateUi(self, StartDialog):
        _translate = QtCore.QCoreApplication.translate
        StartDialog.setWindowTitle(_translate("StartDialog", "Start"))
        self.create_new_game.setText(_translate("StartDialog", "Создать новую партию"))
        self.load_game.setText(_translate("StartDialog", "Загрузить старую партию"))

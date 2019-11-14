# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'promout_pawn_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PromoutPawnDialog(object):
    def setupUi(self, PromoutPawnDialog):
        PromoutPawnDialog.setObjectName("PromoutPawnDialog")
        PromoutPawnDialog.resize(392, 142)
        self.verticalLayoutWidget = QtWidgets.QWidget(PromoutPawnDialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 375, 121))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.button_queen = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_queen.sizePolicy().hasHeightForWidth())
        self.button_queen.setSizePolicy(sizePolicy)
        self.button_queen.setMinimumSize(QtCore.QSize(75, 75))
        self.button_queen.setText("")
        self.button_queen.setIconSize(QtCore.QSize(75, 75))
        self.button_queen.setObjectName("button_queen")
        self.horizontalLayout.addWidget(self.button_queen)
        self.button_bishop = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_bishop.sizePolicy().hasHeightForWidth())
        self.button_bishop.setSizePolicy(sizePolicy)
        self.button_bishop.setMinimumSize(QtCore.QSize(75, 75))
        self.button_bishop.setText("")
        self.button_bishop.setIconSize(QtCore.QSize(75, 75))
        self.button_bishop.setObjectName("button_bishop")
        self.horizontalLayout.addWidget(self.button_bishop)
        self.button_rook = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_rook.sizePolicy().hasHeightForWidth())
        self.button_rook.setSizePolicy(sizePolicy)
        self.button_rook.setMinimumSize(QtCore.QSize(75, 75))
        self.button_rook.setText("")
        self.button_rook.setIconSize(QtCore.QSize(75, 75))
        self.button_rook.setObjectName("button_rook")
        self.horizontalLayout.addWidget(self.button_rook)
        self.button_knight = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_knight.sizePolicy().hasHeightForWidth())
        self.button_knight.setSizePolicy(sizePolicy)
        self.button_knight.setMinimumSize(QtCore.QSize(75, 75))
        self.button_knight.setText("")
        self.button_knight.setIconSize(QtCore.QSize(75, 75))
        self.button_knight.setObjectName("button_knight")
        self.horizontalLayout.addWidget(self.button_knight)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(PromoutPawnDialog)
        QtCore.QMetaObject.connectSlotsByName(PromoutPawnDialog)

    def retranslateUi(self, PromoutPawnDialog):
        _translate = QtCore.QCoreApplication.translate
        PromoutPawnDialog.setWindowTitle(_translate("PromoutPawnDialog", "Выберете фигуру"))
        self.label.setText(_translate("PromoutPawnDialog", "Выберете фигуру:"))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'load_game_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoadGameDialog(object):
    def setupUi(self, LoadGameDialog):
        LoadGameDialog.setObjectName("LoadGameDialog")
        LoadGameDialog.resize(400, 242)
        self.tableWidget = QtWidgets.QTableWidget(LoadGameDialog)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 381, 221))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)

        self.retranslateUi(LoadGameDialog)
        QtCore.QMetaObject.connectSlotsByName(LoadGameDialog)

    def retranslateUi(self, LoadGameDialog):
        _translate = QtCore.QCoreApplication.translate
        LoadGameDialog.setWindowTitle(_translate("LoadGameDialog", "Выберите партию"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("LoadGameDialog", "Id"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("LoadGameDialog", "Player 1"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("LoadGameDialog", "Player 2"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("LoadGameDialog", "Winner"))

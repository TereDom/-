import sqlite3
from PyQt5.QtWidgets import QDialog, QTableWidget, QTableWidgetItem

from load_game_dialog_UI import Ui_LoadGameDialog


class LoadGameDialog(QDialog, Ui_LoadGameDialog):
    def __init__(self, main_window):
        QDialog.__init__(self)
        self.setupUi(self)
        self.main_window = main_window

        con = sqlite3.connect("Chess.db")
        cur = con.cursor().execute("""SELECT id, white, black, date, winner FROM Games
            WHERE id > 0""")

        self.tableWidget.setColumnCount(5)
        counter = 0
        result = list(cur)
        self.tableWidget.setRowCount(len(result))
        for i in result:
            a, b, c, d, e = i
            self.tableWidget.setItem(counter, 0, QTableWidgetItem(str(a)))
            self.tableWidget.setItem(counter, 1, QTableWidgetItem(str(b)))
            self.tableWidget.setItem(counter, 2, QTableWidgetItem(str(c)))
            self.tableWidget.setItem(counter, 3, QTableWidgetItem(str(d)))
            self.tableWidget.setItem(counter, 4, QTableWidgetItem(str(e)))
            self.tableWidget.resizeColumnsToContents()
            counter += 1

        self.tableWidget.itemClicked.connect(self.choose)
        self.main_window.load_result = "exit"

    def choose(self, item):
        self.main_window.load_result = item.text()
        self.close()
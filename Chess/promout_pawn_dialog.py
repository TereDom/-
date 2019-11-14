from PyQt5.QtWidgets import QDialog
from PyQt5.QtGui import QIcon

from Classes import *
from promout_pawn_dialog_UI import Ui_PromoutPawnDialog


class PromoutPawnDialog(QDialog, Ui_PromoutPawnDialog):
    def __init__(self, main_window):
        QDialog.__init__(self)
        self.setupUi(self)
        self.main_window = main_window

        self.button_bishop.setIcon(QIcon("img\\Bishop.png"))
        self.button_knight.setIcon(QIcon("img\\Knight.png"))
        self.button_queen.setIcon(QIcon("img\\Queen.png"))
        self.button_rook.setIcon(QIcon("img\\Rook.png"))

        self.button_bishop.clicked.connect(self.f_bishop)
        self.button_knight.clicked.connect(self.f_knight)
        self.button_queen.clicked.connect(self.f_queen)
        self.button_rook.clicked.connect(self.f_rook)

    def f_bishop(self):
        self.main_window.promout = Bishop
        self.close()

    def f_knight(self):
        self.main_window.promout = Knight
        self.close()

    def f_queen(self):
        self.main_window.promout = Queen
        self.close()

    def f_rook(self):
        self.main_window.promout = Rook
        self.close()

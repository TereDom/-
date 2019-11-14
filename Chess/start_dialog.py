from PyQt5.QtWidgets import QDialog

from start_dialog_UI import Ui_StartDialog


class StartDialog(QDialog, Ui_StartDialog):
    def __init__(self, main_window):
        QDialog.__init__(self)
        self.setupUi(self)
        self.main_window = main_window

        self.create_new_game.clicked.connect(self.new)
        self.load_game.clicked.connect(self.load)
        self.main_window.result = "exit"

    def new(self):
        self.main_window.result = "new"
        self.close()

    def load(self):
        self.main_window.result = "load"
        self.close()

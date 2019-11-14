import sys
import datetime

import sqlite3
from PyQt5.Qt import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication

from main_window_UI import Ui_MainWindow
from load_game_dialog import LoadGameDialog
from create_new_game_dialog import CreateNewGameDialog
from promout_pawn_dialog import PromoutPawnDialog
from start_dialog import StartDialog
from Classes import *


letters = {1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F", 7: "G", 8: "H"}


class Chess(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.area.setPixmap(QPixmap("img\\Big_area.png"))
        self.area_2.setPixmap(QPixmap("img\\Big_area.png"))
        self.result = None
        self.promout_color = None
        self.first_player_color = None
        self.field = None
        self.promout = None
        self.promout_coords = None
        self.fields = list()
        self.moves = list()
        self.leave.clicked.connect(self.f_leave)
        self.exit.clicked.connect(self.f_exit)
        self.next.clicked.connect(self.f_next)
        self.back.clicked.connect(self.f_back)
        self.return_to_menu.clicked.connect(self.f_menu)
        self.setup_info()

    def load_pieces(self):
        for i in range(8):
            for j in range(8):
                if self.board.color == WHITE:
                    if self.board.field[i][j] is not None:
                        eval(f"self.{letters[7 - j + 1]}{i + 1}.setPixmap(QPixmap(self.board.field[i][j].get_big_image()))")
                    else:
                        eval(f"self.{letters[7 - j + 1]}{i + 1}.setPixmap(QPixmap('img\\Big_none.png'))")
                    self.label_A.setText("8")
                    self.label_B.setText("7")
                    self.label_C.setText("6")
                    self.label_D.setText("5")
                    self.label_E.setText("4")
                    self.label_F.setText("3")
                    self.label_G.setText("2")
                    self.label_H.setText("1")
                    self.label_1.setText("A")
                    self.label_2.setText("B")
                    self.label_3.setText("C")
                    self.label_4.setText("D")
                    self.label_5.setText("E")
                    self.label_6.setText("F")
                    self.label_7.setText("G")
                    self.label_8.setText("H")
                else:
                    if self.board.field[i][j] is not None:
                        eval(
                            f"self.{letters[j + 1]}{7 - i + 1}.setPixmap(QPixmap(self.board.field[i][j].get_big_image()))")
                    else:
                        eval(f"self.{letters[j + 1]}{7 - i + 1}.setPixmap(QPixmap('img\\Big_none.png'))")
                    self.label_A.setText("1")
                    self.label_B.setText("2")
                    self.label_C.setText("3")
                    self.label_D.setText("4")
                    self.label_E.setText("5")
                    self.label_F.setText("6")
                    self.label_G.setText("7")
                    self.label_H.setText("8")
                    self.label_1.setText("H")
                    self.label_2.setText("G")
                    self.label_3.setText("F")
                    self.label_4.setText("E")
                    self.label_5.setText("D")
                    self.label_6.setText("C")
                    self.label_7.setText("B")
                    self.label_8.setText("A")

    def choose_piece(self, x, y):
        self.board.choose_piece(x, y)
        self.load_pieces()

    def f_leave(self):
        self.board.set_winner(self.board.color)
        self.player_move.setText(f"Победил {self.first_player_name if self.board.winner == WHITE else self.second_player_name}")

    def f_exit(self):
        self.close()

    def f_next(self):
        if self.counter < len(self.fields) - 1:
            self.counter += 1
            self.load_pieces_for_history(eval(self.fields[self.counter]))

    def f_back(self):
        if self.counter > 0:
            self.counter -= 1
            self.load_pieces_for_history(eval(self.fields[self.counter]))

    def f_menu(self):
        self.close()
        self.setup_info()

    def load_pieces_for_history(self, field):
        for i in range(8):
            for j in range(8):
                if field[i][j] is not None:
                    eval(f"self.{letters[i + 1]}{j + 1}_2.setPixmap(QPixmap(field[i][j].get_big_image()))")
                else:
                    eval(f"self.{letters[i + 1]}{j + 1}_2.setPixmap(QPixmap('img\\Big_none.png'))")

    def mousePressEvent(self, event):
        if self.board.complited:
            return
        x, y = event.x(), event.y()
        x, y, = (x - 82) // 60, (y - 42) // 60
        if 0 <= x <= 7 and 0 <= y <= 7:
            if self.board.color == WHITE:
                x, y = 7 - y, x
            else:
                x, y = y, 7 - x
            self.choose_piece(x, y)
            if self.board.piece is not None:
                self.move = (f"{self.first_player_name if self.board.color == WHITE else self.second_player_name}:\t" +\
                            f"{letters[self.board.piece.get_y() + 1]}{self.board.piece.get_x() + 1} move ")
                self.choose_piece_text.setText("Выбранная фигура: " +
                                               f"{letters[self.board.piece.get_y() + 1]}{self.board.piece.get_x() + 1}")
            else:
                self.choose_piece_text.setText("Фигура не выбрана")

            if self.board.get_player_color() == WHITE:
                self.player_move.setText(f"Ходит: {self.first_player_name}")
            else:
                self.player_move.setText(f"Ходит: {self.second_player_name}")
            if self.board.complited:
                self.player_move.setText(f"Победил {self.first_player_name if self.board.winner == WHITE else self.second_player_name}")

            for i in range(8):
                piece = self.board.field[i][0]
                if piece.__class__ == Pawn:
                    if piece.get_color() == BLACK:
                        PromoutPawnDialog(self).exec()
                        self.promout_coords, self.promout_color = piece.get_coords(), piece.get_color()
                        break
                piece = self.board.field[i][7]
                if piece.__class__ == Pawn:
                    if piece.get_color() == WHITE:
                        PromoutPawnDialog(self).exec()
                        self.promout_coords, self.promout_color = piece.get_coords(), piece.get_color()
                        break
            if self.promout is not None:
                x, y = self.promout_coords
                self.board.field[y][x] = self.promout(x, y, self.promout_color)
                self.promout = None
                self.promout_color = None
                self.promout_coords = None
        self.load_pieces()
        if self.board.get_str_field() != self.fields[-1]:
            self.fields.append(self.board.get_str_field())
            self.counter = len(self.fields) - 1
            self.load_pieces_for_history(eval(self.fields[self.counter]))
            self.move += f"{letters[y + 1]}{x + 1}"
            self.moves.append(self.move)
            self.list_moves.addItem(self.move)
            self.move = ""
        self.update_datebase()

    def update_datebase(self, new=False):
        now = datetime.datetime.now()
        time = now.strftime("%d.%m.%Y %H:%M")
        if new:
            result = self.cur.execute(f"""select id from Games""")
            result_n = list()
            for i in result:
                result_n.append(*i)
            if result_n == []:
                result_n.append(0)
            self.id = max(result_n) + 1
            comand = (f'INSERT INTO Games(id,date,white,black,fields,moves,winner,complited,current_move_color)' +
                      f' VALUES({self.id},"{time}","{self.first_player_name}","{self.second_player_name}","{str(self.fields)}",' +
                      f'"{str(self.moves)}","None","False","{self.board.get_player_color()}")')
            self.cur.execute(comand)
            self.con.commit()
        else:
            comand = f'''update Games
    set date = "{time}", fields = "{self.fields}", moves = "{self.moves}", current_move_color = "{self.board.get_player_color()}"
where id = {self.id}'''
            self.cur.execute(comand)
            self.con.commit()

    def setup_info(self, field=False):
        if field:
            CreateNewGameDialog(self, self.field).exec()
            if self.new_result == "exit":
                self.setup_info()
                return
        else:
            StartDialog(self).exec()
            now = datetime.datetime.now()
            time = now.strftime("%d.%m.%Y   %H:%M")
            self.con = sqlite3.connect("Chess.db")
            self.cur = self.con.cursor()
            if self.result == "new":
                CreateNewGameDialog(self).exec()
                if self.new_result == "exit":
                    self.setup_info()
                    return
                counter_kings = 0
                for i in range(8):
                    for j in range(8):
                        if self.field[i][j].__class__ == King:
                            counter_kings += 1
                if counter_kings != 2:
                    self.setup_info(field=True)
                    return
                self.board = Board(self.field, self.first_player_color)
                self.fields.append(self.board.get_str_field())
                self.counter = len(self.fields) - 1
                self.load_pieces_for_history(eval(f"{self.fields[self.counter]}"))
                self.update_datebase(new=True)
                self.con.commit()

            elif self.result == "load":
                LoadGameDialog(self).exec()
                if self.load_result == "exit":
                    self.setup_info()
                    return
                result = self.cur.execute(f"""select white, black, fields, moves, current_move_color from Games
                    where id = {int(self.load_result)}""")
                self.id = int(self.load_result)
                for i in result:
                    self.first_player_name, self.second_player_name, self.fields, self.moves, self.color = i
                    self.fields = eval(self.fields)
                    self.moves = eval(self.moves)
                self.counter = len(self.fields) - 1
                self.load_pieces_for_history(eval(self.fields[self.counter]))
                self.board = Board(eval(self.fields[-1]), self.color)
            elif self.result == "exit":
                return
            if self.result != "exit":
                if self.board.get_player_color() == WHITE:
                    self.player_move.setText(f"Ходит: {self.first_player_name}")
                else:
                    self.player_move.setText(f"Ходит: {self.second_player_name}")
                self.load_pieces()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Chess()
    ex.show()
    sys.exit(app.exec())

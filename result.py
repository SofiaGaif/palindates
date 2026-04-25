from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout,
    QHBoxLayout, QLabel, QPushButton,
    QMessageBox, QTextEdit)
import txt
from logic import *

class ResultWin(QWidget):
    def __init__(self, y1, y2, mw):
        super().__init__()
        self.y1 = y1
        self.y2 = y2
        self.mw = mw
        self.set_appear()
        self.count_dates()
        self.initUI()
        self.connects()

    def set_appear(self):
        self.setWindowTitle(txt.result)
        self.resize(1300, 910)
        with open('assets/style.qss', 'r') as f:
            self.setStyleSheet(f.read())

    def initUI(self):
        # Текст "Все даты-палиндромы с ГГГГ по ГГГГ года:"
        title = txt.range_[0] + str(self.y1) + txt.range_[1] + str(self.y2) + txt.range_[2]
        self.title = QLabel(title)
        self.title.setWordWrap(True)
        self.title.setAlignment(Qt.AlignCenter)

        # Поле с результатом и кол-во дат-палиндромов
        self.date_list = QTextEdit(self.res)
        self.date_list.setReadOnly(True)
        self.count_res = QLabel(self.count_res)
        self.count_res.setAlignment(Qt.AlignCenter)

        # Кнопка "Выбрать новый промежуток"
        self.back_btn = QPushButton(txt.back_btn)

        # Стиль
        self.count_res.setProperty('class', 'hint')
        self.title.setProperty('class', 'h2')
        self.date_list.setProperty('class', 'small')

        # Лейауты
        self.vlt = QVBoxLayout()
        self.vlt.addWidget(self.title)
        self.vlt.addWidget(self.date_list)
        self.vlt.addWidget(self.count_res)
        self.vlt.addWidget(self.back_btn)
        self.setLayout(self.vlt)

    def prev_win(self):
        self.hide()
        self.mw.show()

    def connects(self):
        self.back_btn.clicked.connect(self.prev_win)
    
    def count_dates(self):
        self.palindromes = palindrome(self.y1, self.y2)
        if self.palindromes == []:
            self.res = txt.dates_not_found
            self.count_res = txt.count_res[2]
        else:
            self.res = ' '.join(self.palindromes)
            self.count_res = txt.count_res[0] + str(len(self.palindromes)) + txt.count_res[1]
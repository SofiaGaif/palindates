from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QMessageBox)
from PyQt5.QtGui import QFontDatabase, QIntValidator
from result import ResultWin
import txt

class StartWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    
    def set_appear(self):
        self.setWindowTitle(txt.title)
        self.resize(1300, 910)
        QFontDatabase.addApplicationFont('assets/fonts/Nunito-ExtraBold.ttf')
        QFontDatabase.addApplicationFont('assets/fonts/Nunito-Regular.ttf')
        with open('assets/style.qss', 'r') as f:
            self.setStyleSheet(f.read())
    
    def initUI(self):
        # Заголовок и кнопка "?"
        self.title = QLabel(txt.title)
        self.help_btn = QPushButton('?')

        # Подсказка
        self.hint = QLabel(txt.hint)
        self.hint.setAlignment(Qt.AlignCenter)

        # Текст "С ГГГГ по ГГГГ"
        validator = QIntValidator(0, 9999)
        self.y1_str = QLabel(txt.years[0])
        self.y1 = QLineEdit()
        self.y1.setPlaceholderText(txt.years[1])
        self.y1.setValidator(validator)
        self.y1.setAlignment(Qt.AlignCenter)
        self.y2_str = QLabel(txt.years[2])
        self.y2 = QLineEdit()
        self.y2.setPlaceholderText(txt.years[1])
        self.y2.setValidator(validator)
        self.y2.setAlignment(Qt.AlignCenter)

        # Пример
        self.eg = QLabel(txt.eg)
        self.eg.setAlignment(Qt.AlignCenter)

        # Кнопка "Посчитать"
        self.count_btn = QPushButton(txt.count_btn)

        # Окно ошибки
        self.warn_win = QMessageBox()
        self.warn_win.setWindowTitle(txt.error)

        # Стиль
        self.title.setProperty('class', 'h1')
        self.eg.setProperty('class', 'hint')
        self.help_btn.setObjectName('help-btn')
        self.count_btn.setObjectName('count-btn')
        self.y1_str.setProperty('class', 'h2')
        self.y2_str.setProperty('class', 'h2')
        self.y1.setProperty('class', 'input')
        self.y2.setProperty('class', 'input')

        # Лейауты
        self.vlt = QVBoxLayout()
        self.hlt1 = QHBoxLayout()
        self.hlt2 = QHBoxLayout()
        self.hlt3 = QHBoxLayout()
        self.hlt4 = QHBoxLayout()
        self.hlt5 = QHBoxLayout()

        self.hlt1.addStretch(1)
        self.hlt1.addWidget(self.title)
        self.hlt1.addWidget(self.help_btn)
        self.hlt1.addStretch(1)
        self.hlt2.addWidget(self.hint)

        self.hlt3.addStretch(1)
        self.hlt3.addWidget(self.y1_str, alignment=Qt.AlignCenter)
        self.hlt3.addWidget(self.y1, alignment=Qt.AlignCenter)
        self.hlt3.addWidget(self.y2_str, alignment=Qt.AlignCenter)
        self.hlt3.addWidget(self.y2, alignment=Qt.AlignCenter)
        self.hlt3.addStretch(1)
        
        self.hlt4.addWidget(self.eg, alignment=Qt.AlignCenter)
        self.hlt5.addWidget(self.count_btn, alignment=Qt.AlignCenter)

        self.vlt.addStretch(2)
        self.vlt.addLayout(self.hlt1)
        self.vlt.addStretch(1)
        self.vlt.addLayout(self.hlt2)
        self.vlt.addLayout(self.hlt3)
        self.vlt.addLayout(self.hlt4)
        self.vlt.addStretch(1)
        self.vlt.addLayout(self.hlt5)
        self.vlt.addStretch(2)
        self.setLayout(self.vlt)
    
    def next_win(self):
        try:
            start_year = int(self.y1.text())
            end_year = int(self.y2.text())
            if start_year >= end_year:
                self.warn_win.setText(txt.error_big_small)
                self.warn_win.show()
                self.warn_win.exec_()
            else:
                self.hide()
                self.second_win = ResultWin(start_year, end_year, self)
                self.second_win.show()
        except ValueError:
            self.warn_win.setText(txt.error_none)
            self.warn_win.show()
            self.warn_win.exec_()

    def help_win(self):
        self.help_msg = QMessageBox()
        self.help_msg.setWindowTitle(txt.help_title)
        self.help_msg.setText(txt.help_desc)
        self.help_msg.show()
        self.help_msg.exec_()
    
    def connects(self):
        self.count_btn.clicked.connect(self.next_win)
        self.help_btn.clicked.connect(self.help_win)

app = QApplication([])
mw = StartWin()
app.exec_()
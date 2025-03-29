from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
months = {
    '01':31,'02':29,
    '03':31,'04':30,
    '05':31,'06':30,
    '07':31,'08':31,
    '09':30,'10':31,
    '11':30,'12':31
}
def palindrome():
    begin = int(y1.text())
    end = int(y2.text())
    leaps = leap_years(begin, end)
    palindromes = list()
    for year in range(begin, end+1):
        date = str(year)[::-1]
        if existing(leaps, year, date) == True:
            palindromes.append(str(date[:2])+'.'+str(date[2:])+'.'+str(year))
    msg_dates(palindromes, begin, end)
def leap_years(y1, y2):
    leaps = list()
    for year in range(y1, y2+1):
        if (year%400==0) or (year%4==0 and year%100!=0):
            leaps.append(year)
    return leaps
def existing(leaps, year, date):
    if year in leaps:
        months['02'] = 29
    else:
        months['02'] = 28
    if len(date) == 4:
        day_str = date[:2]
        month_str = date[2:]
        day = int(day_str)
        month = int(month_str)
        if (1<=month<=12) and (1<=day<=months[month_str]):
            return True
    return False
def msg_dates(palindromes, y1, y2):
    message = 'Даты-палиндромы с '+str(y1)+' по '+str(y2)+': '+', '.join(palindromes)+'.'
    msg = QMessageBox(text=message)
    msg.setWindowTitle('Результат: '+str(len(palindromes))+' шт.')
    msg.setStyleSheet('font-size: 12pt')
    msg.show()
    msg.exec_()
app = QApplication([])
my_win = QWidget()
my_win.setStyleSheet('font-size: 15pt')
my_win.setWindowTitle('Даты-палиндромы')
my_win.resize(800, 700)
text = QLabel('Если записать все цифры даты 10 января 1001 года подряд, получится число 10011001, которое читается одинаково слева направо и справа налево. Такие числа называются палиндромами.')
text.setWordWrap(True)
descr = QLabel('Введите два года, в промежутке которых вы хотите найти даты-палиндромы')
y1_str = QLabel('С')
y1 = QLineEdit('2001')
y2_str = QLabel('по')
y2 = QLineEdit('2100')
start = QPushButton(text='Посчитать')
start.clicked.connect(palindrome)
vLayout = QVBoxLayout()
hLayout1 = QHBoxLayout()
hLayout2 = QHBoxLayout()
hLayout3 = QHBoxLayout()
hLayout4 = QHBoxLayout()
hLayout1.addWidget(text)
hLayout2.addWidget(descr, alignment=Qt.AlignCenter)
hLayout3.addWidget(y1_str, alignment=Qt.AlignCenter)
hLayout3.addWidget(y1, alignment=Qt.AlignCenter)
hLayout3.addWidget(y2_str, alignment=Qt.AlignCenter)
hLayout3.addWidget(y2, alignment=Qt.AlignCenter)
hLayout4.addWidget(start, alignment=Qt.AlignCenter)
vLayout.addLayout(hLayout1)
vLayout.addLayout(hLayout2)
vLayout.addLayout(hLayout3)
vLayout.addLayout(hLayout4)
my_win.setLayout(vLayout)
my_win.show()
app.exec_()
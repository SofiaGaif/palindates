months = {
    '01':31,'02':29,
    '03':31,'04':30,
    '05':31,'06':30,
    '07':31,'08':31,
    '09':30,'10':31,
    '11':30,'12':31
}

def palindrome(y1, y2): # Поиск палиндромов
    leaps = leap_years(y1, y2)
    palindromes = list()
    for year in range(y1, y2+1):
        date = str(year)[::-1]
        if existing(leaps, year, date) == True:
            palindromes.append(str(date[:2])+'.'+str(date[2:])+'.'+str(year))
    return palindromes

def leap_years(y1, y2): # Вычисление високосных годов
    leaps = list()
    for year in range(y1, y2+1):
        if (year%400==0) or (year%4==0 and year%100!=0):
            leaps.append(year)
    return leaps

def existing(leaps, year, date): # Проверка существования даты
    if year in leaps: # Вычисление кол-ва дней в феврале
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
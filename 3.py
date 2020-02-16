from enum import Enum
class month(Enum):
    January = 1
    February = 2
    March = 3
    April = 4
    May = 5
    June = 6
    July = 7
    August = 8
    September = 9
    October = 10
    November = 11
    December = 12
class season(Enum):
    Winter = 1
    Spring = 2
    Summer = 3
    Autumn = 4
while True:
    while True:
        try:
            s = month[input('month:')]
            break
        except KeyError:
            print('Введіть назву місяця англійською')

    if month == month.December or month.January or month.February:
            print(season.Winter)
    elif month == month.March or month.April or month.May:
            print(season.Spring)
    elif month == month.June or month.July or month.August:
            print(season.Summer)
    elif month == month.September or month.October or month.November:
            print(season.Autumn)

    answer = input("Запустити ще? якщо так - 1, ні - інше")
    if answer == '1':
        continue
    else:
        break

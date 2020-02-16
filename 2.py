from enum import Enum
class converter(Enum):
    USD = 1
    EUR = 2
    CZK = 3
    PLN = 4

while True:
    while True:
        try:
            x = float(input('amount of money : '))
            break
        except ValueError:
            print('Тільки числа!')

    while True:
        try:
            p = converter[input('currency : ')]
            break
        except KeyError:
            print('Введіть назву валюти англійською, і великими буквами!')

    if p == converter.USD:
        x *= 24.43
        print(x)
    elif p == converter.EUR:
        x *= 26.62
        print(x)
    elif p == converter.CZK:
        x *= 1.06
        print(x)
    elif p == converter.PLN:
        x *= 6.25
        print(x)

    answer = input("Запустити ще? якщо так - 1, ні - інше")
    if answer == '1':
        continue
    else:
        break

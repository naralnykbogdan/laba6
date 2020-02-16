while True:
    while True:
        try:
            days = range(1, 32)
            mounths = range(1, 13)
            years = range(1901, 2020)
            d, m, y = int(input('day:')), \
            int(input('mounth:')), \
            int(input('year:'))
            break
        except ValueError:
            print('Тільки числа')

#Наступний день
    if d in days:
        if m in mounths:
            if y in years:
                if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
                    if d == 31:
                        if m == 12:
                            d1 = 1
                            m1 = 1
                            y1 = y + 1
                            print(f'Дата наступного дня {d1}.{m1}.{y1}')
                        else:
                            d1 = 1
                            m1 = m + 1
                            y1 = y
                            print(f'Дата наступного дня {d1}.{m1}.{y1}')
                    else:
                        d1 = d+1
                        m1 = m
                        y1 = y
                        print(f'Дата наступного дня {d1}.{m1}.{y1}')
                elif m == 4 or m == 6 or m == 9 or m == 11:
                    if 0 < d < 31:
                        if d == 30:
                            d1 = 1
                            m1 = m + 1
                            y1 = y
                            print(f'Дата наступного дня {d1}.{m1}.{y1}')
                        else:
                            d1 = d+1
                            m1 = m
                            y1 = y
                            print(f'Дата наступного дня {d1}.{m1}.{y1}')
                    else:
                        print('Неправильна умова')
                elif m == 2:
                    if y % 4 == 0:
                        if 0 < d < 30:
                            if d == 29:
                                d1 = 1
                                m1 = 3
                                y1 = y
                                print(f'Дата наступного дня {d1}.{m1}.{y1}')
                            else:
                                d1 = d + 1
                                m1 = m
                                y1 = y
                                print(f'Дата наступного дня {d1}.{m1}.{y1}')
                        
    answer = input("Запустити ще? Якщо так - 1, ні - інше")
    if answer == '1':
        continue
    else:
        break
    

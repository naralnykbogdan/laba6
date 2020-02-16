while True:
    while True:
        try:
            t = int(input('Час='))
            break
        except ValueError:
            print('Тільки числа')

    if t % 6 == 1 or t % 6 == 2 or t % 6 == 3:
        print("Зелений")
    elif t % 6 == 4:
        print("Жовтий")
    elif t % 6 == 5 or t % 6 == 0:
        print("Червоний")

    answer = input("Запустити ще? якщо так - 1, ні - інше")
    if answer == '1':
        continue
    else:
        break

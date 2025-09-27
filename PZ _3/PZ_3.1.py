try:
    a, b, c = int(input("Введите первое число: ")), int(input("Введите второе число: ")), int(input('Введите третье число: '))
    if a + b == 0 or a + c == 0 or b + c == 0:
        print("Есть взаимнопротивоположные числа")
except ValueError:
    print('Ошибка!')
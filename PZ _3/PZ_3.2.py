try:
    a, b = int(input('Введите первое число: ')), int(input('Введите второе число ')) #запрос чисел
    if a > b: #проверка какое число больше
        print(a, b)
    elif b > a:
        print(b, a)
    else: #если числа равны
        print('Числа равны!')
except ValueError:
    print('Ошибка!')
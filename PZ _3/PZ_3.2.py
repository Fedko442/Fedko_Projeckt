try:
    a, b = int(input('Введите первое число: ')), int(input('Введите второе число '))
    if a > b:
        print(a, b)
    elif b > a:
        print(b, a)
    else:
        print('Ошибка!')
except ValueError:
    print('Ошибка!')
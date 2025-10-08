#Дано вещественное число Х и целое число N (> 0). Найти значение выражения 1 X2/(2!) + X4/(4!) - . + (-1)N-X2*N/((2-N)!) (N! 12 ...N). Полученное число является приближенным значением функции cos в точке Х.

import math
try:
    x = float(input("Введите вещественное число X: "))
    N = int(input("Введите целое число N (>0): "))
    x = x % (2 * math.pi)
    
    result = 0
    
    for n in range(N + 1):
        term = ((-1) ** n) * (x ** (2 * n)) / math.factorial(2 * n)
        result += term
        
        print(f" cos({x}) рядом Тейлора до {N}-го члена: {result}")
        print(f"Точное значение math.cos({x}): {math.cos(x)}")
except ValueError:
    print('Ошибка!')

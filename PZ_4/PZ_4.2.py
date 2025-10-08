#Дано целое число N (> 0). Найти сумму 1^1 + 2^2 + ... + N^n

try:
    n = int(input('Введите n число '))
    if n <= 0:
        print("Ошибка: n должно быть больше 0")
    else:
        result = sum(i**i for i in range(1, n + 1))
        print(result)
except ValueError:
    print("Ошибка!")

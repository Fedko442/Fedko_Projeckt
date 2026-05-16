#Дана последовательность из n целых элементов.
#В первой половине последовательности найти количество положительных элементов.

from functools import reduce

n = int(input("Введите количество элементов: "))

numbers = list(map(int, input("Введите элементы через пробел: ").split()))

# Первая половина последовательности
first_half = numbers[:n // 2]

# Подсчет положительных элементов
positive_count = reduce(
    lambda acc, x: acc + 1 if x > 0 else acc,
    first_half,
    0
)

print("Количество положительных элементов:", positive_count)
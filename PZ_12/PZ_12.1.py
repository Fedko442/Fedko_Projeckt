#Дана матрица размером 4×4, заполненная случайными целыми числами. 
#Найти сумму элементов первых двух строк матрицы.

from random import randint

matrix = [[randint(1, 100) for _ in range(4)] for _ in range(4)]

print("Матрица:")
for row in matrix:
    print(row)

sum_first_two = sum(sum(row) for row in matrix[:2])

print("Сумма элементов первых двух строк:", sum_first_two)
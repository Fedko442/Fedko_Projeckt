#Дана матрица размером 4×4, заполненная случайными целыми числами. 
#Найти минимальный и максимальный элементы матрицы.

from random import randint

matrix = [[randint(1, 100) for _ in range(4)] for _ in range(4)]

print("Матрица:")
for row in matrix:
    print(row)

min_elem = min(min(row) for row in matrix)
max_elem = max(max(row) for row in matrix)

print("Минимальный элемент:", min_elem)
print("Максимальный элемент:", max_elem)
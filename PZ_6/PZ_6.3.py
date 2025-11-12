#Дан список размера N, все элементы которого, кроме одного, упорядочены по убыванию. 
#Сделать список упорядоченным, переместив элемент, нарушающий упорядоченность, на новую позицию.

import random

N = int(input("Введите количество элементов: "))

if N <= 0:
    print("Ошибка!")

List = [random.randint(1,100) for _ in range(N)]

lst = List.copy()

lst.sort()

lst.reverse()

print(List)
print(lst)
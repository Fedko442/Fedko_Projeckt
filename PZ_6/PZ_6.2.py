import random
#Дан целочисленный список размера N. Найти максимальное количество его одинаковых элементов.

N = int(input('Введите количество элементов: '))

List = [random.randint(1, 5) for _ in range(N)]

max_count = 0

for i in List:
    count = List.count(i)
    if count > max_count:
        max_count = count
        num = i

print(f"Колличество повторений = {max_count}, Какое число воторяется больше всего = {num}")
print(List)
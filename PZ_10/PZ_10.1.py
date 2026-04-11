#1. Средствами языка Python сформировать текстовый файл (.txt), содержащий
#последовательность из целых положительных и отрицательных чисел. Сформировать
#новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
#обработку элементов:
#Исходные данные:
#Количество элементов:
#Элементы в обратном порядке:
#Сумма элементов последней половины:

# Исходный список чисел
numbers = [5, -3, 8, -1, 10, -7, 4, -2]

# 1. Создаем исходный файл
with open("numbers.txt", "w", encoding="utf-8") as file:
    for num in numbers:
        file.write(str(num) + " ")

# 2. Читаем данные из файла
with open("numbers.txt", "r", encoding="utf-8") as file:
    data = file.read().split()

# Преобразуем строки в числа
nums = [int(x) for x in data]

# 3. Обработка
count = len(nums)
reverse_nums = nums[::-1]

# Последняя половина
half_index = count // 2
last_half = nums[half_index:]
sum_last_half = sum(last_half)

# 4. Записываем результат в новый файл
with open("result1.txt", "w", encoding="utf-8") as file:
    file.write("Исходные данные:\n")
    file.write(" ".join(map(str, nums)) + "\n")
    file.write("Количество элементов: " + str(count) + "\n")
    file.write("Элементы в обратном порядке:\n")
    file.write(" ".join(map(str, reverse_nums)) + "\n")
    file.write("Сумма элементов последней половины: " + str(sum_last_half) + "\n")

print("Задание 1 выполнено. Результат записан в файл result1.txt")
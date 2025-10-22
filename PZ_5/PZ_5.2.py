#Напишите функцию digit_count_sum(k), которая принимает целое положительное число k и выводит на экран:
def digit_count_sum(k):
    s = str(k)
    count = len(s)
    total = 0
    for char in s:
        total += int(char)
    print(f"Число: {k}, количество цифр: {count}, сумма цифр: {total}")

# Проверка для пяти чисел
numbers = [123, 4567, 89, 1000, 7]
for n in numbers:
    digit_count_sum(n)
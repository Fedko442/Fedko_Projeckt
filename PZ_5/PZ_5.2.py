def digit_count_sum(k):
    count = 0
    total = 0
    temp = k
    while temp > 0:
        total += temp % 10
        temp //= 10
        count += 1
    print(f"Число: {k}, количество цифр: {count}, сумма цифр: {total}")

# Проверка:
numbers = [123, 4567, 89, 1000, 7]
for n in numbers:
    digit_count_sum(n)
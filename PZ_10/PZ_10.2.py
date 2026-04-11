# Из предложенного текстового файла (text18-10.txt) вывести на экран его содержимое,
#количество букв в верхнем регистре. Сформировать новый файл, в который поместить текст
#в стихотворной форме предварительно поставив после последней строки автора и название
#произведения.

# Открываем исходный файл
with open("text18-10.txt", "r", encoding="utf-8") as file:
    text = file.read()

# 1. Выводим содержимое файла на экран
print("Содержимое файла:\n")
print(text)

# 2. Считаем количество букв в верхнем регистре
upper_count = 0
for symbol in text:
    if symbol.isalpha() and symbol.isupper():
        upper_count += 1

print("\nКоличество букв в верхнем регистре:", upper_count)

# 3. Формируем текст в стихотворной форме
# Например, каждое предложение с новой строки
lines = text.split(". ")

# Автор и название
author = "А.С. Пушкин"
title = "Пример произведения"

# 4. Записываем в новый файл
with open("result2.txt", "w", encoding="utf-8") as file:
    for line in lines:
        line = line.strip()
        if line:
            file.write(line)
            if not line.endswith("."):
                file.write(".")
            file.write("\n")
    file.write("\n")
    file.write("Автор: " + author + "\n")
    file.write("Название: " + title + "\n")

print("Задание 2 выполнено. Результат записан в файл result2.txt")
# Из предложенного текстового файла (text18-10.txt) вывести на экран его содержимое,
#количество букв в верхнем регистре. Сформировать новый файл, в который поместить текст
#в стихотворной форме предварительно поставив после последней строки автора и название
#произведения.

# Открываем исходный файл
with open("text18-10.txt", "r", encoding="utf-8") as file:
    text = file.read()

# 1. Вывод содержимого файла
print("Содержимое файла:\n")
print(text)

# 2. Подсчёт заглавных букв
upper_count = sum(1 for symbol in text if symbol.isalpha() and symbol.isupper())

print("\nКоличество букв в верхнем регистре:", upper_count)

# 3. Формирование стихотворной формы
# Разбиваем текст на слова
words = text.split()

# Формируем строки по 5 слов (как "стих")
poem_lines = []
line = ""

for i, word in enumerate(words, 1):
    line += word + " "
    if i % 5 == 0:
        poem_lines.append(line.strip())
        line = ""

# если остались слова
if line:
    poem_lines.append(line.strip())

# Автор и название
author = "А.С. Пушкин"
title = "Пример произведения"

# 4. Запись в новый файл
with open("result2.txt", "w", encoding="utf-8") as file:
    file.write("Текст в стихотворной форме:\n\n")

    for line in poem_lines:
        file.write(line + "\n")

    file.write("\n")
    file.write("Автор: " + author + "\n")
    file.write("Название: " + title + "\n")

print("Задание 2 выполнено. Результат записан в файл result2.txt")
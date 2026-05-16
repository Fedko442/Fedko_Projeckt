#Из заданной строки отобразить только символы нижнего регистра.
#Использовать библиотеку string.

import string

text = input("Введите строку: ")

# Оставляем только символы нижнего регистра
lowercase_chars = ''.join(
    filter(lambda ch: ch in string.ascii_lowercase, text)
)

print("Символы нижнего регистра:", lowercase_chars)
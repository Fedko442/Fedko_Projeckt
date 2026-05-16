#Из заданной строки отобразить только символы нижнего регистра.
#Использовать библиотеку string.

import string

text = "In PyCharm, you can specify third-party standalone applications and run them as External Tools"

result = ""

for ch in text:
    if ch in string.ascii_lowercase:
        result += ch

print("Символы нижнего регистра:")
print(result)
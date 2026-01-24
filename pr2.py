str = '2020год -16 -10 -6 4 20 32 36 32 32 15 1 -15'

parts = str.split()

year = parts[0]

temp = [int(x) for x in parts[1:]]

list = list(temp)

spisok = {
    "Год": year,
    "Температура": temp
}

mid_temp = sum(temp) // len(temp)

print("минимальная температура: ", min(temp))
print("Средняя температура: ", mid_temp)
print(spisok)

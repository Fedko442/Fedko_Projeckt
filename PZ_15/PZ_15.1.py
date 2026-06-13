#Приложение «НОТАРИАЛЬНАЯ КОНТОРА» для некоторой организации. 
# БД должна содержать таблицу «Нотариальные услуги» со следующей структурой записи:
#ФИО клиента
#Услуга
#Сумма сделки
#Комиссионные (доход конторы)

import sqlite3

conn = sqlite3.connect("notary.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Нотариальные_услуги (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ФИО_клиента TEXT,
    Услуга TEXT,
    Сумма_сделки REAL,
    Комиссионные REAL
)
""")

cursor.execute("""
INSERT INTO Нотариальные_услуги
(ФИО_клиента, Услуга, Сумма_сделки, Комиссионные)
VALUES
('Иванов Иван Иванович', 'Заверение договора', 50000, 2500)
""")

conn.commit()

cursor.execute("SELECT * FROM Нотариальные_услуги")

for row in cursor.fetchall():
    print(row)

conn.close()
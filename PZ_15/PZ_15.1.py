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

conn.commit()


def add_record():
    client = input("ФИО клиента: ")
    service = input("Услуга: ")
    amount = float(input("Сумма сделки: "))
    commission = float(input("Комиссионные: "))

    cursor.execute("""
    INSERT INTO Нотариальные_услуги
    (ФИО_клиента, Услуга, Сумма_сделки, Комиссионные)
    VALUES (?, ?, ?, ?)
    """, (client, service, amount, commission))

    conn.commit()
    print("Запись добавлена")


def show_records():
    cursor.execute("SELECT * FROM Нотариальные_услуги")

    for row in cursor.fetchall():
        print(row)


def search_by_client():
    client = input("Введите ФИО клиента: ")

    cursor.execute("""
    SELECT * FROM Нотариальные_услуги
    WHERE ФИО_клиента = ?
    """, (client,))

    print(cursor.fetchall())


def search_by_service():
    service = input("Введите услугу: ")

    cursor.execute("""
    SELECT * FROM Нотариальные_услуги
    WHERE Услуга = ?
    """, (service,))

    print(cursor.fetchall())


def search_by_amount():
    amount = float(input("Минимальная сумма сделки: "))

    cursor.execute("""
    SELECT * FROM Нотариальные_услуги
    WHERE Сумма_сделки > ?
    """, (amount,))

    print(cursor.fetchall())


def delete_by_id():
    id_record = int(input("Введите id: "))

    cursor.execute("""
    DELETE FROM Нотариальные_услуги
    WHERE id = ?
    """, (id_record,))

    conn.commit()
    print("Запись удалена")


def delete_by_client():
    client = input("Введите ФИО клиента: ")

    cursor.execute("""
    DELETE FROM Нотариальные_услуги
    WHERE ФИО_клиента = ?
    """, (client,))

    conn.commit()
    print("Записи удалены")


def delete_by_service():
    service = input("Введите услугу: ")

    cursor.execute("""
    DELETE FROM Нотариальные_услуги
    WHERE Услуга = ?
    """, (service,))

    conn.commit()
    print("Записи удалены")


def update_commission():
    id_record = int(input("ID записи: "))
    commission = float(input("Новые комиссионные: "))

    cursor.execute("""
    UPDATE Нотариальные_услуги
    SET Комиссионные = ?
    WHERE id = ?
    """, (commission, id_record))

    conn.commit()
    print("Данные изменены")


while True:
    print("\n1 - Добавить запись")
    print("2 - Показать записи")
    print("3 - Поиск по клиенту")
    print("4 - Поиск по услуге")
    print("5 - Поиск по сумме сделки")
    print("6 - Удалить по ID")
    print("7 - Удалить по клиенту")
    print("8 - Удалить по услуге")
    print("9 - Изменить комиссионные")
    print("0 - Выход")

    choice = input("Выберите действие: ")

    try:
        if choice == "1":
            add_record()

        elif choice == "2":
            show_records()

        elif choice == "3":
            search_by_client()

        elif choice == "4":
            search_by_service()

        elif choice == "5":
            search_by_amount()

        elif choice == "6":
            delete_by_id()

        elif choice == "7":
            delete_by_client()

        elif choice == "8":
            delete_by_service()

        elif choice == "9":
            update_commission()

        elif choice == "0":
            break

        else:
            print("Неверный пункт меню")

    except Exception as e:
        print("Ошибка:", e)

conn.close()
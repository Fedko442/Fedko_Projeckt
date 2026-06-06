try:
    with open("writer.txt", "r", encoding="utf-8") as file:
        text = file.read()

    words = text.split()

    surnames = list(filter(lambda word: word.istitle(), words))

    print("Фамилии писателей:")
    print(*surnames, sep="\n")

    print("Количество фамилий:", len(surnames))

    new_text = text.replace("роман", "произведение")

    with open("new_writer.txt", "w", encoding="utf-8") as file:
        file.write(new_text)

except FileNotFoundError:
    print("Файл writer.txt не найден")
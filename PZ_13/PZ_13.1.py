try:
    with open("writer.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()

    surnames = list(
        map(
            lambda line: line.split()[0],
            filter(lambda line: line.strip(), lines)
        )
    )

    print("Фамилии писателей:")
    print(*surnames, sep="\n")

    print("\nКоличество фамилий:", len(surnames))

    text = ''.join(lines)

    new_text = text.replace("роман", "произведение")

    with open("new_writer.txt", "w", encoding="utf-8") as file:
        file.write(new_text)

    print("Файл new_writer.txt создан")

except FileNotFoundError:
    print("Файл writer.txt не найден")
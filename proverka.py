# Вариант 6
# Определить, в каких магазинах нельзя приобрести книги Грибоедова и Маяковского.

magistr = {"Лермонтов", "Достоевский", "Пушкин", "Тютчев"}
domknigi = {"Толстой", "Грибоедов", "Чехов", "Пушкин"}
bukmarket = {"Пушкин", "Достоевский", "Маяковский"}
galereya = {"Чехов", "Тютчев", "Пушкин"}

stores = {
    "Магистр": magistr,
    "ДомКниги": domknigi,
    "БукМаркет": bukmarket,
    "Галерея": galereya
}

# кого ищем
author1 = "Грибоедов"
author2 = "Маяковский"

# магазины, где НЕТ автора
no_author1 = [name for name, books in stores.items() if author1 not in books]
no_author2 = [name for name, books in stores.items() if author2 not in books]

print("=== Вариант 6 ===")
print(f"Книги {author1} нельзя купить в магазинах:", ", ".join(no_author1))
print(f"Книги {author2} нельзя купить в магазинах:", ", ".join(no_author2))

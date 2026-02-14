# Вариант 7
# Определить, в каких турагентствах можно приобрести туры в Канаду и в США.

voyazh = {"Мексика", "Канада", "Израиль", "Италия", "США"}
reinatour = {"Англия", "Япония", "Канада", "ЮАР"}
raduga = {"США", "Испания", "Швеция", "Австралия"}

agencies = {
    "Вояж": voyazh,
    "РейнаТур": reinatour,
    "Радуга": raduga
}

country1 = "Канада"
country2 = "США"

canada_agencies = [name for name, tours in agencies.items() if country1 in tours]
usa_agencies = [name for name, tours in agencies.items() if country2 in tours]

print("=== Вариант 7 ===")
print(f"Туры в {country1} можно купить в:", ", ".join(canada_agencies))
print(f"Туры в {country2} можно купить в:", ", ".join(usa_agencies))

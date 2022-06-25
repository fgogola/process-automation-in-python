"""
Wymagania:
Napisz program, który wczytuje od użytkownika stringi w postaci klucz - wartość
Dodaj je do słownika.
Jeśli dany klucz istnieje w słowniku - nie rób nic.

Zapewnij możliwość podania kolejnych par klucz-wartość lub zaprzestawania ich podawania.

Wypisz elementy słownika na ekran w formie "klucz -> wartość"

Podpowiedź:
Użyj dwóch inputów do pobrania wartości
"""
slownik = {}

while True:
    klucz = input("Podaj klucz (slowo stop konczy program): ")
    if klucz in slownik.keys():
        print("Podany klucz znajduje sie juz w slowniku")
        continue
    elif klucz == "stop":
        break
    wartosc = input("Podaj wartosc: ")
    slownik[klucz] = wartosc

for key, value in slownik.items():
    print(f"{key} = {value}")
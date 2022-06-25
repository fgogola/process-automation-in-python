"""
Wymagania:
Sprawdź czy podana przez użytkownika liczba
jest podzielna przez 3, 5, 7

Wypisz wyniki na ekran.

Pamiętaj o komentarzach.

Rezultat wypisz na ekran.

Podpowiedź:
Odpowiednio formatuj stringi
"""

liczba = int(input("Podaj liczbe: "))

if liczba % 3 == 0:
    print(f"Liczba {liczba} jest podzielna przez 3")
else:
    print(f"Liczba {liczba} nie jest podzielna przez 3")
if liczba % 5 == 0:
    print(f"Liczba {liczba} jest podzielna przez 5")
else:
    print(f"Liczba {liczba} nie jest podzielna przez 5")
if liczba % 7 == 0:
    print(f"Liczba {liczba} jest podzielna przez 7")
else:
    print(f"Liczba {liczba} nie jest podzielna przez 7")
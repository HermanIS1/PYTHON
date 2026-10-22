from math import sqrt

# 1
teksty = ["Ala ma kota", "Python", "To jest przykład", "jeden dwa trzy"]
teksty_wynik = [
    " ".join(tekst.split()[:2]) for tekst in teksty if len(tekst.split()) > 1
]
print(teksty_wynik)

# 2
krotki_dodatnie = [(1, 4, 9), (2, 0, 8), (16, 25)]
krotki_pierwiastki = [
    tuple(sqrt(liczba) for liczba in krotka)
    for krotka in krotki_dodatnie
    if all(liczba > 0 for liczba in krotka)
]
print(krotki_pierwiastki)

# 3
krotki_podzielne = [(6, 3, 9), (3, 4, 6), (12, 0)]
krotki_po_podzieleniu = [
    tuple(liczba // 3 for liczba in krotka)
    for krotka in krotki_podzielne
    if all(liczba % 3 == 0 for liczba in krotka)
]
print(krotki_po_podzieleniu)

# 4
krotki_z_podzielnymi = [(1, 0, 4, 3), (2, 5), (6, 7, 9)]
krotki_elementow_podzielnych = [
    tuple(liczba for liczba in krotka if liczba % 3 == 0)
    for krotka in krotki_z_podzielnymi
    if any(liczba % 3 == 0 for liczba in krotka)
]
print(krotki_elementow_podzielnych)

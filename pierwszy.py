from copy import deepcopy

a = 2
print(a)

# typy liczbowe int, float, complex i operatory arytmetyczne

# typy sekwencyjne: string, bytes, list, tuple, konkatenacja

s = "rzuf"
print(s, type(s), len(s))

# podkatenacja
print(2 * "pies" + "kot")

# indeksowanie
print(s[1])

s = "Ala ma kota"
print(s[1:-1:2])
print(s[1:])
print(s[:-2])
print(s[::-1])

print(dir(s))

print(s.count("a"), s.index("a"))


# bytes

s = b"Ala ma kota"
print(type(s))


s = b"zolw"
print(s)

s = b"\xc5\xbc".decode("utf-8")
print(s)
print("\u0394")

print(dir(b" "))

s = 'Ala\nma\nkota"\\'
print(s)
s = r"Ala\nma\nkota" "\\"
print(s)
s = "Ala\nma\nkota\\"

s = """Ala
ma
kota"""

# listy
l = [1, "Ala", [b"kot", 2.0]]
print(l[-1], l[:2], len(l))


# operacje na listach
l = ["1", 2, "1"]
l.append("a")
print(l)
l.insert(0, "b")
print(l)
x = l.pop
print(l, x)
l.remove("1")
print(l)


# lista jest modyfikowana w miejscu

l = ["a", ["b", "c"]]
l1 = deepcopy(l)
l[-1][-1] = "d"
print(l, l1)

s = "Ala ma kota"
# s[0] = '0' !niemozna!
print(s.split(" "))
print(s.split("a", 1))
print(s.split(" ", 1))
print(s.rsplit.__doc__)
print(
    s.rsplit(maxsplit=1)
)  # dziele dalej domyslnie po wszystkich ciagach bialych znakow
# przekazuje argument nie przez pozycje ale przez nzawe

s = "    Ala\n"
print(s, ":)")
print(s.strip() + ":)")
print(s.rstrip() + ":)")
print(s.lstrip() + ":)")

slowa = ["Ala", "ma", "kota"]
print(slowa)
print("_X_".join(slowa))

# krotka

t = (1, 2)
print(t)
# t[1] = 3  # niemozna!
a = 13
b = 7

a, b = b, a % b
print(a, b)


# google colapse GUGIEL
# dox,python.org


# ZALICZENIE

# zajec wprowadznie -> obiektowe -> wielowatkowosc -> tcipi -> sqlite -> skrypty cgi -> numeryka

# slowniki
d = {"red": (255, 0, 0), "blue": (0, 0, 255)}

d = dict([("red", (255, 0, 0)), ("blue", (0, 0, 255))])

print(d["red"])

d = {1: "a", "a": [("c", 1), {2: (1, 2)}]}

# dodaj wartosc dla klucza
d[3] = 4
print(d)

# usun wartosc
del d[3]
print(d)

# usun wartosc dla klucza z pobraniem wartosci
# x = d.pop(3)
# print(d, x)


# update slownika
# print(d | {2: "b", 3: "c"})
# print(d)
# d = d | {2: "b", 3: "c"}
# print(d)
# d |= {2: "b", 3: "c"}
# print(d)
# d.update({2: "b", 3: "c"})
# print(d)


# pobieranie wartosci
# if 1 in d:
#    print(d[1])
print(d[10]) if 10 in d else "nie ma"
print(d.get(10, "Nie ma"))
print(chr(0x41))
# print(dir(d))
# print(d.__hash__)


# iteracja po slowniku <==> iteracja po kluczach

for key in d:
    print(d[key])
k = d.keys()
d["kot"] = "ala"
print(k)

print(d.values())
print(d.items)

# slownik skladany
kw = {x: x**2 for x in range(4)}
print(kw)

s = {1, 2, 3}
print(s, type(s))
l = [1, 1, 2, 3]
print(set(l), len(set(l)))
print(x % 3 for x in range(10))


##########################################
# FUNCKJE
def podwoj(x: int) -> int:
    "funkcja ktora podwaja"
    return 2 * x


print(podwoj(2), podwoj(2.0), podwoj(2.0 + 0), podwoj("dwa"))  # na slowniku sie nie da
print(podwoj.__doc__)
print(print.__doc__)


# argumenty funkcji domyslne, pozycyjne, nazwane
def f(a, b="xx", c="yy"):
    return a, b, c


print(f(1))
## print(f(1, 2)) #2 - argument pozycyjny
## print(f(1, 2, 3))
## print(f(1, c=2))# 2 - argument nazwany
## print(f(c=2, 1))# argument pozycyjny przed nazwanym

k = (1, 2, 3)
print(f(k))
print(f(*k))  # rozpakowanie sekwencji
d = {"a": 11, "b": 12, "c": 13}
print(f(**d))  # rozpakowywanie slownika


# blad izycie typu modyfikowalnego w miejscu jako wartosc domyslna
# funkcja pamietajaca stan
# def powieksz(l=[]):
# l.append(x)
#   return l


# jak naprawic
def powieksz(x, l=None):
    if l == None:
        l = []
    l.append(x)
    return l


print(powieksz(2, [10]))
print(powieksz(1))
print(powieksz(1))
print(powieksz(1))


def pole(a, b=None):
    if b == None:
        b = a
    return a * b


print(pole(2, 3))
print(1)  # zwraca none


# argumenty tylko pozycyjne i tylko nazwane


def f(a, /, b, *, c):  # za gwiazda moga byc tylko argumenty nazwane
    print(a, b, c)


# funckja typu void

f(1, 2, c=3)
f(1, b=2, c=3)


# zmienna liczba argumentow
def pole(*boki):
    if len(boki) == 2:
        return boki[0] * boki[1]
    elif len(boki) == 1:
        return boki[0] ** 2
    else:
        print("nieprawidlowa liczba bokow")  # powinnismy rzucic wyjatek
    return boki


print(pole(1, 2, 3))
print(pole("ala", "kot"))
print(pole(2, 3), pole(2))

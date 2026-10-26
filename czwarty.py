def funkcja(a):
    print(a)


x = 8
funkcja(2)

##################


def funkcja(a):
    x = 3
    print(x)


x = 8
funkcja(2)
print(x)

##################


def funkcja(a):
    global x
    x = 3
    print(x)


x = 8
funkcja(2)
print(x)

##################


sekwencja = [1, 4, 2, 8, 5, 7]


def kwadrat(x):
    return x**2


def nieparzyste(x):
    return x % 2 == 1


l = [i**2 for i in sekwencja]
print(l)
l = map(kwadrat, sekwencja)
print(list(l))

l = [i for i in sekwencja if nieparzyste(i)]
print(l)
l = filter(nieparzyste, sekwencja)
print(list(l))

l = sorted(sekwencja, reverse=True)
print(l)
l = sorted(sekwencja, reverse=True, key=abs)
print(l)

d = {"pies": 4, "kot": 8, "szczur": 2}
print(sorted(d))
# jak posortowac klucze slownika ze wzledu na przypisana im wartosc
print(sorted(d, key=d.get))

# funkcje anonimowe
kwadrat = lambda x: x**2
print(*map(lambda x: x**2, sekwencja))

print(sorted(d, key=lambda x: x[-1]))

l = [1, 3, 2]
print(sorted(l))
l.sort()
print(l)


# lista funkcji potegowych o wykladnikach od 0 do 9
fp = [lambda x, y=y: x**y for y in range(10)]

for f in fp:
    print(f(2))

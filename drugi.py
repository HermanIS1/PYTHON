
# instrukcje warunkowe

T = 12

if T < 10:	
	print("zimno")
else:
	print("ciepło")

if T < 10:
	if T < 0:	
		print("zimno")
	else:
		print("chłodno")
else:
	if T < 20:
		print("ciepło")
	else:
		print("gorąco")

#########

if T < 0:
	print("zimno")
elif T < 10:
	print("chłodno")
elif T < 20:
	print("ciepło")
else:
	print("gorąco")
	
##########

print("zimno" if T < 10 else "ciepło")

print(("zimno" if T < 0 else "chłodno") if T < 10 else ("ciepło" if T < 20 else "gorąco"))
# można, ale już nieczytelne

# Operatory porównania: <, <=, >, >=, ==, !=
# Operatory logiczne: not, or, and

# kwantyfikatory

zachodzenie = (True, True, False) # sprawdzamy warunek na jakimś zbiorze
print(all(zachodzenie))
print(any(zachodzenie))

########### Pętla for

print(20*'#')

for znak in "żółw":
	print(znak)

print(20*'#')

for liczba in range(2,10,2): # start, stop, step
	print(liczba)

print(20*'#')

for liczba in range(10):
	if liczba<4:
		continue
	if liczba > 7:
		break
	print(liczba)
else:
	print('czyste wyjście') # jeżeli nie było breaka

print(20*'#')

wyjscie = False
for i in range(2):
	if wyjscie:
		break
	for j in range(2):
		if wyjscie:
			break
		print(i,j)
		if i or j:
			wyjscie = True

## Pętla while

i = 0
kwadrat = 0
while kwadrat < 10:
	print(kwadrat)
	i+=1
	kwadrat = i**2

# continue, break, else - jak dla for

# lepiej składniowo, ale niewydajnie

i = 0
while i**2 < 10:
	print(i**2)
	i+=1

# idealnie: 4 linijki, jedno obliczanie kwadratu <= operator przypisania

i = 0
while (kwadrat := i**2) < 10:
	print(kwadrat)
	i+=1

############################# Listy składane

lin = [-1,4,2,8,3]
# Zad 1. stwórzmy lout zawierający kwadraty elementów nieparzystych

lout = len(lin)*[0]
for i in range(len(lin)):
	if lin[i] % 2 != 0:
		lout[i] = lin[i]**2

print(lout) # bardzo brzydko

lout = []
for el in lin:
	if el % 2:
		lout.append(el**2)

print(lout) # lepiej

# Zad 2. stwórzmy lout zawierający nieparzyste kwadraty elementów

lout = []
for el in lin:
	if (kwadrat := el**2) % 2:
		lout.append(kwadrat)

print(lout)

#Tak należy to zrobić w pythonie
lout = [el**2 for el in lin if el % 2] # Zad 1
print(lout)
lout = [kwadrat for el in lin if (kwadrat := el**2) % 2] # Zad 2
print(lout)

############# Rozpakowywanie krotek

krotka_wymiarow = (2.1,5.3,1.2) 
l, h = krotka_wymiarow[:2]	# rozpakowuje krotke do zmiennych
print(l)
print(h)

#rozpakowanie sekwencji argumentów funkcji
print(krotka_wymiarow)
print(*krotka_wymiarow) # rozkauj sekwencję - podaj jej elementy jako kolejne argumenty

args = (' ',1)
print('Ala ma kota'.split(*args))

############### zip

slowa = 'Ala ma kota'.split()
rangi = [5,-1,4]
litery = 'XYZ'

print(*zip(slowa,rangi,litery)) # pierwsze z pierwszymi, drugie z drugimi

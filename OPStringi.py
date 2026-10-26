x = "ala"
y = "kot"
print(x, "ma", y)
# brzydko!!!

s = "%s ma %s"

print(s)
print(s % (x, y))

# %d, %f, %e

z = 101.687354
print("%f %e " % (z, z))

print("X%sX" % "Ala")

###############################

S = "{} ma {}"
print(S)
print(S.format(x, y))

l = ["Ala", "kot"]
d = {"zwierze": "pies"}

print(f"{l[0]} ma {l[1]} i {d['zwierze']}")  # mozemy indeksowac argumenty

z = 1 + 2j
print(f"{z.real} + {z.imag}i")  # mozemy odwolywac sie do atrybutow

print("***{0:10s}***".format("Ala"))

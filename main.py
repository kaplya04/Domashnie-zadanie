chis = int(input("Введите число: "))
st = input("Введите строку: ")
mass = []
for e in range(1,chis):
    if e % 2 == 0:
        e = st
        mass.append(st)
    else:mass.append(e)
print(mass)

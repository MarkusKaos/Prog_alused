ringid = int(input("Sisesta ringide arv: "))
i = 1
summa = 0
porgandid = 0
while i <= ringid:
    porgandid += i
    i += 1
    summa = porgandid + summa
print("Porgandite koguarv on " + str(summa))
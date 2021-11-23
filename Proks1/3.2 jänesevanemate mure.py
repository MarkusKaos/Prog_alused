ringid = int(input("Sisestage ringide arv: "))
i = 1
a = 0
porgandid = 0
while i < ringid:
    i = i + 2
    porgandid = porgandid + 2 + a
    a = a + 2
print("Porgandite koguarv on " + str(porgandid))


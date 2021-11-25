põialpoisid = int(input("Mitu põialpoissi tahab õunu? "))

from random import randint
i = 0
õun = 14
while i < põialpoisid:
    i += 1
    r = randint(1,2)
    õun = õun - r
    print(str(r))
print("lumivalgekesele jäi " + str(õun))

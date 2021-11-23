from random import randint

istekoht = input("Kas te soovite istekohta ise valida (ise) või loodsida (loos)? ")
if istekoht == "ise":
    isekoht = input("Kas soovite istuda akna ääres (aken) või mitte (muu)? ")
    if isekoht == "aken":
        print("Valisite ise. Aknakoht.")
    else:
        print("Valisite ise muu koha.")
elif istekoht == "loos":
    looskoht = randint(1,3)
    if looskoht == 1:
        print("Teie loositud koht on aknakoht.")
    elif looskoht == 2 or looskoht == 3:
        print("Teie loositud koht on muukoht.")
        
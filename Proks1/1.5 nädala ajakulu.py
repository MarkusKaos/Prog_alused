ainepunktid = int(input("Sisestage ainepunktide arv: "))
nädalate_arv = int(input("Sisestage nädalate arv: "))

ajakulu = round(ainepunktid * 26 / nädalate_arv)
print(str(ajakulu))
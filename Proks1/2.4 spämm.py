kirjasuurus = input("Sisestage kirja suurus: ")
kirjateema = input("Sisestage kirja teema pealkiri: ")
kirjafail = input("Kas kirjaga on kaasas fail? ")

if kirjateema == "" or "fail" == "jah" and kirjasuurus > 1:
    print("Kiri on spämm")
else:
    print("Kiri ei ole spämm")
    

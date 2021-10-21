nimi = input("Sisestage oma nimi: ")
lubatud_kiirus = int(input("Sisestage lubatud kiirus: "))
tegelik_kiirus = int(input("Sisestage tegelik kiirus: "))

trahv = (tegelik_kiirus - lubatud_kiirus) *3
tegelik_trahv = min(190, trahv)
print(nimi + ", kiiruse ületamise eest on teie trahv " + str(tegelik_trahv))
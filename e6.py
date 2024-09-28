def szog():
#A program  kérjen be a konzolról egy valós számot! Ha ez a szám 0 és 360 közé esik, akkor legyen egy szög mértéke (pl. 60 fok), egyébként a program adjon hibaüzenetet! Ha lehet, a program írja ki a szög mértéke alapján a szög típusát (pl.: 60 -> hegyesszög)!
    vszam = float(input("Kérem adjon meg egy valós számot!"))
    if (vszam >= 0) and (vszam <= 360):
        if vszam == 0:
            print(str(vszam)+" -> nullszög")
        elif (vszam > 0) and (vszam < 90):
            print(str(vszam)+" -> hegyesszög")
        elif vszam == 90:
            print(str(vszam) + " -> derékszög")
        elif (vszam > 90) and (vszam < 180):
            print(str(vszam)+" -> tompaszög")
        elif vszam == 180:
            print(str(vszam) + " -> egyenesszög")
        elif (vszam > 180) and (vszam < 360):
            print(str(vszam)+" -> homorúszög")
        elif vszam == 360:
            print(str(vszam) + " -> teljesszög")
    else:
        print("HIBA: Nem megfelelő szögérték!")
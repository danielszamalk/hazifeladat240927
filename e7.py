import math
def negyzetgyok():
    #A program számítsa ki egy beolvasott valós szám négyzetgyökét! A program adjon hibaüzenetet, ha a felhasználó negatív számból akar gyököt vonni!
    szam = float(input("Adjon meg egy számot!"))
    if szam >= 0:
        gyok = math.sqrt(szam)
        print(gyok)
    else:
        print("HIBA: Negatív szám gyökét akarja számolni")
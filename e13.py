import math



def kor():
    #A program olvassa be a konzolról egy kör sugarát! Ha a sugár nem pozitív, akkor a program írja ki konzolra, hogy "Hiba: a kör sugara nem pozitív!"; egyébként a program számítsa ki és írja ki a kör kerületét, területét a konzolra!
    r = float(input("Kérem adjon meg egy kör sugárértéket!"))
    if r>0:
        terulet = math.pow(r, 2) * math.pi
        # r**2, r*r, pow(r, 2)*math.pi
        kerulet = 2* r * math.pi
        print("A kör területe: "+str(terulet)+", a kör kerülete: "+str(kerulet)+".")
    else:
        print("HIBA: A kör sugara nem pozitív")



#célozottan from math import pow, pi
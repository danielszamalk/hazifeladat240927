#A program olvasson be a konzolról két valós számot! Ha mindkét szám pozitív, akkor legyenek a beolvasott számok egy téglalap oldalai. A program számítsa ki a téglalap kerületét, területét, és írja ki két tizedesre kerekítve az eredményeket a konzolra! Hiba esetén írja ki: "Hiba: a téglalap oldalai nem pozitívak!"!


#függvény
def egeszbeolvas():
    szam=float(input("Kérem adjon meg egy egész számot!"))
    return szam


 #eljárás
def teglalap():
    oldal1=egeszbeolvas()
    oldal2=egeszbeolvas()

    if (oldal1>0) and (oldal2>0):
        kerulet= round((oldal1 * oldal2), 2)
        terulet= round((2 * (oldal1 + oldal2)), 2)
        print("A téglalap kerülete: "+str(kerulet)+", területe:"+str(terulet))
    else:
        print("Hiba: a téglalap oldalai nem pozitívak!")
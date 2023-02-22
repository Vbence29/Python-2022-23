nev=input("Kérek egy nevet: ")

print("A " + nev + " nevet irtad be.")

print("A {belsoNev} nevet irtad be.".format(belsoNev=nev))


if len(nev)<5:
    print("jó rövid név.")
elif len(nev)>=10:
    print("veri big név.")

be="nemvégjel"
szavak=[]
while be!="":
    be=input("Irj be valamit: ")
    szavak.append(be)

#szavak.remove("")
#szavak.pop(-1)
#szavak.pop(len(szavak)-1)
szavak=szavak[:-1]

print(szavak)



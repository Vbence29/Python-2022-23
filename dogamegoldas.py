#1. feladat: Kérj be 10 számot egy megfelelő adatszerkezetbe!
szamok=[ ]
for i in range(10):
    szamok.append(int(input(str(i+1)+" .szam: ")))
szamok=[1,2,3,4,5,6,7,8,9,0]
#2. feladat: A bekért számokat irasd ki egymás mellé!

for i in szamok:
    print(str(i),end="")
print()
print("vége")
#print("".join(szamok))
#3. feladat: A bekért számokat irasd ki 2 oszlopba!
for i in range(10):
    print(str(i)+"\t",end="")
    if i%3==0:
        print()

print()
#4. feladat: Számold ki a bekért számok átlagát!
atlag=sum(szamok)/len (szamok)
print(atlag)

osszeg=0
for i in szamok:
      osszeg+=i
atlag=osszeg/len(szamok)
print(atlag)


#5. feladat: A mellékelt szöveget tárold el a programodban:
szoveg="Integer eget pharetra magna. Nulla ex urna, congue ac tincidunt ut, interdum et metus. Phasellus nunc nunc, consectetur eu odio vitae, ullamcorper sagittis nisi. Ut quam tortor, tempus sit amet diam nec, auctor iaculis leo. Donec ut libero velit. Maecenas nisi magna, congue ut tortor quis, maximus maximus arcu. Mauris et commodo nibh. Fusce id est vehicula, consectetur mi et, molestie sapien."

betu="qwe"
while betu!="":
        betu=input("Kérek egy betűt:")
        szoveg=szoveg.replace(betu,betu.upper())

        print(szoveg)


lista=szoveg.split(" ")
lista.reverse()
szoveg2=" ".join(lista)
print(szoveg2)

jelek="'.!?-:;,"

for i in range(len(jelek)):
     szoveg=replace(jelek[i],"")

print(szoveg)     
     









f=open("penztar.txt")

termekek=[]
for e in f:
    temp=e.replace("\n","")
    termekek.append(temp)
f.close

print("2. feladatok")
print("A fizetesek szama: {} ".format(termekek.count("F")))

print("3. feladatok")


termekekszama=0
elsof=termekek.index("F")
for i in range(len(termekek)):
    if i < elsof:
        termekekszama+=1

print("Az első vásárló {} darab árucikket vásárolt".format(termekekszama))

print("4. feladatok")

termek=[]
f=open("penztar.txt")
for e in f:
    termek




f.close()
print(termek)

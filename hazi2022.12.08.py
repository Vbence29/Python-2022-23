import random 
oke=0
szam=random.randint(1000,9000)

while oke==0:
    szam=random.randint(1000,9000)
    if szam%6==0 and szam%12!=0:
        oke=1
        print(szam)

#167
#1666
#hattal oszthato, de 12-vel (2*6)nemnagyon

        
print(random.randrange(167,1667,2)*6)

print((random.randint(83,832)*2+1)  *  6)


szavak=["alma","körte","barack","sárkánygyümölcs","dinnye","szölő"]

#random.seed(1)
print(szavak[random.randint(0,len(szavak)-1)])

print(random.choice(szavak))

#[["alma",14],["körte",18],[]...]
print("-"*20)

nagyLista=[]
for e in szavak:
    kisLista=[]
    kisLista.append(e)
    kisLista.append(random.randint(12,312))
    #print(kisLista)
    nagyLista.append(kisLista)

print(nagyLista)
    
for e in nagyLista:
    print(e[0].ljust(10),str(e[1]).rjust(4),"kg")





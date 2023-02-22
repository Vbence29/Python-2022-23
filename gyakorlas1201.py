def oszlopba(munkalista,db):
        for i in range (len(munkalista)):
             print(munkalista[i],end=" ")
             if i%db==db-1:
                 print()
        print()

    


lista=[ ]
for i in range(0):
    lista.append(int(input("Adj egy numbert: ")))

lista=[1,2,3,4,5,6,7,8,9,0]    
print(lista)

for i in range (len(lista)):
     print(lista[i],end=" ")
     if i%3==2:
         print()
print()
   
szamBe=int(input("Give me 1 szám: "))
if szamBe in lista:
    print("van inside")
else:
    print("nincs inside")

oszlopba(lista,5)
#hibakezeles

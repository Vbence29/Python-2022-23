

lista=["Bence","László","Ferenc"]
#lista.append("Martin")
try: 
    print(lista[3])
except:
    print("valami nem jó")
else:
    print("Sikeres! :)")
finally:
    print("Itt a vége")

szam=""
while szam=="":
    try:
        szam=int(input("Adj egy számot: ") )
    except ValueError:
        print("Nem szám")
    except:
            print("Ismeretlen hiba")


print(szam)




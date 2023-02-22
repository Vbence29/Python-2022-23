#Számbekérő modul
#Többféle paraméterezéssel
#2022.11.18. Verbulecz Bence



def szamBe(szoveg,tort=False,minimum=False,maximum=False) :
#      print(szoveg)
#      print(tort)
#      print(minimum)
      hiba=True
      while hiba:
          try:
                if tort:
                      szam=float(input(szoveg))
                else:
                      szam=int(input(szoveg))
          except:
              print("VALAMI NEM JÓ GECC!")
          else:
              hiba=False
      
szamBe("aggyál one számot sir: " ,minimum=10,tort=True)
    

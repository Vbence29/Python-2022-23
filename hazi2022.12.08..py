import random 
igen=0
szam=random.randint(1000,9000)

while igen==0:
    if szam%6==0 and szam%12!=0:
        igen=1
        print(szam)


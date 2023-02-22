f=open("penztar.txt")
otszaz=[]
for sor in f:
    temp=sor.replace("\n","").split(";")
    otszaz.append(temp)

f.close
print(otszaz)

for sor in otszaz:
    if sor== "F":
        1+1
print(1)

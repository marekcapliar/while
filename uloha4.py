cislo=int(input("zadaj cislo: "))
pocet=0
x=cislo
while cislo!=0:
    cislo=int(input("zadaj cislo: "))
    x+=cislo
    pocet+=1
print(x/pocet)

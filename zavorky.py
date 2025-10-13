from itertools import product
priklad=str(input());novyvypocet=False
vypocet,vysledek=priklad.split("=",1)
for (index1,cislo1),(index2,cislo2) in product(enumerate(str(vypocet.strip())),repeat=2):
    if index1>=index2:
        continue
    elif cislo1.isdigit() and cislo2.isdigit() and (index1==0 or vypocet[index1-1] in "+-*/") and (index2==(len(str(vypocet))-1) or vypocet[index2+1] in "+_*/"):
        if round(float(eval(str(vypocet[:index1]+"("+vypocet[index1:(index2+1)]+")"+vypocet[(index2+1):]))),5)==round(float(vysledek),5):
            novyvypocet=str(vypocet[:index1]+"("+vypocet[index1:(index2+1)]+")"+vypocet[(index2+1):])
            break
print("NELZE" if not(novyvypocet) else (novyvypocet+"="+vysledek))
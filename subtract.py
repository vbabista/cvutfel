seznam={"a":10, "b":11, "c":12, "d":13, "e":14, "f":15, "g":16, "h":17, "i":18, "j":19, "k":20, "l":21, "m":22, "n":23, "o":24, "p":25, "q":26, "r":27, "s":28, "t":29, "u":30, "v":31, "w":32, "x":33, "y":34, "z":35};prvek = {v: k for k, v in seznam.items()};vysledek_dek=0;z1=str(input());s1=int(input());z2=str(input());s2=int(input());sv=int(input())
def ne_vetsi(prvky, hranice):
    for znak in str(prvky):
        if znak.isdigit():hodnota=int(znak)
        elif znak in seznam:hodnota=seznam[znak]
        if (not(znak.isdigit()) and not(znak in seznam)) or hodnota>=hranice: print("ERROR");exit()
    return True
def vysledek(num,s):
    vysledek=""
    if not(2<=s<36):print("ERROR");exit()
    while num>0:
        zbytek=num%s
        if zbytek<10:vysledek=str(zbytek)+vysledek
        else:vysledek=prvek[zbytek]+vysledek
        num//=s
    print(vysledek or "0")
if all(2<=s<36 and ne_vetsi(z,s) for z,s in zip((z1,z2),(s1,s2))):vysledek_dek=abs(int(z1,s1)-int(z2,s2))
vysledek(vysledek_dek,sv)
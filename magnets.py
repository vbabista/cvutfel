import numpy as np
import sys
radky=open(sys.argv[1], 'rt', encoding='utf-8').read().splitlines()
silapole=2 #je to hranice na kterou působí magnet, ale kvůli pozdější matice to nebude fungovat pro cokoliv jinýho než 2 ze zadání, respektive funguje to parciálně
pol=radky[0]   #získání polarity
crd=list(map(int, radky[1].split())) #získání souřadnic + uložení do listu v int
matice=np.array([list(map(lambda magnet:magnet,line)) for line in radky[2:]])   #převedení do matice o h řádcích w sloupcích a pro práci v poli použití numpy, protože pak bude mnohem přehlednější for cyklus
if min(crd[1],crd[0])<0 or crd[1]>len(matice)-1 or crd[0]>len(matice[0])-1 or matice[crd[1],crd[0]]!=" ":print("ERROR");exit() #před procesingem kontrola jestli můžeme vložit novej magnet jinak to dá error a vypne se
for (y,x),hodnota in np.ndenumerate(matice):
    dx=x-crd[0] #definujeme "vzdálenost" vzájemnou polohu současné hodnoty od magnetu na ose x
    dy=y-crd[1] #to samý na ose y
    if hodnota!=" " and max(abs(dx),abs(dy))<=silapole and (abs(dx)==abs(dy) or 0 in (dx,dy)):    #1.pokud jde o + nebo - 2.pokud bude nejvyšší z absolutních rozdílů v tolerovaném poli je souřadnice v ovlivňovasném poli 3. pokud se absolutní rozdíly rovnají je na diagonále nebo pokud některý je 0 je na stejném řádku/sloupci jako magnet (už nemusíme uvažovat že se magnety nekryjou dx,dy=0 bo jsme to už oštřili)
        if hodnota==pol and max(abs(dx),abs(dy))<silapole and (0>crd[0]+2*dx or crd[0]+2*dx>len(matice[0])-1 or 0>crd[1]+2*dy or crd[1]+2*dy>len(matice)-1 or matice[crd[1]+2*dy][crd[0]+2*dx]==" "):#1.pokud budou shodná znaménka 2. musíme si uvědomit že když jsou stejné budou se z pole vytlačují jen ty co sousedí z novým magnetem 3. když se budou odpuzovat nová souřadnice bude mít 2x větší rozdíl jelikož maximální rozdíl bude 1 ověříme tedy jestli je souřadnice v matici(v té logice je že je pravda když není, to zamezuje erroru) a pokud ano jestli je prázdná
            if 0<=crd[0]+2*dx<=len(matice[0])-1 and 0<=crd[1]+2*dy<=len(matice)-1:  #pokud pole v matici existuje dáme novou hodnotu
                matice[crd[1]+2*dy][crd[0]+2*dx]=hodnota
            matice[y][x]=" "  #vymažeme starou tak i tak, jelikož se buď přepíše nebo oddálí mimo mřížku (matici)
            print(f"posunuji {x} {y} {hodnota}")
        elif hodnota!=pol and max(abs(dx),abs(dy))==silapole and matice[crd[1]+int((1/2)*dy)][crd[0]+int((1/2)*dx)]==" ":  #pokud to není stejná hodnota tak 1. aby ji pole přitáhlo musí být minimálně jedno pole mezera od bodu 2. jelikož musí být mezera aby se přitáhly tak to bude vždy 2 a nova souřadnice bude o polovinu menší než stará, proto nemusíme ani kontrolovat jestli je nová souřadnice v matici, pouze jestli je její hodnota mezera
            matice[crd[1]+int((1/2)*dy)][crd[0]+int((1/2)*dx)]=hodnota  #vepsani nove hodnoty
            matice[y][x]=" "  #smazani stare hodnoty
            print(f"posunuji {x} {y} {hodnota}")
matice[crd[1]][crd[0]]=pol
print(matice)
[print("".join(line)) for line in matice] #spojí to text jednoho řádku a vytiskne a pak znovu a znovu
import numpy as np
import sys
from itertools import product

def chyba():
    print("NONEXIST"); exit

def shoda_slova(radek,slovo,mirashody=[-100,0,0]):
    if len(radek)>=len(slovo):
        for inverz,index in product([1, -1],range(len(radek)-(len(slovo)-1))):
            akt_radek=radek[::inverz]
            count = sum(1 if akt_radek[j+index]==slovo[j] else -1 for j in range(len(slovo)))
            if count>mirashody[0]:
                mirashody=[count,index,inverz]
    else: return([0,0,0])
    return mirashody

def najdi_smer_a_radek(p1=list, p2=list):
    if p1[0]==p2[0]:
        smer=[2,0,6]
        radek=matice_vstup[p1[0],:]
        coord=[1,0,len(radek)-1,  0,  p1[0]]
    elif p1[1]==p2[1]:
        smer=[0,0,4]
        radek=matice_vstup[:,p1[1]]
        coord=[0,1,len(radek)-1,  p1[1],  0]
    elif p2[0]-p1[0]==p1[1]-p2[1]:
        smer=[7,0,3]
        radek=np.diagonal(np.fliplr(matice_vstup), offset=((len(matice_vstup[0])-1)-p1[1])-p1[0])
        coord=[-1,1,len(radek)-1,   p1[1]+np.argmax(radek=="0"),    p1[0]-np.argmax(radek=="0")]
    elif p2[0]-p1[0]==p2[1]-p1[1]:
        smer=[1,0,5]
        radek=np.diagonal(matice_vstup, offset=p1[1]-p1[0])
        coord=[1,1,len(radek)-1,   p1[1]+np.argmax(radek=="0"),    p1[0]+np.argmax(radek=="0")]
    else: chyba()
    return smer,radek,coord

vstup=open(sys.argv[1], 'rt', encoding='utf-8').read().splitlines()
matice_vstup=np.array([list(line) for line in vstup if vstup])
seznam_slov=open(sys.argv[2], 'rt', encoding='utf-8').read().splitlines()
nuly=np.argwhere(matice_vstup=="0")
finalnishoda=[0]
#coord[krok x, krok y, délka řady, souřadnice kraje řádku k matici x, y]    shoda[míra shody, index počátku slova, je braný z inverzní (-1) nebo ne (1)]    smer[inerzní, 0, normální] 
if len(nuly)!=2: chyba()

smer,radek,coord=najdi_smer_a_radek(nuly[0],nuly[1])
  
for slovo in seznam_slov:
    shodaslova=shoda_slova(radek,slovo)
    if shodaslova[0]>finalnishoda[0]:
        finalnishoda=shodaslova+[slovo]
#první závorka zkrze inverzi pozná jestli se list otáčel, pokud ano musí se podle souřadnic kroku a souřadnice začátku řádku počítat odzadu, jinak se počítá odpředu, elegantně vše přes -1 pro inverzi listu (finalnishoda[2])
souradnice=[int(coord[4]+(coord[2]*coord[1]*((1-finalnishoda[2])/2))+(coord[1]*finalnishoda[2]*finalnishoda[1])),   int(coord[3]+(coord[2]*coord[0]*((1-finalnishoda[2])/2))+(coord[0]*finalnishoda[2]*finalnishoda[1]))]

print(' '.join(str(cast) for cast in souradnice + [smer[1+finalnishoda[2]], finalnishoda[3]]))
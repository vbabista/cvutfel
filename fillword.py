import numpy as np
import sys
def chyba(): print("NONEXIST"); exit

def shoda_slova(radek,slovo,delsl,indexy,mirashody=[0,0,0]):
    word=np.array(list(slovo))
    for i,inverz in enumerate([1,-1]):
        akt_radek=radek[::inverz]
        for index in range(indexy[i][0],indexy[i][1]):
            segment=akt_radek[index:index+delsl]
            mask=(segment==word)|(segment=="0")
            count=np.count_nonzero(mask)*2-delsl
            if count>mirashody[0]:
                mirashody=[count, index, inverz]
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
        coord=[1,1,len(radek)-1,   p1[1]-np.argmax(radek=="0"),    p1[0]-np.argmax(radek=="0")]
    else: chyba()
    return smer,radek,coord

with open(sys.argv[1], encoding='utf-8') as f:
    vstup = [list(line.strip()) for line in f if line.strip()]; matice_vstup = np.array(vstup, dtype='<U1')
seznam_slov=open(sys.argv[2], 'rt', encoding='utf-8').read().splitlines()
nuly=np.argwhere(matice_vstup=="0")
if len(nuly)!=2: chyba()
finalnishoda=[0,0,0,0]
#coord[krok x, krok y, délka řady, souřadnice kraje řádku k matici x, y]    shoda[míra shody, index počátku slova, je braný z inverzní (-1) nebo ne (1)]    smer[inerzní, 0, normální] 
smer,radek,coord=najdi_smer_a_radek(nuly[0],nuly[1])
okraj=[nuly[0][0]-coord[4],nuly[1][0]-coord[4]] if smer[0] in [1,7] else [nuly[0][1],nuly[1][1]] if smer[0]==2 else [nuly[0][0],nuly[1][0]] # pozice podle x pokud nejde o sloupec jinak y
delka=abs(okraj[0]-okraj[1])+1
delrad=len(radek)

for slovo in seznam_slov:
    delsl=len(slovo)
    if delrad>=delsl and delsl>=delka:
        indexy=[[max(okraj[1]-delsl+1,0),min(okraj[0]+1,delrad-delsl)],[max(delrad-(okraj[0]+delsl),0),min(delrad-okraj[1],delrad-delsl)]]
        shodaslova=shoda_slova(radek,slovo,delsl,indexy)
        if shodaslova[0]>finalnishoda[0]:
            finalnishoda=shodaslova+[slovo]
#první závorka zkrze inverzi pozná jestli se list otáčel, pokud ano musí se podle souřadnic kroku a souřadnice začátku řádku počítat odzadu, jinak se počítá odpředu, elegantně vše přes -1 pro inverzi listu (finalnishoda[2])
souradnice=[int(coord[4]+(coord[2]*coord[1]*((1-finalnishoda[2])/2))+(coord[1]*finalnishoda[2]*finalnishoda[1])),   int(coord[3]+(coord[2]*coord[0]*((1-finalnishoda[2])/2))+(coord[0]*finalnishoda[2]*finalnishoda[1]))]
print(' '.join(str(cast) for cast in souradnice + [smer[1+finalnishoda[2]], finalnishoda[3]]))
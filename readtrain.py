import sys
if len(sys.argv)!=3: exit()
rad=sys.argv[1];tab=sys.argv[2];vysledek=[]
def mira_shody(a=str,b=str,count=0):
    if len(a)==len(b): 
        count = sum(a[i] == b[i] for i in range(len(a)))
    return count
with open(rad,'r',encoding='utf-8') as f1, open(tab,'r',encoding='utf-8') as f2:lines_rad=[line.strip() for line in f1 if line.strip()];lines_tab=[line.strip() for line in f2 if line.strip()] 
for i,line in enumerate(lines_rad):nazev,casyneroz=line.split(";",1);casy=list(casyneroz.strip().split());lines_rad[i]=[nazev.strip(),casy]
for i,line in enumerate(lines_tab):casti=line.split();line_v2=[" ".join(casti[:-2])] + casti[-1:];lines_tab[i]=line_v2
for line_chybny in lines_tab:
    score=0
    for t, line_bez_chyb in enumerate(lines_rad):
        nazev_shoda=mira_shody(line_bez_chyb[0].strip(),line_chybny[0].strip());max_cas=0
        if nazev_shoda>score:
            score=nazev_shoda;nazev_index=t
            for c in range(len(list(line_bez_chyb[1]))):
                if mira_shody(line_bez_chyb[1][c],line_chybny[1])>max_cas: max_cas=mira_shody(line_bez_chyb[1][c],line_chybny[1]);cas_index=c
    vysledek.extend([lines_rad[nazev_index][0],lines_rad[nazev_index][1][cas_index]])
[print(f"{vysledek[i]}, {vysledek[i+1]}") for i in range(0, len(vysledek), 2)]
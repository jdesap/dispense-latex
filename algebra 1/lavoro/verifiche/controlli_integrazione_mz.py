"""Controlli finiti indipendenti delle identità coinvolte nella revisione."""
from pathlib import Path
from itertools import product
from math import gcd
import json

root=Path(__file__).resolve().parents[2]
U=set(range(4));sets=[{i for i in U if bits>>i&1} for bits in range(16)]
triples=0
for A,B,C in product(sets,repeat=3):
    A0=A-(B|C);B0=B-(A|C);C0=C-(A|B);T=A&B&C
    assert (A^B)-C==A0|B0
    assert C-(A^B)==C0|T
    assert A-(B^C)==A0|T
    assert (B^C)-A==B0|C0
    assert ((A^B)^C)==A0|B0|C0|T==(A^(B^C))
    triples+=1
maps=0;subsets=0
for nx,ny in product(range(4),repeat=2):
    X=set(range(nx));Y=set(range(ny))
    for vals in product(range(ny),repeat=nx):
        im=set(vals);inj=len(im)==nx;sur=im==Y
        def image(A):return {vals[x] for x in A}
        def preimage(B):return {x for x in X if vals[x] in B}
        xs=[{x for x in X if bits>>x&1} for bits in range(2**nx)]
        ys=[{y for y in Y if bits>>y&1} for bits in range(2**ny)]
        for A in xs:assert A<=preimage(image(A));subsets+=1
        for B in ys:assert image(preimage(B))==B&im;subsets+=1
        assert all(A==preimage(image(A)) for A in xs)==inj
        assert all(image(preimage(B))==B for B in ys)==sur
        maps+=1
powers=0
for na,nb in product(range(5),repeat=2):
    assert sum(1 for _ in product(range(nb),repeat=na))==nb**na
    powers+=1
reductions=0
for a,b in product(range(-40,41),repeat=2):
    if (a,b)==(0,0):continue
    d=gcd(a,b);assert gcd(a//d,b//d)==1;reductions+=1
for t in range(-20,21):assert (6+420*t)*72+(-1-72*t)*420==12
# Dipendenze e struttura dei sorgenti: non sostituiscono la lettura delle prove.
texts={p.name:'\n'.join(line.split('%',1)[0] for line in p.read_text().splitlines()) for p in (root/'capitoli').glob('*.tex')}
assert not any(x in texts['01-insiemi.tex'] for x in ['modulo','caratteristic','parità'])
assert 'A_0=X' not in texts['04-cardinalita.tex'] # vecchia prova CSB rimossa
assert 'T(\\varepsilon)' not in texts['04-cardinalita.tex'] # vecchia prova ternaria rimossa
assert 'B^A' in texts['04-cardinalita.tex']
report={'data':'2026-10-23','terne_insiemi':triples,'mappe_finite':maps,'sottoinsiemi_verificati':subsets,'conteggi_B_potenza_A':powers,'riduzioni_coprime':reductions,'famiglie_coefficienti_Bezout':41,'controlli_sorgenti':'superati','limite':'Controlli finiti e strutturali supplementari; nessuna certificazione formale delle prove generali.'}
(root/'lavoro/CONTROLLI_INTEGRAZIONE_MZ_2026-10-23.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False))

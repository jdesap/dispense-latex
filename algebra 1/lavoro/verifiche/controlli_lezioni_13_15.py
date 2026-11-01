"""Riscontri finiti sulle formule nuove e sugli esempi stampati; non prove dei teoremi."""
from pathlib import Path
import csv
import hashlib
import itertools
import json
import math
import re
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[2]

def run():
    congruenze = 0
    for m in range(2, 41):
        for a in range(-m, m+1):
            d = math.gcd(a, m)
            for b in range(-m, m+1):
                actual = [x for x in range(m) if (a*x-b) % m == 0]
                assert bool(actual) == (b % d == 0), (a,b,m)
                if actual:
                    x0 = actual[0]
                    expected = sorted({(x0+(m//d)*j) % m for j in range(d)})
                    assert actual == expected and len(actual) == d
                    # La divisione simultanea deve conservare le soluzioni intere.
                    for x in [-m-1, -1, 0, m//2, m, 2*m+1]:
                        assert ((a*x-b)%m==0) == (((a//d)*x-b//d)%(m//d)==0)
                congruenze += 1
    sistemi = 0
    for mods in [(3,4),(6,7),(3,5,7),(4,5,9)]:
        M = math.prod(mods)
        weights = [(M//m)*pow(M//m,-1,m) for m in mods]
        for residues in itertools.product(*(range(m) for m in mods)):
            x = sum(w*b for w,b in zip(weights,residues)) % M
            actual = [y for y in range(M) if all(y%m==b for m,b in zip(mods,residues))]
            assert actual == [x]
            sistemi += 1
    assert [x for x in range(84) if (15*x-6)%84==0] == [6,34,62]
    assert [x for x in range(12) if (3*x-6)%12==0] == [2,6,10]
    assert not any((3*x-2)%12==0 for x in range(12))
    assert [x for x in range(18) if (21*x-15)%18==0] == [5,11,17]
    assert [x for x in range(30) if (21*x-6)%30==0] == [6,16,26]
    assert not any((21*x-15)%18==0 and (35*x-21)%42==0 for x in range(126))
    assert [x for x in range(42) if (3*x-1)%7==0 and (5*x-3)%6==0] == [33]
    assert 35*2*2+21*3+15*2==233 and 233%105==23
    assert 6*6*5+7*3==201 and 201%42==33
    assert all(r==s*84+t*15 for r,s,t in [(84,1,0),(15,0,1),(9,1,-5),(6,-1,6),(3,2,-11),(0,-5,28)])
    # Unità e divisori dello zero in prodotti di campi, inclusi fattori uguali.
    prodotti = 0
    for p,q in itertools.product([2,3,5,7], repeat=2):
        elements=list(itertools.product(range(p),range(q)))
        for a,b in elements:
            inv=any(a*u%p==1 and b*v%q==1 for u,v in elements)
            zero=any((u,v)!=(0,0) and a*u%p==0 and b*v%q==0 for u,v in elements)
            assert inv==(a!=0 and b!=0)
            assert zero==(a==0 or b==0)
            prodotti+=1
    # Correlazione tra le sei classi e le coppie; tutte le operazioni della tabella.
    for a,b in itertools.product(range(6),repeat=2):
        for op in [lambda x,y:x+y,lambda x,y:x*y]:
            assert (op(a,b)%6%2,op(a,b)%6%3)==(op(a%2,b%2)%2,op(a%3,b%3)%3)
    units84=[1,5,11,13,17,19,23,25,29,31,37,41,43,47,53,55,59,61,65,67,71,73,79,83]
    assert units84==[a for a in range(84) if math.gcd(a,84)==1]
    # Formula inversa 2x2: prodotti con aggiunta verificati per entrambi i lati.
    matrici=0
    for a,b,c,d in itertools.product(range(-3,4),repeat=4):
        D=a*d-b*c
        assert (a*d-b*c,-a*b+b*a,c*d-d*c,-c*b+d*a)==(D,0,0,D)
        assert (d*a-b*c,d*b-b*d,-c*a+a*c,-c*b+a*d)==(D,0,0,D)
        if D==0:
            v=(-b,a) if (a,b)!=(0,0) else (-d,c) if (c,d)!=(0,0) else (1,0)
            assert v!=(0,0) and a*v[0]+b*v[1]==0 and c*v[0]+d*v[1]==0
        matrici+=1
    # Provenienze e testo precedente.
    sources=json.loads((ROOT/'fonti/manifest.json').read_text())
    for row in sources['fonti']+sources['serie_M-Z']['fonti']:
        saved=ROOT/row['file']
        assert hashlib.sha256(saved.read_bytes()).hexdigest()==row['sha256']
        assert saved.read_bytes()==Path(row['origine']).read_bytes()
    tables={}
    for name in ['COPERTURA.csv','CONFRONTO_MZ.csv','SCELTA_DIMOSTRAZIONI.csv']:
        with (ROOT/'lavoro'/name).open() as f:tables[name]=list(csv.DictReader(f))
    assert len(tables['COPERTURA.csv'])==97 and len(tables['CONFRONTO_MZ.csv'])==106
    units={row['id']:row for row in tables['SCELTA_DIMOSTRAZIONI.csv']}
    assert len(units)==len(tables['SCELTA_DIMOSTRAZIONI.csv'])
    for name in ['COPERTURA.csv','CONFRONTO_MZ.csv']:
        for row in tables[name]:assert all(x.strip() in units for x in row['unita_riesame'].split(';'))
    snapshot=ROOT/'lavoro/storico-prima-lezioni-13-15-2026-11-01'
    old=PdfReader(snapshot/'build/main.pdf');new=PdfReader(ROOT/'build/main.pdf')
    for source in (ROOT/'capitoli').glob('0[1-5]-*.tex'):
        assert source.read_bytes()==(snapshot/'capitoli'/source.name).read_bytes()
    for i in range(4,37):assert re.sub(r'\s+', '', old.pages[i].extract_text())==re.sub(r'\s+', '', new.pages[i].extract_text())
    tex='\n'.join(p.read_text() for p in (ROOT/'capitoli').glob('*.tex'))
    labels=re.findall(r'\\label\{([^}]+)\}',tex)
    refs=re.findall(r'\\(?:ref|eqref)\{([^}]+)\}',tex)
    assert len(labels)==len(set(labels)) and set(refs)<=set(labels)
    assert len(re.findall(r'\\begin\{esercizio\}',tex))==len(re.findall(r'\\begin\{svolgimento\}',tex))
    assert 'congruenti' not in tex.lower()
    result={'data':'2026-11-01','congruenze_testate':congruenze,'sistemi_CRT_testati':sistemi,'elementi_prodotti_campi':prodotti,'matrici_testate':matrici,'esempi_stampati':'tutti verificati','fonti_originali_identiche':30,'pagine_AL':97,'pagine_MZ':106,'unita':len(units),'unita_rinviate':[k for k,v in units.items() if v['capitolo']=='rinviato'],'capitoli_1_5':'sorgenti e testo PDF invariati','limite':'Riscontri finiti supplementari; le prove generali sono riesaminate manualmente nelle unità e non certificate da questi controlli.'}
    target=ROOT/'lavoro/CONTROLLI_LEZIONI_13-15_2026-11-01.json'
    target.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(result,ensure_ascii=False))

if __name__=='__main__':run()

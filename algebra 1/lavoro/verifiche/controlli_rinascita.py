"""Riscontri aritmetici supplementari; non certificano le dimostrazioni generali."""
from pathlib import Path
from math import gcd
import hashlib,json,re
root=Path(__file__).resolve().parents[2]
# Costruzione per induzione su a>=0, confronto con quoziente/resto dell'oracolo intero.
divisions=0
for B in range(1,41):
    q=r=0
    for A in range(201):
        assert (q,r)==divmod(A,B)
        assert A==B*q+r and 0<=r<B
        for sa in (1,-1):
            for sb in (1,-1):
                a,b=sa*A,sb*B
                if sa==1:qa,ra=q,r
                elif r==0:qa,ra=-q,0
                else:qa,ra=-q-1,B-r
                if sb==-1:qa=-qa
                assert a==b*qa+ra and 0<=ra<abs(b)
                assert ra==a%abs(b)
                assert qa==(a-ra)//b
                divisions+=1
        if r+1<B:r+=1
        else:q+=1;r=0
# Algoritmo esteso: ogni riga verificata rispetto agli argomenti originali e a gcd.
pairs=rows=0
for a in range(-100,101):
    for b in range(-100,101):
        if (a,b)==(0,0):continue
        A,B=abs(a),abs(b)
        r0,r1=A,B;s0,s1=1,0;t0,t1=0,1
        previous=None
        while r1:
            assert r0==s0*A+t0*B and r1==s1*A+t1*B
            assert gcd(r0,r1)==gcd(a,b)
            if previous is not None:assert r1<previous
            previous=r1
            q,r2=divmod(r0,r1)
            s2=s0-q*s1;t2=t0-q*t1
            assert r2==s2*A+t2*B and 0<=r2<r1
            r0,r1=r1,r2;s0,s1=s1,s2;t0,t1=t1,t2
            rows+=1
        assert r0==gcd(a,b)>0
        alpha=s0*(1 if a>=0 else -1);beta=t0*(1 if b>=0 else -1)
        assert alpha*a+beta*b==r0
        pairs+=1
# Tabella effettivamente stampata: controllo indipendente di tutte le righe.
table=[(72,1,0),(420,0,1),(72,1,0),(60,-5,1),(12,6,-1),(0,-35,6)]
assert all(r==s*72+t*420 for r,s,t in table)
assert 12==6*72+1*(-420)
# Politica sui prerequisiti del primo capitolo, esclusi i commenti di provenienza.
files={p.name:p.read_text() for p in (root/'capitoli').glob('*.tex')}
first='\n'.join(line.split('%',1)[0] for line in files['01-insiemi.tex'].splitlines())
assert not any(s in first for s in ['caratteristic','modulo','parità','\\chi','\\mathbb{Z}'])
assert all(t.count('\\begin{esercizio}')==t.count('\\begin{svolgimento}') for t in files.values())
report={'data':'2026-10-23','divisioni_confrontate':divisions,'dividendi_nonnegativi':'0..200','divisori_assoluti':'1..40','segni':'tutte quattro le combinazioni','coppie_euclide':pairs,'argomenti_euclide':'-100..100 escluso (0,0)','righe_ricorrenza_controllate':rows,'tabella_stampata_righe':len(table),'identita_coefficienti_e_segni':True,'prerequisiti_capitolo_1':True,'esercizi_con_svolgimento_separato':True,'sorgenti_sha256':{n:hashlib.sha256(t.encode()).hexdigest() for n,t in files.items()},'limite':'Riscontri finiti, non prove dei risultati generali. Il riesame delle dimostrazioni è documentato separatamente nelle 75 unità del registro.'}
(root/'lavoro/CONTROLLI_RINASCITA_2026-10-23.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k!='sorgenti_sha256'},ensure_ascii=False))

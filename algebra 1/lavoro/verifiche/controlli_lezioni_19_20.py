"""Riscontri esatti sugli esempi19–20; non certificano le prove generali."""
from pathlib import Path
from math import gcd,lcm
from itertools import permutations
import json
BASE=Path(__file__).resolve().parents[2]

def additive_order(a,n):
    return next(k for k in range(1,n+1) if k*a%n==0)
def multiplicative_order(a,n):
    v=1
    for k in range(1,n+1):
        v=v*a%n
        if v==1: return k
    raise AssertionError((a,n))
def compose(s,t): return tuple(s[t[i]-1] for i in range(len(s)))
def power(s,k):
    out=tuple(range(1,len(s)+1))
    for _ in range(k): out=compose(out,s)
    return out

def run():
    count=0
    for n in range(1,81):
        for a in range(-2*n,2*n+1):
            assert additive_order(a,n)==n//gcd(a,n)
            count+=1
        for d in range(1,n+1):
            if n%d==0:
                h={k*(n//d)%n for k in range(n)}
                assert len(h)==d
    subgroup_count=0
    for n in range(1,13):
        actual=set()
        for bits in range(1,1<<n,2):
            h=frozenset(i for i in range(n) if bits>>i&1)
            if all((a-b)%n in h for a in h for b in h): actual.add(h)
        expected={frozenset(k*(n//d)%n for k in range(n)) for d in range(1,n+1) if n%d==0}
        assert actual==expected
        subgroup_count+=len(actual)
    for m in range(1,41):
        for n in range(1,41):
            assert gcd(m,n)*lcm(m,n)==m*n
            for k in range(-100,101):
                assert (k%m==0 and k%n==0)==(k%lcm(m,n)==0)
    sigma=(4,3,2,1,5); rho=(5,1,2,4,3)
    assert power(sigma,2)==(1,2,3,4,5)
    assert power(rho,2)==(3,5,1,4,2)
    assert power(rho,3)==(2,3,5,4,1)
    assert power(rho,4)==(1,2,3,4,5) and power(rho,25)==rho
    assert compose((2,3,1,4,5),(1,2,3,5,4))==(2,3,1,5,4)
    assert compose((2,1,3,4,5),(1,2,4,3,5))==(2,1,4,3,5)
    embeds=0
    for m in range(1,5):
        for s in permutations(range(1,m+1)):
            for t in permutations(range(1,m+1)):
                ext=lambda x:x+tuple(range(m+1,6))
                assert ext(compose(s,t))==compose(ext(s),ext(t)); embeds+=1
    units16=[a for a in range(16) if gcd(a,16)==1]
    orders16=[multiplicative_order(a,16) for a in units16]
    assert orders16==[1,4,4,2,2,4,4,2]
    assert [pow(3,i,16) for i in range(4)]==[1,3,9,11]
    assert [5*pow(3,i,16)%16 for i in range(4)]==[5,15,13,7]
    assert {pow(3,i,16)*pow(5,j,16)%16 for i in range(4) for j in range(2)}==set(units16)
    assert [pow(3,k,17) for k in [2,4,8,16]]==[9,13,16,1]
    assert multiplicative_order(3,17)==16
    assert len({pow(3,i,17) for i in range(16)})==16
    assert [a for a in range(15) if gcd(a,15)==1]==[1,2,4,7,8,11,13,14]
    assert [a for a in range(16) if gcd(a,16)==1]==[1,3,5,7,9,11,13,15]
    divisors=[1,2,3,4,6,12]
    # Le sette frecce dei due reticoli: dZ⊆eZ e <[d]>⊆<[e]>.
    covers={(12,4),(12,6),(4,2),(6,2),(6,3),(2,1),(3,1)}
    actual={(d,e) for d in divisors for e in divisors if d!=e and d%e==0 and not any(k not in (d,e) and d%k==0 and k%e==0 for k in divisors)}
    assert actual==covers
    report={'data':'2026-11-13','esito':'superato','ordini_additivi_verificati':count,'sottogruppi_enumerati_esaustivamente_Zn_n_1_12':subgroup_count,'coppie_MCD_mcm':1600,'coppie_permutazioni_inclusioni':embeds,'esempi_permutazioni':'due ordiniS5 e due decomposizioniS5 esatti','unita16':units16,'ordini_unita16':orders16,'generatore_unita17':3,'frecce_reticoli_verificate':len(covers),'limite':'Riscontri finiti esatti supplementari; il riesame delle prove generali è manuale per unità, non certificazione formale.'}
    (BASE/'lavoro/CONTROLLI_LEZIONI_19-20_2026-11-13.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(report,ensure_ascii=False))
if __name__=='__main__': run()

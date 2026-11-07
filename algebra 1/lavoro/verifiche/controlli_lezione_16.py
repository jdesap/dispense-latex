"""Riscontri finiti degli esempi nuovi e verifica della copertura; non prova generale."""
from pathlib import Path
from math import gcd,prod
from collections import defaultdict
import csv,json,hashlib,re

B=Path(__file__).resolve().parents[2]
S=B/'lavoro/storico-prima-lezione-16-2026-11-05'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def rows(n):
 with (B/n).open(newline='') as f:return list(csv.DictReader(f))
def phi_count(n):return sum(gcd(a,n)==1 for a in range(n))
def phi_factors(n):
 factors=[];p=2
 while p*p<=n:
  if n%p==0:
   k=0
   while n%p==0:n//=p;k+=1
   factors.append(p**(k-1)*(p-1))
  p+=1
 if n>1:factors.append(n-1)
 return prod(factors)
for n in range(2,1001):assert phi_count(n)==phi_factors(n),(n,phi_count(n),phi_factors(n))
coprimi=0
for m in range(2,51):
 for n in range(2,51):
  if gcd(m,n)==1:
   assert phi_count(m*n)==phi_count(m)*phi_count(n)
   coprimi+=1
assert phi_count(600)==160
assert [phi_count(n) for n in range(2,9)]==[1,2,2,4,2,6,4]
assert phi_count(12)==4
assert phi_count(6)!=phi_count(3)+phi_count(3)
assert phi_count(4)!=phi_count(2)**2
# Tutte le fibre, comprese le vuote, della mappa non coprima.
fibres=defaultdict(list)
for a in range(12):fibres[a%2,a%6].append(a)
for e in range(2):
 for b in range(6):assert fibres[e,b]==([b,b+6] if e==b%2 else [])
assert sum(bool(v) for v in fibres.values())==6
assert [(a%2,a%3) for a in range(6)]==[(0,0),(1,1),(0,2),(1,0),(0,1),(1,2)]
assert (5%4,5%3)==(1,2) and (7%4,7%3)==(3,1)
assert [a for a in range(12) if (a%4,a%3)==(3,2)]==[11]
values=[(3*a+2)%36 for a in range(36)]
assert [a for a,v in enumerate(values) if v==5]==[1,13,25]
assert sorted(set(values))==list(range(2,36,3))
assert values[1]==values[13] and 0 not in values
# Caratteristiche: quattro punti, tutte le 256 coppie di sottoinsiemi.
for a in range(16):
 for b in range(16):
  ca=[(a>>x)&1 for x in range(4)];cb=[(b>>x)&1 for x in range(4)]
  assert [((a^b)>>x)&1 for x in range(4)]==[(v+w)%2 for v,w in zip(ca,cb)]
  assert [((a&b)>>x)&1 for x in range(4)]==[v*w for v,w in zip(ca,cb)]
# Conservazione degli edit preesistenti e riconciliazione pagina per pagina.
for p in sorted((B/'capitoli').glob('0[1-6]-*.tex')):assert sha(p)==sha(S/'capitoli'/p.name)
for p in ['main.tex','preambolo.tex']:assert sha(B/p)==sha(S/p)
m=json.loads((B/'fonti/manifest.json').read_text())
coverage=rows('lavoro/COPERTURA.csv');compare=rows('lavoro/CONFRONTO_MZ.csv');units=rows('lavoro/SCELTA_DIMOSTRAZIONI.csv')
assert len(coverage)==101 and len(compare)==110 and len(units)==126
assert len({x['id'] for x in units})==len(units)
ids={x['id'] for x in units}
for r in coverage+compare:
 for i in r['unita_riesame'].split(';'):
  if i.strip():assert i.strip() in ids,i
for sources,table,key in [(m['fonti'],coverage,'fonte'),(m['serie_M-Z']['fonti'],compare,'lezione')]:
 for s in sources:
  actual=[int(x['pagina']) for x in table if x[key]==(f"Lezione {s['numero']}" if key=='fonte' else str(s['numero']))]
  assert sorted(actual)==list(range(1,s['pagine']+1)),s
  assert sha(B/s['file'])==s['sha256']
assert not json.loads((B/'lavoro/MATERIALE_MZ_DA_RIPRENDERE.json').read_text())['unita']
t='\n'.join(p.read_text() for p in sorted((B/'capitoli').glob('*.tex')))
labels=re.findall(r'\\label\{([^}]+)\}',t);refs=re.findall(r'\\(?:eqref|ref)\{([^}]+)\}',t)
assert len(labels)==len(set(labels)) and set(refs)<=set(labels)
assert t.count('\\begin{esercizio}')==t.count('\\begin{svolgimento}')
assert 'congruenti' not in t
report={'data':'2026-11-05','stato':'pass','controlli_finiti_supplementari':{'eulero_conteggio_vs_fattorizzazione':{'intervallo':[2,1000],'moduli':999},'moltiplicativita_coprimi':{'moduli':[2,50],'coppie_ordinate':coprimi},'caratteristiche':{'punti':4,'coppie_sottoinsiemi':256},'fibra_affine_36':[1,13,25],'immagine_affine_36':sorted(set(values)),'mappa_Z12_Z2_Z6':{'classi':12,'coppie_codominio':12,'fibre_non_vuote':6,'elementi_per_fibra':2},'phi600':160},'conservazione':{'capitoli_1_6_sorgenti_identici':True,'main_e_preambolo_identici':True},'copertura':{'pdf':m['totale_pdf'],'pagine':m['totale_pagine'],'righe_AL':len(coverage),'righe_MZ':len(compare),'unita':len(units),'rinvii':0},'struttura':{'capitoli':t.count('\\chapter{'),'sezioni':t.count('\\section{'),'sottosezioni':t.count('\\subsection{'),'figure_tikz':t.count('\\begin{tikzpicture}'),'prove':t.count('\\begin{proof}'),'esercizi':t.count('\\begin{esercizio}'),'svolgimenti':t.count('\\begin{svolgimento}'),'label_uniche':len(labels),'riferimenti_risolti':len(refs)},'limite':'Verifiche finite e tecniche supplementari: non sostituiscono il riesame manuale delle dimostrazioni per unità.'}
(B/'lavoro/CONTROLLI_LEZIONE_16_2026-11-05.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False,indent=2))

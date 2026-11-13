"""Riscontri finiti supplementari, conservazione e riconciliazione fonti17–18."""
from pathlib import Path
from itertools import permutations,product
from fractions import Fraction as F
from math import gcd
import re,csv,json,hashlib
B=Path(__file__).resolve().parents[2];S=B/'lavoro/storico-prima-lezioni-17-18-2026-11-11'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def comp(a,b):return tuple(a[i-1] for i in b)
def inv(a):return tuple(a.index(i)+1 for i in range(1,len(a)+1))
def power(a,k):
 v=tuple(range(1,len(a)+1));p=a if k>=0 else inv(a)
 for _ in range(abs(k)):v=comp(v,p)
 return v
s=(1,3,2,4);t=(4,2,1,3);r=(3,2,4,1)
assert power(s,2)==(1,2,3,4)
assert comp(s,t)==(4,3,1,2) and comp(t,s)==(4,1,2,3)
assert comp(r,s)==(3,4,2,1) and comp(s,r)==(2,3,4,1)
s=(2,3,4,1);t=(1,4,3,2)
assert comp(comp(t,s),inv(t))==(4,1,2,3)
assert comp(comp(s,t),inv(s))==(3,2,1,4)
p=(4,3,1,2,5)
assert [power(p,k) for k in range(4)]==[(1,2,3,4,5),p,(2,1,4,3,5),(3,4,2,1,5)]
assert power(p,4)==(1,2,3,4,5)
P=list(permutations(range(1,5)))
for a,b in product(P,repeat=2):assert inv(comp(a,b))==comp(inv(b),inv(a))
Q=list(permutations(range(1,4)));e=(1,2,3);tau=(2,1,3)
def subgroup(h):return e in h and all(comp(a,inv(b)) in h for a,b in product(h,repeat=2))
subsets=[{Q[i] for i in range(6) if mask>>i&1} for mask in range(64)]
subs=[h for h in subsets if subgroup(h)]
assert len(subs)==6
for h,k in product(subs,repeat=2):
 assert subgroup(h&k)
 assert subgroup(h|k)==(h<=k or k<=h)
 containing=[u for u in subs if h|k<=u];join=set.intersection(*containing)
 assert subgroup(join) and h|k<=join
for x in subsets:
 central={g for g in Q if all(comp(g,a)==comp(a,g) for a in x)}
 assert subgroup(central)
assert {g for g in Q if comp(g,tau)==comp(tau,g)}=={e,tau}
assert {g for g in Q if all(comp(g,a)==comp(a,g) for a in Q)}=={e}
for a in Q:
 for m,n in product(range(-4,5),repeat=2):assert comp(power(a,m),power(a,n))==power(a,m+n)
def affine(f,g):a,b=f;c,d=g;return a*c,a*d+b
def afinv(f):a,b=f;return 1/a,-b/a
A=[(F(a,2),F(b,3)) for a in [-3,-2,-1,1,2,3] for b in range(-2,3)]
for f in A:
 assert affine(f,afinv(f))==affine(afinv(f),f)==(1,0)
 for g in A:
  a,b=f;c,d=g
  assert (affine(f,g)==affine(g,f))==((1-c)*b==(1-a)*d)
  for x in [F(-2),F(0),F(3,2)]:assert affine(f,g)[0]*x+affine(f,g)[1]==a*(c*x+d)+b
  assert afinv(affine(f,g))==affine(afinv(g),afinv(f))
for a,b in A:
 h=(a,F(0));t=(F(1),b)
 assert affine(affine(h,t),afinv(h))==(1,a*b)
 assert affine(affine(t,h),afinv(t))==(a,b*(1-a))
for b in [F(0),F(1),F(-3,2)]:
 for f in A:
  commute=affine(f,(1,b))==affine((1,b),f)
  assert commute==(b==0 or f[0]==1)
assert affine((2,1),(1,2))==(2,5) and affine((1,2),(2,1))==(2,3)
for m,count in [(3,2),(25,20),(75,40),(13,12)]:assert sum(gcd(a,m)==1 for a in range(m))==count
# Conservazione: nessuna modifica a capitoli1–6, inclusioni principali o preambolo.
for p in (B/'capitoli').glob('0[1-6]-*.tex'):assert sha(p)==sha(S/'capitoli'/p.name)
for n in ['main.tex','preambolo.tex']:assert sha(B/n)==sha(S/n)
old=(S/'capitoli/08-eulero-e-gruppi.tex').read_text();new=(B/'capitoli/08-eulero-e-gruppi.tex').read_text()
old=old.replace('\\fonti{Lezione 16}','\\fonti{Lezioni 16, 17 e 18}').replace('% M–Z L16 p. 4 completa il tema avviato in A–L L16 p. 4.','% M–Z L16 p. 4; A–L L17 pp. 1–2 riprende la stessa prova e l\'esempio600.')
assert new.startswith(old.rstrip())
# Conservati gli edit delle altre materie nell'indice esterno.
oldstudy=(S/'DIMOSTRAZIONI_DA_STUDIARE.md').read_text();study=(B.parent/'DIMOSTRAZIONI_DA_STUDIARE.md').read_text()
for start,end in [('## Analisi 1','## Algebra 1'),('## Geometria 1','## Protocollo di aggiornamento')]:assert oldstudy.split(start)[1].split(end)[0]==study.split(start)[1].split(end)[0]
for link in re.findall(r'\]\(<([^>]+)>\)',study):assert (B.parent/link).exists(),link
# Righe e locator delle fonti: corrispondenza completa, unità valide e unico rinvio.
def rows(n):
 with (B/n).open(newline='') as f:return list(csv.DictReader(f))
m=json.loads((B/'fonti/manifest.json').read_text());units=rows('lavoro/SCELTA_DIMOSTRAZIONI.csv');al=rows('lavoro/COPERTURA.csv');mz=rows('lavoro/CONFRONTO_MZ.csv')
assert len(units)==147 and len(al)==119 and len(mz)==123
ids={u['id'] for u in units};assert len(ids)==147
for r in al+mz:
 for i in r['unita_riesame'].split(';'):
  if i.strip():assert i.strip() in ids,i
for series,table,key in [(m['fonti'],al,'fonte'),(m['serie_M-Z']['fonti'],mz,'lezione')]:
 for s in series:
  label=f"Lezione {s['numero']}" if key=='fonte' else str(s['numero'])
  assert sorted(int(r['pagina']) for r in table if r[key]==label)==list(range(1,s['pagine']+1))
  assert sha(B/s['file'])==s['sha256']
assert [u['id'] for u in units if u['capitolo']=='rinviato']==['D04']
# Solo sorgenti effettivamente inclusi nel volume.
active=[]
def visit(p):
 if p in active:return
 active.append(p)
 for child in re.findall(r'\\input\{([^}]+)\}',p.read_text()):visit(B/(child+'.tex'))
visit(B/'main.tex')
t='\n'.join(p.read_text() for p in active if p.parent.name=='capitoli')
labels=re.findall(r'\\label\{([^}]+)\}',t);refs=re.findall(r'\\(?:eqref|ref)\{([^}]+)\}',t)
assert len(labels)==len(set(labels)) and set(refs)<=set(labels)
assert t.count('\\begin{esercizio}')==t.count('\\begin{svolgimento}')
assert 'congruenti' not in t
report={'data':'2026-11-11','stato':'pass','controlli_supplementari':{'prodotti_S4':576,'sottoinsiemi_S3':64,'sottogruppi_S3':6,'coppie_sottogruppi_S3':36,'centralizzanti_S3':64,'identita_potenze_S3':486,'affinita_razionali':30,'coppie_affinita':900,'esempi_permutazioni_e_affini':'tutti i valori scritti verificati esattamente','unità_moduli':{'3':2,'25':20,'75':40,'13':12}},'conservazione':{'capitoli_1_6_sorgenti_identici':True,'main_e_preambolo_identici':True,'vecchia_parte_phi_preservata':True,'altre_materie_indice_dimostrazioni_identiche':True},'copertura':{'pdf':36,'pagine':242,'AL':119,'MZ':123,'unita_totali':147,'unita_integrate':146,'rinvii':['D04']},'struttura':{'capitoli':t.count('\\chapter{'),'sezioni':t.count('\\section{'),'sottosezioni':t.count('\\subsection{'),'figure_tikz':t.count('\\begin{tikzpicture}'),'prove':t.count('\\begin{proof}'),'esercizi':t.count('\\begin{esercizio}'),'svolgimenti':t.count('\\begin{svolgimento}'),'label_uniche':len(labels),'riferimenti_risolti':len(refs)},'limite':'Riscontri finiti e tecnici supplementari, non certificazione delle dimostrazioni generali; riesame manuale per unità nel registro prove.'}
(B/'lavoro/CONTROLLI_LEZIONI_17-18_2026-11-11.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');print(json.dumps(report,ensure_ascii=False,indent=2))

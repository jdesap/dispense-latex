"""Conservazione esatta del testo nella separazione del capitolo su Eulero."""
from pathlib import Path
import csv,hashlib,json,re,subprocess
from PIL import Image,ImageChops
from pypdf import PdfReader
B=Path(__file__).resolve().parents[2]
S=B/'lavoro/storico-prima-capitolo-eulero-2026-11-05'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
old=(S/'capitoli/07-anelli.tex').read_text();a=old.index('\\section{La funzione di Eulero}')
header='% !TeX root = ../main.tex\n\\chapter{Funzione di Eulero e gruppi}\\label{cap:eulero-gruppi}\n\\fonti{Lezione 16}\n\n'
assert (B/'capitoli/07-anelli.tex').read_text()==old[:a].rstrip()+'\n'
assert (B/'capitoli/08-eulero-e-gruppi.tex').read_text()==header+old[a:]
assert (B/'main.tex').read_text()==(S/'main.tex').read_text().replace('\\input{capitoli/07-anelli}\n','\\input{capitoli/07-anelli}\n\\input{capitoli/08-eulero-e-gruppi}\n')
assert sha(B/'preambolo.tex')==sha(S/'preambolo.tex')
assert sha(B/'fonti/manifest.json')==sha(S/'fonti/manifest.json')
for p in sorted((B/'capitoli').glob('0[1-6]-*.tex')):assert sha(p)==sha(S/'capitoli'/p.name)
t='\n'.join(p.read_text() for p in sorted((B/'capitoli').glob('*.tex')))
prev='\n'.join(p.read_text() for p in sorted((S/'capitoli').glob('*.tex')))
for env in ['proof','esercizio','svolgimento','definizione','esempio','proposizione','corollario','teorema']:
 assert t.count('\\begin{'+env+'}')==prev.count('\\begin{'+env+'}'),env
labels=re.findall(r'\\label\{([^}]+)\}',t);refs=re.findall(r'\\(?:eqref|ref)\{([^}]+)\}',t)
assert len(labels)==len(set(labels)) and set(refs)<=set(labels)
with (B/'lavoro/SCELTA_DIMOSTRAZIONI.csv').open(newline='') as f:units=list(csv.DictReader(f))
assert len(units)==126
for u in units:
 if u['id'] in ['D03','N21','N22','N23','N24','N25']:assert u['capitolo']=='8'
# Il volume ha una testata nuova, ma conserva anche l'impaginazione di tutti i capitoli1–7.
source=PdfReader(S/'build/main.pdf');current=PdfReader(B/'build/main.pdf')
assert len(source.pages)==len(current.pages)==58
out=Path('/private/tmp/algebra-cap8-conservazione');out.mkdir(exist_ok=True)
subprocess.run(['pdftoppm','-f','5','-l','56','-scale-to','1500','-png',str(S/'build/main.pdf'),str(out/'precedente')],check=True,capture_output=True)
for n in range(5,57):
 with Image.open(out/f'precedente-{n:02d}.png') as a,Image.open(Path('/private/tmp/algebra-verifica-finale/algebra 1/volume')/f'p-{n:02d}.png') as b:
  assert a.size==b.size and ImageChops.difference(a.convert('RGB'),b.convert('RGB')).getbbox() is None,n
 assert source.page_labels[n-1]==current.page_labels[n-1]
structure={'capitoli':t.count('\\chapter{'),'sezioni':t.count('\\section{'),'sottosezioni':t.count('\\subsection{'),'figure_tikz':t.count('\\begin{tikzpicture}'),'prove':t.count('\\begin{proof}'),'esercizi':t.count('\\begin{esercizio}'),'svolgimenti':t.count('\\begin{svolgimento}'),'label_uniche':len(labels),'riferimenti_risolti':len(refs)}
result={'data':'2026-11-05','stato':'pass','sezione_eulero_spostata_integralmente_senza_modifiche':True,'nessuna_nuova_teoria_dei_gruppi_aggiunta':True,'resto_capitolo7_identico':True,'capitoli_1_6_sorgenti_identici':True,'preambolo_e_manifest_fonti_identici':True,'unita_matematiche_precedenti_conservate':126,'unita_nuove':0,'numerazione_e_pixel_identici_capitoli_1_7':{'pagine_testo':52,'pagine_pdf':[5,56],'scala_render':1500},'struttura':structure,'snapshot':str(S.relative_to(B))}
(B/'lavoro/VERIFICA_CAPITOLO_EULERO_E_GRUPPI_2026-11-05.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(json.dumps(result,ensure_ascii=False,indent=2))

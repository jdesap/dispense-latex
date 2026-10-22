# Integrazione e revisione della lezione 7 — 21 ottobre 2026

## Fonte e confronto

Fonte acquisita da `/Users/jude/Downloads/Lezione_7.pdf` e conservata
senza modifiche in `fonti/Lezione 7.pdf`: 7 pagine manoscritte.
Lette visivamente tutte le pagine, comprese le continuazioni dei
ragionamenti e dei disegni tra le pagine 2–3, 3–4, 4–5 e 6–7.
Le sette nuove righe di `COPERTURA.csv` mappano ogni pagina ai moduli
attivi. Il manifest ora comprende sette PDF e 33 pagine di fonti.

## Organizzazione tematica

Resta un solo capitolo «Spazi vettoriali». Sono state separate:

1. Somme di sottospazi e somme dirette, dopo il sottospazio generato.
2. Indipendenza lineare, basi e coordinate, prima della dimensione.
3. Dimensione e teorema dello scambio.
4. Formula di Grassmann e sottospazi complementari, dopo le costruzioni
   del prodotto e del quoziente, conservando le prove già presenti.

Le definizioni prima inserite come raccordo sono state incorporate
nei primi due moduli e completate con la nuova fonte; eliminate le
ripetizioni nel modulo della dimensione e in quello di Grassmann.
Il modulo `01h-somme-grassmann-complementi.tex` è ora
`01h-grassmann-complementi.tex`; somma e somma diretta sono nel nuovo
`01b-somme-di-sottospazi.tex`. Il nuovo modulo
`01c-indipendenza-basi-coordinate.tex` precede `01c-basi-e-dimensione.tex`.
I prefissi dei moduli sono identificatori interni, non numeri di lezione.

## Verifica dei contenuti e delle prove

- Somma definita come span dell'unione e caratterizzazione `u+w`:
  dimostrate entrambe le inclusioni raggruppando combinazioni finite;
  conservate chiusura, minimalità ed esempio dei due assi.
- Generalizzazione a un numero finito di sottospazi e somma diretta
  definita tramite unicità delle componenti, come nella fonte.
- Criterio per due sottospazi `U∩W={0}`: ricontrollati entrambi i versi,
  senza ipotesi di dimensione finita. Svolto anche l'esercizio della
  prova alternativa: da `z≠0` nell'intersezione si ottengono le due
  scomposizioni `u+w=(u+z)+(w-z)`.
- Precisazione per più sottospazi: criterio della sola decomposizione
  nulla; prova sottraendo due scomposizioni. In nota, controesempio
  all'uso delle sole intersezioni a due a due per tre sottospazi.
- Indipendenza di un insieme anche infinito precisata con scelte finite
  di vettori distinti. In nota, distinzione tra insiemi e famiglie con
  ripetizioni; convenzioni per le famiglie vuote.
- Esclusione del vettore nullo dagli insiemi liberi e criterio di
  dipendenza dimostrato nei due versi; legittimità della divisione per
  un coefficiente non nullo nel campo. Incluso il caso di un solo vettore.
- Conservati i due esempi numerici in R³: `(1,1,1),(2,0,0),(4,0,0)` e
  `(1,2,3),(2,0,0),(3,2,3)`. Nel primo il coefficiente del primo vettore
  può essere nullo; nel secondo la relazione si risolve per ciascuno.
- Base come insieme libero di generatori; esistenza e unicità delle
  rappresentazioni giustificate separatamente.
- Base canonica in R²: prove di generazione e indipendenza. Esercizio
  in R^m svolto per componenti, con estensione esplicita a K^m.
- Coordinate definite rispetto a una base ordinata; esercizio di
  `w=(3,2)` svolto nella base canonica e nella base `((1,-1),(2,1))`.
  La fonte lascia da svolgere il sistema finale: qui è risolto e
  verificato, con coordinate `(-1/3,5/3)` e formule inverse generali
  `a=(x-2y)/3`, `b=(x+y)/3`. Queste provano anche che la famiglia è base.
- Ricontrollati i raccordi con scambio, dimensione, Grassmann e
  complementari dopo lo spostamento delle definizioni. Le dimostrazioni
  conservate continuano ad avere prima di sé le nozioni necessarie.

## Calcoli e controllo editoriale

Verificate con frazioni esatte entrambe le relazioni in R³, la
ricostruzione di `(3,2)` e l'inversa del sistema per le coordinate
mediante i vettori coordinati. Le prove universali sopra elencate
sono state controllate a mano: i calcoli finiti riguardano gli esempi.

Compilazione con `latexmk`: 29 pagine (4 preliminari e 25 di testo),
senza errori, avvisi, riferimenti indefiniti o segnalazioni di righe
fuori margine e spaziature. Indice aggiornato per argomento.
Aggiunti due TikZ: componenti nella base canonica e ricostruzione del
vettore mediante la base obliqua, compresa la componente negativa.
Verificate a risoluzione leggibile le nuove pagine, i raccordi e le
pagine di Grassmann/complementari; controllata l'intera impaginazione
attraverso tavole di tutte le 29 pagine. Corretti la nota spezzata e
il titolo di Grassmann isolato dalla sottovoce nell'indice.

Numeri delle lezioni soltanto sotto il titolo del capitolo;
precisazioni in note. Registri e numeri di pagina delle fonti esclusi
dal PDF. I sette PDF originali corrispondono alle impronte del manifest.

## Rapporto con la revisione precedente

Il resoconto `REVISIONE_MATEMATICA_2026-10-21.md` e il relativo JSON
rimangono una fotografia della versione precedente di 25 pagine.
Questa sessione aggiunge il confronto integrale della nuova fonte e la
revisione dei moduli modificati, non una nuova rilettura indipendente
di tutte le altre 26 pagine già confrontate nelle sessioni precedenti.
La versione corrente è identificata da `VERIFICA_LEZIONE_7_2026-10-21.json`.
La parte sui numeri complessi rimane in attesa della fonte dell'autore.

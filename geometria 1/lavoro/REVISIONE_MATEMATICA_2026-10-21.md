# Revisione matematica — 21 ottobre 2026

**Resoconto storico della versione di 25 pagine precedente alla consegna
della lezione 7.** Il controllo successivo delle parti modificate e della
nuova fonte è in `REVISIONE_LEZIONE_7_2026-10-21.md`; le impronte di
questo resoconto restano conservate senza riscriverne retroattivamente
i risultati.

## Ambito effettivo del controllo

Riletti tutti i dieci moduli di contenuto attivi, da `01a` a `01j`,
oltre al documento principale e al file che li riunisce nel capitolo.
Controllati gli enunciati, le ipotesi sul campo e sulla dimensione,
le implicazioni nelle dimostrazioni, i casi nulli, i sistemi, le
parametrizzazioni, gli esempi e le formule dei disegni.

Le sei fonti originali conservano le impronte SHA-256 del manifest.
Il confronto pagina per pagina delle fonti è quello registrato nelle
sessioni 1–6 e in `COPERTURA.csv`; questa sessione è una nuova revisione
matematica dei sorgenti attivi, non una seconda trascrizione integrale
indipendente delle 26 pagine originali.

## Errore corretto

**Definizione abbreviata di spazio vettoriale, nota alla definizione 1.1.**
Mancava l'assioma `1_K v = v`. L'elenco principale lo conteneva già,
ma la nota presentava come equivalente una definizione incompleta.
È stato aggiunto esplicitamente, preservando la formulazione della nota.

La condizione non discende dalle due distributività e dall'associatività
del prodotto per scalari: su un gruppo abeliano non nullo si potrebbe
porre `λ·v=0` per ogni scalare e vettore. Quell'operazione soddisfa tali
leggi, ma `1·v=0` non coincide con `v` per un vettore non nullo.
L'assioma dell'unità compare esplicitamente anche nella definizione 1.19
di [Sheldon Axler, Linear Algebra Abridged](https://linear.axler.net/LinearAbridged.pdf).

## Passaggi resi più espliciti

- **Corollario sulla cardinalità delle basi.** Prima di confrontare due
  basi finite, ora si giustifica che tutte le basi di uno spazio generato
  da `m` vettori sono finite: `m+1` elementi indipendenti violerebbero
  il teorema dello scambio. Il risultato era corretto; il passaggio
  intermedio non era scritto.
- **Campo degli esempi.** Specificato che i vettori geometrici del piano
  e le funzioni `R→R` considerate sono spazi su `R`, con scalari reali.
  Questo evita di leggere gli esempi come costruzioni su un campo `K`
  arbitrario senza averne definito un'azione sui reali.

## Contenuti ricontrollati

| Modulo | Controllo matematico |
|---|---|
| 01a | Assiomi, identità nulle e opposti, esempi, criterio di sottospazio, parabola, intersezione e controesempio per l'unione |
| 01b | Due esercizi sui generatori; esistenza del sottospazio generato; entrambe le inclusioni nella caratterizzazione per combinazioni finite; insieme vuoto |
| 01c | Indipendenza, coordinate uniche, esistenza di una base finita, caso dei polinomi, ogni passo dello scambio, cardinalità e dimensione |
| 01d | Estrazione e completamento, terminazione dei procedimenti, basi dei tre sottospazi di R⁴ e relazione fra i generatori |
| 01e | Eliminazione dei parametri e sufficienza delle due equazioni cartesiane |
| 01f | Assiomi per componenti, generazione e indipendenza della base del prodotto |
| 01g | Equivalenza, classi, buona definizione di entrambe le operazioni, assiomi, esistenza della base del sottospazio, generazione e indipendenza nel quoziente, casi estremi |
| 01h | Chiusura e minimalità della somma, prova di Grassmann, unicità della scomposizione, costruzione e non unicità dei complementari |
| 01i | Cinque equazioni della relazione, tre matrici, cartesiane, complementare, indipendenza di Z e calcolo di entrambe le intersezioni |
| 01j | Sottospazio dei polinomi, equazioni nelle due basi, base di W, cambio di coordinate e inverse, esempio finale |

Riscontro esterno degli assiomi e degli enunciati di dimensione con Axler:
definizione 1.19, risultati del capitolo 2 sulle basi e sulla dimensione,
formula 2.43 per la somma, formula 3.89 per il quoziente. Il testo di
Axler consultato è una versione abbreviata senza dimostrazioni; è stato
usato per confrontare definizioni ed enunciati. Le dimostrazioni della
dispensa sono state controllate nei loro passaggi.

## Verifiche aritmetiche aggiuntive

Con coefficienti razionali esatti, mediante sostituzioni e riduzione
di matrici, sono stati ricontrollati tutti gli esercizi numerici:

- Soluzioni dell'esercizio in R² e impossibilità dell'esempio in R³.
- Annullamento dei sistemi cartesiani sui vettori delle basi in R⁴,
  loro indipendenza e numero delle coordinate libere.
- Relazione `-2u1+3u2+u3=0` e operazioni su entrambi i blocchi delle
  matrici dell'esercizio in R⁵.
- Dimensioni `dim U=2`, `dim W=2`, `dim(U+W)=4`, `dim Z=3`,
  `dim(Z∩U)=dim(Z∩W)=1`.
- Equazioni dei polinomi, due polinomi della base aggiunta, cambio di
  coordinate e sua inversa.

Questi controlli confermano i calcoli specifici. La validità dei teoremi
generali dipende dalla revisione delle dimostrazioni, non da un insieme
finito di esempi.

## Output, stato e limiti

PDF ricompilato: 25 pagine, senza errori, avvisi, riferimenti indefiniti
o righe fuori margine. Controllate le pagine modificate a risoluzione
leggibile e l'intero flusso del volume tramite tavole delle pagine.
Le impronte della versione controllata sono in
`CONTROLLI_AGGIUNTIVI_2026-10-21.json`; cambi successivi ai sorgenti
richiedono un nuovo controllo delle parti interessate.

Non sono emersi altri errori nella revisione effettuata. Questo è un
controllo matematico manuale dell'assistente con riscontri mirati e
verifiche aritmetiche, non una prova formale dell'assenza di errori
residui o una validazione del docente. La parte sui complessi non è
compresa, perché deve ancora essere consegnata. Il controllo riguarda
la materia fornita, senza attestare la copertura dell'intero programma
d'esame.

# Registro delle sessioni

Questo file resta fuori dal PDF.

## Regole concordate nella dispensa di Analisi 1

- Titolo e docente sotto il titolo; autore nel campo autore.
- Indice per argomenti. I numeri delle lezioni compaiono solo sotto i
  macroargomenti, senza indicazioni di pagina nel PDF.
- Prosa autonoma, senza richiami narrativi alle lezioni; precisazioni
  necessarie in nota a piè di pagina.
- Tutti gli enunciati, le proprietà, le dimostrazioni, gli esempi e gli
  esercizi delle fonti vanno conservati. Si sciolgono abbreviazioni e
  passaggi sottintesi.
- TikZ quando aiuta a comprendere il contenuto.
- Registri e avanzamento esclusi dal PDF.
- Lavoro per sessioni: ogni sessione termina con una parte concreta,
  compilabile e controllata.
- Struttura modulare nella cartella `dispense latex`, con sorgenti e PDF
  finale disponibili per l'aggiornamento tramite la stessa repository.
- Un capitolo corrisponde a un macroargomento, non a una singola lezione.
  Sezioni e sottosezioni raccolgono i temi; le nuove lezioni si integrano
  nel capitolo pertinente.

## Ripartenza — 21 ottobre 2026

La prima stesura aveva concentrato sei PDF in un volume di 14 pagine.
Era stata dichiarata completa troppo presto: la trascrizione non era
stata verificata con la profondità richiesta, né era stata svolta per
sessioni. Quel PDF e i tre moduli successivi sono conservati in
`lavoro/bozze/`, con stato **non verificato**. La dispensa attiva è stata
ricondotta alla sola lezione 5.

## Sessione 1 — Lezione 5 — 21 ottobre 2026

Fonte: `fonti/Lezione_5.pdf`, 6 pagine manoscritte. Verifica visiva
pagina per pagina, confrontando definizioni, esempi, dimostrazioni e
l'esercizio della parabola con il sorgente ora chiamato
`capitoli/01a-spazi-e-sottospazi.tex`.

Copertura verificata:

1. Definizione di spazio vettoriale su un campo arbitrario, tipi delle
   due operazioni, sette assiomi e conseguenze immediate.
2. Vettori geometrici e regola del triangolo; `K` su se stesso ed
   estensioni di campi, inclusi gli esempi `R/Q` e `C/R`.
3. `K^m` con notazione per righe e colonne, `K[x]`, funzioni `R→R` e
   definizione di sottospazio.
4. Retta affine `a+b=1`, retta lineare `a+b=0`, primo quadrante e
   parabola `a²−2b=0`, con controesempio esplicito nell'esercizio.
5. Prova della chiusura dell'intersezione e controesempio per l'unione
   dei due assi coordinati.
6. Combinazioni lineari finite, rappresentazione di `(a,b)` mediante i
   vettori coordinati e definizione di insieme di generatori.

Ampliati i passaggi impliciti: distinzione fra somma nel campo e nello
spazio vettoriale; verifica per componenti e punto per punto;
dimostrazione del criterio di sottospazio; calcolo del termine misto
nella parabola; ruolo della combinazione lineare rispetto all'unione.
Schemi TikZ per somma geometrica, rette affini e unione degli assi.

Verifiche: compilazione completa con `latexmk`, indice aggiornato e PDF
di 7 pagine (frontespizio, indice, convenzioni e quattro pagine di testo).
Nel log non compaiono errori, avvisi, riferimenti indefiniti o righe
fuori margine. Controllate visivamente tutte le sette pagine e i tre
schemi TikZ; corretto un salto che lasciava il disegno dell'unione
isolato all'inizio della pagina seguente. Titolo e autore verificati
nei metadati del PDF. Il PDF contiene soltanto la lezione 5.

**Sessione 1 conclusa.**

Le altre fonti restano in attesa di integrazione, anche se ne esiste
una bozza preliminare. La parte sui complessi verrà integrata quando
sarà consegnata.

## Sessione 2 — Lezione 6 — 21 ottobre 2026

Fonte: `fonti/Lezione_6.pdf`, 2 pagine manoscritte, confrontate
visivamente con il sorgente ora chiamato
`capitoli/01b-sottospazio-generato.tex`.

- Svolti entrambi gli esercizi iniziali: soluzione per ogni `(x,y)`
  nell'esempio di `R²` e vettore non rappresentabile nell'esempio di
  `R³`. Esplicitata anche l'equazione che tutte le combinazioni del
  secondo esempio soddisfano.
- Definito il sottospazio generato come il più piccolo sottospazio che
  contiene `S`; giustificata l'esistenza tramite intersezione; trattati
  i casi `S` già sottospazio e `S` vuoto.
- Dimostrata in entrambe le inclusioni l'uguaglianza fra sottospazio
  generato e combinazioni lineari finite, chiarendo la somma vuota,
  la chiusura delle operazioni e la minimalità.
- Aggiunto uno schema TikZ per visualizzare l'inclusione
  `S ⊆ ⟨S⟩ ⊆ W`.

Compilazione completa con `latexmk`: PDF di 9 pagine complessive,
indice aggiornato, senza errori, avvisi, riferimenti indefiniti o righe
fuori margine. Controllati visivamente l'indice e le due pagine della
nuova sezione. Rimossa una pagina finale quasi vuota prodotta dalla
prima impaginazione. Il PDF attivo comprende soltanto le lezioni 5 e 6.

**Sessione 2 conclusa.**

## Revisione della struttura — 21 ottobre 2026

Su indicazione dell'autore, eliminate le divisioni in capitoli che
seguivano i numeri delle lezioni. Il PDF ha ora un unico capitolo,
«Spazi vettoriali», con le sezioni «Struttura e modelli», «Sottospazi»
e «Generatori e sottospazio generato», articolate in sottosezioni.
I riferimenti alle lezioni 5 e 6 compaiono una sola volta sotto il
titolo del capitolo. I due sorgenti restano separati per consentire
aggiornamenti locali. Compilazione e controllo visivo completati:
PDF di 8 pagine, indice tematico aggiornato, nessun avviso nel log.

## Sessione 3 — Lezione 8 — 21 ottobre 2026

Fonte: `fonti/Lezione_8.pdf`, 3 pagine manoscritte, confrontate
visivamente con `capitoli/01c-basi-e-dimensione.tex`. Il nuovo
sorgente è incluso nel capitolo tematico «Spazi vettoriali»; la
provenienza sotto il titolo del capitolo è ora «Lezioni 5, 6 e 8».

- Definiti gli spazi finitamente generati; spiegati `K^m` e il
  controesempio `K[x]`, con la prova basata sul massimo grado dei
  generatori ipotetici.
- Enunciato e dimostrato il teorema dello scambio: a ogni sostituzione
  resta una famiglia di generatori; il coefficiente di un vecchio
  generatore deve essere non nullo per l'indipendenza dei nuovi.
  Trattati anche i casi vuoti.
- Dimostrato il corollario sul numero di vettori di due basi,
  applicando il teorema nei due versi. Definita la dimensione e
  verificato `dim K^m=m` mediante generazione e indipendenza dei
  vettori coordinati.
- Poiché le definizioni di indipendenza e base sono presupposte dalla
  fonte ma non compaiono nei PDF consegnati, inserito un raccordo
  autonomo: definizioni, criterio per eliminare un vettore dipendente,
  unicità delle coordinate ed esistenza di una base finita a partire
  da generatori finiti. Questa integrazione serve a rendere leggibili
  il teorema e la dimensione senza presumere contenuti non forniti.

Compilazione completa con `latexmk`: PDF di 10 pagine complessive,
indice aggiornato, senza errori, avvisi, riferimenti indefiniti o
righe fuori margine. Controllate visivamente le pagine nuove e il
passaggio dal sottospazio generato alla nuova sezione. Nessun registro
o riferimento a pagine delle fonti nel PDF.

**Sessione 3 conclusa.** Prossima sessione: lezione 9.

## Sessione 4 — Lezione 9 — 21 ottobre 2026

Fonte: `fonti/Lezione_9.pdf`, 4 pagine manoscritte, confrontate
visivamente con `capitoli/01d-estrazione-e-basi-di-sottospazi.tex`.
Il sorgente continua il capitolo «Spazi vettoriali» nelle sezioni
tematiche «Estrazione e completamento di basi» e «Basi di sottospazi
di R⁴». La provenienza sotto il titolo del capitolo è ora
«Lezioni 5, 6, 8 e 9».

- Dimostrati i due corollari: eliminazione di un generatore ridondante
  con sostituzione esplicita in una combinazione qualsiasi;
  completamento di una famiglia indipendente scegliendo vettori
  esterni allo span, con terminazione garantita dallo scambio.
- Svolto l'esercizio del sottospazio di `R^4` definito da due
  equazioni: parametri liberi, due vettori generatori, indipendenza
  per coordinate e dimensione `2`.
- Svolto l'esercizio con tre generatori: sistema delle relazioni,
  identità `-3v1+v2+2v3=0`, eliminazione del generatore ridondante,
  prova esplicita dell'indipendenza dei due restanti e dimensione.
- Svolta la seconda parte dell'esercizio: parametrizzazione di `W`,
  scelta dei parametri `(1,0)` e `(0,1)`, verifica di generazione e
  indipendenza, dimensione `2`.

Compilazione completa con `latexmk`: PDF di 12 pagine complessive,
indice aggiornato, senza errori, avvisi, riferimenti indefiniti o
righe fuori margine. Controllate visivamente le due pagine nuove,
la pagina precedente e l'indice. Nessun numero di lezione introdotto
nel corpo delle sezioni; nessun registro o riferimento alle pagine
delle fonti nel PDF.

**Sessione 4 conclusa.** Prossima sessione: lezione 10.

## Sessione 5 — Lezione 10 — 21 ottobre 2026

Fonte: `fonti/Lezione 10.pdf`, 5 pagine manoscritte, confrontate
visivamente con tre moduli tematici: `01e-equazioni-cartesiane.tex`,
`01f-prodotti.tex` e `01g-quozienti.tex`, nella cartella `capitoli/`.
La dispensa continua a contenere un unico capitolo, «Spazi vettoriali»;
la provenienza sotto il suo titolo include ora la lezione 10.

- Pagina 1: conservato l'enunciato con i tre generatori; ricavata
  la parametrizzazione dalla base di due vettori, eliminati i due
  parametri e verificata anche la sufficienza delle equazioni
  cartesiane. Il tema prosegue la sezione sui sottospazi di `R^4`.
- Pagina 2: definiti prodotto cartesiano e operazioni; svolta la
  verifica degli assiomi lasciata per esercizio nella fonte.
  Costruita una base del prodotto, con prove esplicite di generazione
  e indipendenza, e dedotta la somma delle dimensioni.
- Pagina 3: definita l'equivalenza modulo un sottospazio e verificate
  riflessività, simmetria e transitività; definiti classi, rappresentanti
  e insieme quoziente. Esplicitate la forma `v+W` e la condizione
  di uguaglianza tra classi. Sviluppato il controllo sui rappresentanti
  diversi per la somma.
- Pagina 4: completati i controlli di buona definizione per somma e
  prodotto per scalari; verificati gli assiomi del quoziente, con
  elemento nullo e opposti. Avviata la prova della dimensione tramite
  una base di `W` completata a una base di `V`, mostrando la generazione
  del quoziente.
- Pagina 5: completata l'indipendenza delle classi della base e
  dedotta `dim(V/W)=dim V-dim W`.

Chiariti anche l'esistenza di una base finita del sottospazio e i
casi estremi `W={0}` e `W=V`. Aggiunti un esempio in `R^2`, uno
schema TikZ delle classi come rette orizzontali e una precisazione
in nota sulla classe come sottoinsieme di `V` ed elemento di `V/W`.

Verifiche: compilazione completa con `latexmk`, PDF di 17 pagine
complessive, indice tematico aggiornato, nessun errore, avviso,
riferimento indefinito o riga fuori margine. Controllate visivamente
le cinque pagine nuove, la pagina di raccordo precedente, l'indice
e il titolo del capitolo. Dopo la rifinitura del simbolo di fine
dimostrazione, ricompilata e ricontrollata la pagina interessata.
Nessun registro o riferimento alle pagine delle fonti nel PDF.

**Sessione 5 conclusa.** Prossima sessione: lezioni 11–12.

## Sessione 6 — Lezioni 11–12 — 21 ottobre 2026

Fonte: `fonti/Lezione 11_12.pdf`, 6 pagine manoscritte, confrontate
visivamente con tre moduli tematici nella cartella `capitoli/`:
`01h-somme-grassmann-complementi.tex`, `01i-costruzioni-in-r5.tex`
e `01j-equazioni-di-polinomi.tex`. Tutti sono inclusi nel capitolo
«Spazi vettoriali», la cui provenienza ora comprende anche le lezioni
11 e 12.

- Pagine 1–2: enunciato e prova completa di Grassmann, con espansione
  dei vettori della somma, prova dell'indipendenza della famiglia
  costruita e conteggio delle dimensioni. Inserite come raccordo le
  definizioni di somma e somma diretta, con proprietà di sottospazio,
  minimalità e unicità della scomposizione. Definiti i complementari,
  dimostrata l'esistenza in dimensione finita ed esplicitata la non
  unicità con un esempio e uno schema TikZ.
- Pagine 2–3: conservato l'enunciato dell'esercizio in `R^5` con
  tutte le quattro richieste e la data dell'esame in nota.
  Verificati appartenenza dei generatori a `V` e dimensione di `V`.
  Risolto il sistema delle relazioni, controllata l'indipendenza
  della base estratta e riprodotte tutte e tre le matrici del
  metodo alternativo, spiegando il ruolo del blocco identità.
- Pagine 3–4: svolte tutte le sostituzioni per eliminare i parametri,
  ottenute le tre equazioni cartesiane e verificato il viceversa.
  Costruito lo stesso complementare della fonte e risolto il sistema
  che prova l'indipendenza dei quattro vettori in `V`.
- Pagine 4–5: costruito `Z` con i vettori della fonte, dimostrata
  l'indipendenza e calcolate esplicitamente entrambe le intersezioni.
  Precisato in nota perché scegliere il terzo vettore esterno
  separatamente a `U` e `W` non sarebbe sufficiente.
- Pagine 5–6: conservate le due richieste dell'esercizio sui
  polinomi. Ricavate le equazioni nelle due basi; verificate la
  proprietà di sottospazio e la seconda base mediante formule di
  passaggio e inverse. Aggiunti il calcolo di una base del sottospazio
  e un esempio del medesimo polinomio espresso nelle due coordinate.

Controlli aritmetici indipendenti con frazioni esatte: relazione di
dipendenza, operazioni sulle righe, equazioni cartesiane di `U`,
dimensioni di `U`, `W`, `U+W` e `Z`, dimensioni delle due intersezioni,
formule del cambio di coordinate e polinomi della base aggiunta.
Tutti i controlli sono riusciti.

Verifiche editoriali: compilazione completa con `latexmk`, PDF di
25 pagine complessive (21 di testo e 4 preliminari). Controllate
visivamente le nuove pagine, il raccordo con il quoziente, le due
pagine dell'indice e la provenienza sotto il titolo del capitolo.
Corretta una riga fuori margine; raggruppate nell'indice le voci
dell'esercizio in `R^5`. Ricompilazione finale senza errori, avvisi,
riferimenti indefiniti, righe fuori margine o spaziature segnalate.
Registri e riferimenti alle pagine delle fonti restano fuori dal PDF.

**Sessione 6 conclusa.** Tutte le 26 pagine dei sei PDF consegnati
sono integrate e registrate come verificate. La parte sui numeri
complessi resta in attesa della consegna dell'autore.

## Revisione matematica — 21 ottobre 2026

Riletti tutti i moduli attivi, ricostruiti i passaggi delle prove e
rifatti i calcoli degli esercizi con aritmetica razionale esatta.
Corretto l'assioma dell'unità mancante nella definizione abbreviata
in nota; completato il passaggio sulla finitezza delle basi; precisato
il campo reale in due esempi. Resoconto, ambito e limiti in
`REVISIONE_MATEMATICA_2026-10-21.md`; risultati e impronte della
versione controllata in `CONTROLLI_AGGIUNTIVI_2026-10-21.json`.
PDF di 25 pagine, ricompilato senza errori o avvisi e controllato
visivamente nelle parti modificate. Fonti originali integre.

## Sessione 7 — Integrazione della lezione 7 — 21 ottobre 2026

Nuova fonte: `fonti/Lezione 7.pdf`, 7 pagine, consegnata dopo le
sessioni precedenti. Confronto visivo integrale, con copertura di
ogni pagina registrata in `COPERTURA.csv`.

Integrati somme di sottospazi, generalizzazione e somme dirette;
entrambi i versi del criterio dell'intersezione nulla e l'esercizio
della dimostrazione alternativa; insiemi liberi e criterio di
dipendenza con prova; i due esempi in R³; basi e unicità delle
rappresentazioni; base canonica in R² e relativo disegno; esercizio
in R^m; coordinate ed esercizio del vettore `(3,2)` in due basi.
Svolte tutte le verifiche lasciate aperte e aggiunti due schemi TikZ.

Su autorizzazione dell'autore, riorganizzati i moduli per argomento:
somme prima dell'indipendenza; basi e coordinate prima della
dimensione; Grassmann e complementari conservati nelle sezioni
successive. I raccordi aggiunti quando la fonte mancava sono stati
fusi con la nuova trattazione, eliminando doppioni. Unico capitolo
«Spazi vettoriali», lezioni indicate soltanto sotto il titolo.

Ricontrollate le nuove prove e i raccordi. Verificati con frazioni
esatte i due esempi in R³ e le coordinate `(-1/3,5/3)`, comprese le
formule inverse del sistema generale. Compilazione senza errori o
avvisi: **29 pagine**, di cui 25 di testo e 4 preliminari.
Controllo visivo delle nuove pagine e dei raccordi e tavole dell'intero
volume; sistemate una nota spezzata e una voce isolata nell'indice.

Manifest aggiornato: **7 PDF e 33 pagine di fonti**, tutti integri.
La precedente revisione resta storica; ambito e risultati di questa
integrazione in `REVISIONE_LEZIONE_7_2026-10-21.md`, impronte della
versione corrente in `VERIFICA_LEZIONE_7_2026-10-21.json`.

**Sessione 7 conclusa.** Restano da consegnare i materiali sui complessi.

## Esportazione automatica dei capitoli — 22 ottobre 2026

Attivata la configurazione condivisa della raccolta: ogni Salva/Build
riuscito esporta i capitoli numerati in `build/capitoli/`, oltre al
volume completo. Capitoli riconosciuti dai segnalibri, senza elenchi
manuali; testi, disegni e numerazione provengono dalle stesse pagine
del volume. Nessun contenuto matematico modificato in questa sessione.
Verificata l'identità di tutti i flussi di pagina e del testo, la
numerazione e i link alle note; controllato il rendering della prima
pagina di ogni estratto. Risultati comuni in
`../strumenti/VERIFICA_ESPORTAZIONE_2026-10-22.json` rispetto alla materia.
Copie annotate in Goodnotes separate dai file rigenerati; le
annotazioni non vengono riallineate automaticamente dopo riscritture.
Modello e regole predisposti anche per le nuove materie, inclusa Algebra.


## Revisione editoriale — sessione 01, 22 ottobre 2026

Indice stampato limitato a capitolo e sezioni; sottosezioni conservate
nel corpo e nei segnalibri. La revisione editoriale del contenuto di
Spazi vettoriali è programmata in quattro sessioni a partire dalla 02.
Compilazione e verifica degli estratti completate. Piano e resoconto
comuni in `../../lavoro/revisione-editoriale/`.


## Revisione editoriale — sessione 02, 22 ottobre 2026

Revisionate integralmente le sezioni 1.1–1.4: struttura, modelli,
sottospazi, generatori, sottospazio generato, somme e somme dirette.
Dimostrazioni organizzate per idee e direzioni; esempi strutturati;
prosa su una riga per paragrafo. Numerazione e TikZ conservati.
Rimossi i rientri di prima riga e ridotti quelli degli elenchi nel
preambolo. Compilazione ed estratti verificati. Resoconto comune in
`../../lavoro/revisione-editoriale/SESSIONE_02.md`.


## Revisione editoriale — sessione 03, 22 ottobre 2026

Completate le sezioni 1.5–1.8, comprese le cartesiane. Resoconto e checkpoint in `../../lavoro/revisione-editoriale/`. Prove strutturate per idee, sorgenti ripuliti, esempi verificati, compilazioni ed estratti controllati.


## Revisione editoriale — sessione 04, 22 ottobre 2026

Completate le sezioni 1.9–1.10: prodotti e quozienti, con prove strutturate e verifica della buona definizione. Compilazioni ed estratti controllati; resoconto in `../../lavoro/revisione-editoriale/SESSIONE_04.md`.


## Revisione editoriale — sessione 05, 22 ottobre 2026

Completate Grassmann, complementari e tutti gli esercizi finali: Spazi vettoriali interamente revisionato. PDF di 28 pagine, estratto di 25. Verifiche matematiche, compilazione, contenuti, numerazione, link e ispezione visiva completati. Resoconto in `../../lavoro/revisione-editoriale/SESSIONE_05.md`.


## Revisione editoriale — verifica conclusiva, 22 ottobre 2026

Revisione integrale conclusa. Controllati sorgenti attivi, indici, provenienza, fonti integre, compilazione condivisa e compilatore integrato; verificati contenuto, numerazione e collegamenti degli estratti. Ispezione visiva finale dei preliminari e dell’intero flusso delle pagine; nessun errore o avviso LaTeX. Resoconto e limiti in `../../lavoro/revisione-editoriale/RESOCONTO_FINALE.md`; impronte correnti in `../../lavoro/revisione-editoriale/VERIFICA_CONCLUSIVA.json`. Le copie annotate non sono state modificate.


## Stile visivo — sessione 12, 22 ottobre 2026

Applicati rientro di 4 mm e spaziatura interna alle prove, etichette colorate per i diversi ambienti e formule guida in riquadri sottili. Formule, calcoli, note, label e numerazione conservati; compilazioni condivise e integrate riuscite, estratti verificati. Analisi resta di 54 pagine; Geometria passa a 29 (26 per Spazi vettoriali). Cambia l’impaginazione interna dei capitoli; copie annotate separate e non modificate. Parametri nei preamboli dalla riga 49. Resoconto e verifiche in `../../lavoro/revisione-editoriale/SESSIONE_12.md` e `VERIFICA_STILE_12.json` nella stessa cartella comune.

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


## Stile visivo — sessione 13, 22 ottobre 2026

Applicate barre laterali ai diversi ambienti, intestazioni nere e numeretti delle note blu elettrico in corpo e a piè di pagina. Esempi non numerati con due punti. Conservati rientro e fasi delle prove; rifiniti spazi dei display e cambi pagina. Contenuti invariati salvo la punteggiatura di un titoletto in Topologia. Compilazioni condivise e integrate riuscite senza avvisi LaTeX; tutti gli estratti e le 83 pagine controllati. Volumi di 54 e 29 pagine, estratti invariati per lunghezza; copie annotate non modificate. Parametri nei preamboli dalla riga 51; resoconto e verifiche in `../../lavoro/revisione-editoriale/SESSIONE_13.md` e `VERIFICA_STILE_13.json` nella stessa cartella comune.


## Stile visivo — sessione 14, 22 ottobre 2026

Barra allineata al testo normale e corpo degli ambienti rientrato di circa 3.4 mm. Compilazioni condivise e integrate riuscite senza avvisi LaTeX; formule, allineamenti e tutti gli estratti verificati. Contenuti invariati, con solo un correttivo di impaginazione prima del binomio. Analisi ha ora 55 pagine (sette nel capitolo 3); Geometria 29 (26 di Spazi vettoriali). Cambiano numerazione dei capitoli 4–7 di Analisi e disposizione interna degli ambienti. Copie annotate non modificate. Dettagli in `../../lavoro/revisione-editoriale/SESSIONE_14.md` e `VERIFICA_STILE_14.json` nella stessa cartella comune.


## Verifica dell’esportazione con Algebra — 23 ottobre 2026

Aggiornato l’esportatore condiviso per conservare anche i link a pagine esterne al capitolo come collegamenti remoti al volume completo. Rigenerati e verificati gli estratti: identità di tutti i flussi pagina, testo, formato, numerazione e rendering pixel; conservate tutte le annotazioni e verificate le destinazioni. Nessuna modifica ai contenuti o all’impaginazione del volume e nessuna copia annotata modificata. Risultati correnti in `../../strumenti/VERIFICA_ESPORTAZIONE_2026-10-23.json`. I collegamenti remoti richiedono un lettore compatibile e il volume nel percorso relativo.


## Rifiniture editoriali — sessione 15, 23 ottobre 2026

Uniformata ad Algebra la separazione fra consegna nell'ambiente `esercizio` e soluzione nell'ambiente `svolgimento`. Recuperati esercizi ancora mescolati alla spiegazione e svolgimenti senza ambiente; uniformati due alias e consegne incomplete. In Analisi riportati sei esempi manuali negli ambienti gialli e una prova degli intorni nell'ambiente delle dimostrazioni. Migliorati i raccordi per gli esercizi brevi e per la densità; allineata la protezione delle note di Analisi a Geometria e Algebra.

Conservati tutte le formule precedenti, gli ambienti di calcolo, i 47 TikZ complessivi, note, label e sequenza degli enunciati numerati. Compilazione condivisa e integrata riuscite senza avvisi LaTeX; tutti gli otto estratti verificati, anche pixel per pixel e nei collegamenti. Analisi passa da 55 a 56 pagine: capitolo 4 di 12 pagine, numerazione dei capitoli 5–7 spostata di una pagina; Geometria resta di 29 pagine, con 26 per Spazi vettoriali. Cambia anche la disposizione interna di alcune pagine. Copie annotate non modificate.

Regola aggiunta ad `AGENTS.md` e `MASTER_PROMPT.md`. Resoconto e verifiche in `../../lavoro/revisione-editoriale/SESSIONE_15.md` e `VERIFICA_STILE_15.json` nella cartella comune. Le modifiche sono editoriali: restano i limiti delle precedenti revisioni matematiche.


## Lezioni 13–15 — 28 ottobre 2026

Confrontate visivamente tutte le 14 pagine dei tre nuovi PDF, copiati in
fonti con impronte nel manifest. Copertura aggiornata pagina per pagina.
Nuovo capitolo 2 «Sistemi lineari e matrici»: matrici e sistemi, Gauss,
forme a scala e pivot, basi tramite righe, prodotto e proprietà con prove,
trasposizione, inverse destre e sinistre e unicità, rango e uguaglianza
fra ranghi, soluzioni omogenee e traslazione, Rouché–Capelli con prova,
esercizio sul rango parametrico con tutti i casi.

Confronto con tutti i moduli attivi: sistemi per coordinate, basi e metodo
con blocco identità erano già presenti nel capitolo 1. Conservata lì la
trattazione degli esercizi; aggiunto un rinvio al nuovo capitolo nel metodo
matriciale. La nuova applicazione in R4 resta nel capitolo 2 per illustrare
Gauss, senza duplicare la teoria delle basi. La prova dei ranghi completa
l'anticipazione della lezione 13. Riprese sulle soluzioni accorpate nella
sezione tematica. Aggiunte giustificazioni delle operazioni, delle proprietà
della trasposta e del calcolo dell'inversa. Precisata la condizione sulle
righe nulle nella forma a scala. Come richiesto, trattazione soprattutto
su R e precisazione sui campi finiti soltanto in nota a Rouché–Capelli.

Controllati con frazioni sistema, prodotti e relazione fra generatori;
riletta la riduzione simbolica del parametro e controllata in cinque valori.
La prova dei ranghi esplicita l'invarianza di ogni relazione fra colonne,
evitando di assumere l'uguaglianza dei ranghi nel corso della dimostrazione.

Compilazione condivisa riuscita senza avvisi: 36 pagine. Estratti di 26 e
7 pagine, testo e flussi pagina identici al volume; controllo visivo di
indice, raccordo e tutte le pagine nuove. Capitolo 1: aggiunto un rinvio,
lunghezza invariata; capitolo 2 nuovo, pagine 27–33. Nessuna copia annotata
modificata. Risultati in VERIFICA_LEZIONI_13-15_2026-10-28.json.


## Lezioni 16–18 — 2 novembre 2026

Fonti: Lezione_16.pdf (7 pagine), Lezione_17.pdf (5), Lezione_18.pdf (6).
Tutte le 18 pagine sono state lette visivamente; copie originali conservate
in fonti, con hash SHA-256 verificati e manifest aggiornato. Il corpus
contiene ora 13 PDF e 65 pagine. Copertura puntuale in COPERTURA.csv.

### Confronto e collocazione

Confrontati i contenuti con tutti i moduli attivi dei capitoli 1 e 2.
Coordinate e unicità erano già trattate in 01c; somme dirette in 01b e
complementari in 01h; coordinate dei polinomi e loro passaggi in 01j.
La nuova teoria usa questi risultati senza riscriverne le prove: formalizza
l'isomorfismo delle coordinate e applica le somme dirette alle proiezioni.
Sistemi omogenei, rango e struttura delle soluzioni erano già presenti
in 02a–02c: conservati lì i metodi di calcolo e le prove; nel nuovo capitolo
sono reinterpretati come nucleo, immagine e fibre. Aggiunto in 02c un
rinvio al teorema della dimensione, e tenuto insieme il titolo del successivo
esercizio con consegna e avvio dello svolgimento.

Creato il capitolo 3 «Applicazioni lineari», macroargomento distinto dai
sistemi. La definizione di matrice anticipata nella lezione 16 è accorpata
con la trattazione completa della 17. La generazione dell'immagine tramite
immagini di una base, ripresa nella 18, è collegata alla prova della dimensione
e sviluppata nella sezione sul calcolo matriciale, senza duplicare la prova
astratta. La somma di applicazioni della 18 completa la definizione di Hom
anticipata nella 16. Il cambio di base comprende la definizione come matrice
dell'identità, entrambi i versi, le quattro identità delle coordinate e la
derivazione della formula generale. Provenienza soltanto sotto il capitolo;
registri e riferimenti alle pagine delle fonti esclusi dal volume.

### Contenuti e correzioni

Conservati definizioni, proprietà, esempi e richieste delle fonti. Esplicitati
i controesempi seno e potenze; la precisazione sul campo a due elementi resta
in nota. Svolte le prove lasciate per esercizio: linearità dell'inversa,
sottospazio immagine, isomorfismo dei coefficienti e delle coordinate,
proprietà della simmetria e matrice nelle basi canoniche. Teorema della
dimensione con completamento della base del nucleo e prove di generazione
e indipendenza. Hom dotato delle operazioni punto per punto; aggiunti la
compatibilità con gli scalari e il conseguente isomorfismo con le matrici.
Tre schemi TikZ ricostruiscono proiezione obliqua, simmetria e due sistemi
di coordinate per lo stesso vettore. La prova del criterio di iniettività
esplicita in testo le due preimmagini dello zero del disegno della fonte.

Corretto il refuso finale della lezione 17, pagina 5: la matrice nelle basi
assegnate è ((4;-1);(13/2;1)), con entrata (2,2) uguale a 1, come già risulta
dal sistema svolto nella stessa fonte. Le proprietà della simmetria sono
presentate su R; una nota precisa l'eccezione in caratteristica 2 per le
identità Im(id+sigma)=U e ker(id+sigma)=W. La formula generale di cambio di
basi è verificata anche riprendendo l'esercizio concreto.

### Verifiche e impaginazione

Controlli con frazioni esatte: immagini dei vettori di base, matrice nelle
basi assegnate, matrice canonica, inversa della matrice di coordinate,
formula di cambio di basi. Verificate idempotenza della proiezione,
involutività della simmetria e id+sigma=2pi in un esempio obliquo.
Rilette le dimostrazioni generali, incluse le direzioni dei cambi di basi
e l'ordine dei fattori nella composizione.

Compilazione con configurazione condivisa completata senza errori o avvisi.
Volume di 45 pagine: 3 preliminari e capitoli di 26, 7 e 9 pagine.
Verificati tutti gli estratti rispetto al volume: testo, flussi pagina,
formato, etichette di numerazione e rendering pixel identici; segnalibri
numerati presenti. Controllo visivo dell'indice, raccordo finale del
capitolo 2 e tutte le nove pagine nuove; ricontrollate le due pagine del
raccordo dopo aver eliminato il titolo isolato.

Il capitolo 1 conserva il contenuto e l'impaginazione; nel capitolo 2 cambia
il raccordo finale alle pagine 32–33, senza cambiare lunghezza. Il capitolo 3
occupa le pagine 34–42 del testo. Gli estratti sono stati rigenerati; nessuna
copia annotata modificata. Esiti e impronte correnti in
VERIFICA_LEZIONI_16-18_2026-11-02.json.


## Chiarimenti di notazione e diagrammi — 10 novembre 2026

Richiesta dell'autore: rendere espliciti simboli e oggetti introdotti,
mostrare la corrispondenza sistema–matrice, illustrare il prodotto righe per
colonne e chiarire l'isomorfismo delle coordinate, controllando sempre il
significato matematico e il rendering dei disegni.

Verificate le definizioni già esistenti: [v]_B era introdotto nella sezione
sulle coordinate del capitolo 1; I_n era descritto brevemente nelle proprietà
del prodotto nel capitolo 2. Rafforzate le definizioni locali per non imporre
la ricerca di un richiamo lontano. Nel capitolo 1 definiti anche l'alias
span e, al primo uso nel metodo matriciale, matrice identità e notazione R_i.
Nel capitolo 2 precisati a_ij, righe e colonne, R_i e sostituzioni di riga,
e il significato di ~ fra matrici. Evitato l'uso anticipato dell'apice T per
le colonne; la trasposta rimane definita nella sua sezione. I_n presentata
con matrice generale, dimensioni, definizione delle entrate e caso I_2,
senza introdurre il delta di Kronecker come ulteriore simbolo non spiegato.
Nel capitolo 3 definiti id_V e somma punto per punto prima delle proprietà
della simmetria; promemoria iniziale di I_n e [v]_B utile anche nell'estratto.

Riutilizzato il sistema già presente per mostrare, senza duplicare un
esercizio, la corrispondenza fra ogni riga della matrice completa e ogni
equazione. Spiegati barra dei termini noti, ordine delle incognite e
coefficienti nulli. Dopo Gauss riportato anche il sistema equivalente
rappresentato dall'ultima matrice.

Nuovo TikZ del prodotto: fattori di tipo m×n e n×p, riga i del primo fattore,
colonna j del secondo e posizione (i,j) nel risultato m×p evidenziate.
Il risultato è chiamato c_ij per distinguerlo dalle entrate a_ij del primo
fattore. Mostrati somma dei prodotti e calcolo numerico di c_12=7.
Le omissioni di righe e colonne sono dichiarate; la tabella non pretende
di essere una matrice numerica di tre righe e tre colonne.

Esplicitate la mappa c_B che legge i coefficienti e la sua inversa r_B
che ricostruisce il vettore. Verificate entrambe le composizioni e la
linearità. Distinti vettore in V e colonna in K^n e chiarito che le
parentesi con pedice non sono classi del quoziente. Nuovo schema delle
due mappe con domini, frecce e operazioni inverse; esempio del polinomio
2−3X+X² in entrambe le direzioni. Distinti n generatori da una base di n
elementi: esempio di R² generato da e1,e2,e1+e2 e due terne con la stessa
immagine. L'enunciato precedente richiedeva già dim V=n: l'ampliamento
chiarisce l'ipotesi e non sostituisce una dimostrazione errata.

Rilette le prove pertinenti e aggiornato DIMOSTRAZIONI_DA_STUDIARE.md:
isomorfismo delle coordinate ancora C, ricostruibile da esistenza e unicità;
collegamenti ai sorgenti e distinzione dai generatori ridondanti. Nessuna
priorità A/B modificata, nessun nuovo risultato assunto o rinviato e nessun
progresso di studio attribuito all'autore. Inserita in AGENTS.md la regola
per definizioni preventive e verifica dei diagrammi richiesta dall'autore.

Verifiche: calcoli con frazioni esatte per sistema e sistema ridotto,
esempio numerico del prodotto, ricostruzione dei coefficienti e controesempio
dei generatori. Riletti gli indici simbolici del prodotto e controllate
le direzioni delle mappe del TikZ. Ispezione visiva dei due nuovi disegni
ad alta risoluzione e del flusso di tutte le pagine dei capitoli 2–3;
ricontrollati i tre disegni preesistenti del capitolo 3, indice e raccordo
matriciale nel capitolo 1. Corretti titoli isolati e code di esempi.

Compilazione condivisa senza errori o avvisi: 47 pagine. Estratti di 26,
8 e 10 pagine. Testo, flussi pagina, formato, etichette e rendering pixel
di ogni estratto identici alle corrispondenti pagine del volume; segnalibri
presenti e percorsi dei link remoti controllati. Fonti originali integre.
Il capitolo 1 mantiene 26 pagine ma cambia l'impaginazione interna delle
parti chiarite; il capitolo 2 occupa le pagine 27–34 e il capitolo 3 le
35–44. Tutti gli estratti sono rigenerati, nessuna copia annotata modificata.
Esiti in VERIFICA_CHIARIMENTI_NOTAZIONI_2026-11-10.json.

## 10 novembre 2026 — Chiarimento locale della prova sui ranghi

Su richiesta dell’autore, esplicitato nel teorema 2.11 il passaggio dalla conservazione delle relazioni alla conservazione del rango per colonne e dal sottospazio delle colonne accorciate in K^r alla disuguaglianza c ≤ r. Nessun nuovo risultato o fonte; priorità A invariata nell’indice delle dimostrazioni, la cui idea decisiva è stata precisata. Compilazione senza avvisi, 47 pagine; estratti rigenerati (26, 8, 10 pagine). Controllate visivamente pagina 32 e successiva; rendering della pagina modificata identico nell’estratto del capitolo 2. Numerazione e confini dei capitoli invariati; cambia il testo di pagina 32.


## Lezioni 19–21 — 12 novembre 2026

Fonti lette visivamente pagina per pagina: Lezione_19.pdf (7 pagine),
Lezione_20.pdf (5), Lezione_21.pdf (4). Copie in fonti con impronte nel
manifest; tutte le 16 pagine registrate in COPERTURA.csv. Il corpus
contiene ora 16 PDF e 81 pagine; nessuna istruzione contenuta nei documenti
è stata trattata come richiesta dell'autore.

### Confronto integrale e collocazione

Confrontati tutti i moduli attivi dei tre capitoli, seguendo gli input dei
main. Il blocco identità era già usato nel capitolo 1 per conservare le
relazioni; il capitolo 2 definiva inverse, operazioni elementari e una breve
giustificazione del calcolo mediante Gauss. Quella giustificazione è stata
accorpata con la nuova spiegazione mediante matrici elementari, senza
conservarne un doppione. Definite E_ij e le tre matrici; provati effetto
sulle righe, inverse e ordine dei fattori; registrato BA=A′ mediante
(A affiancata a I). Conservati entrambi gli esempi numerici, con tutti gli
stadi della riduzione e la verifica dei prodotti.

Il criterio di invertibilità usa nucleo, immagine e teorema della dimensione
appena sviluppati nel capitolo 3: collocato dopo il teorema della dimensione,
con due schemi di funzioni finite e distinzione fra inverse unilatere e
bilatere. Il criterio del rango massimo per matrici quadrate è dedotto qui;
la parte computazionale nel capitolo 2 rinvia a questa sezione. La breve
anticipazione del duale in Hom è collegata al nuovo capitolo.

Il duale non è un nuovo spazio Hom da ricostruire: si usa la struttura già
provata, specializzando W=K. Base duale, biduale, annullatori e trasposta
formano il nuovo macroargomento «Dualità e applicazione trasposta» nel
capitolo 4. Le riprese di duale e base duale fra lezioni 19 e 20 sono fuse;
la dimensione del biduale usa la dimensione del duale, l'immagine della
trasposta usa la dimensione degli annullatori e rango–nullità. Il teorema
sulla matrice della trasposta rinvia alla trasposizione già definita nel
capitolo 2: nessuna nuova prova dell'uguaglianza dei ranghi per righe e
colonne. Le equazioni cartesiane studiate prima sono interpretate, con un
nuovo esempio in R³, come funzionali che annullano un sottospazio.

### Chiarimenti, completamenti e ambito

Definiti prima dell'uso E_ij, delta di Kronecker, funzionale lineare, base
duale, dualità bilineare, biduale e mappa alpha, annullatori nei due versi
e trasposta algebrica. Distinti funzionale, sua matrice-riga e sua colonna
di coordinate. La dualità non è un prodotto scalare; il simbolo perpendicolare
non identifica da solo l'ambiente. L'asterisco della trasposta non denota
una coniugazione complessa. Le basi duali e le dimensioni sono esplicitate
nel teorema che dà la matrice A^T.

Svolte le verifiche lasciate per esercizio: L-perpendicolare sottospazio
di V e doppio annullatore. La prova del doppio annullatore completa una
base di U aggiungendo il vettore esterno da separare, poi sceglie il suo
funzionale duale. Questa alternativa costruttiva è accorpata nell'indice
di studio al metodo della base adattata; non richiede una seconda prova
per dimensioni. Esplicitate buona definizione e linearità di alpha e f*.

Precisate le ipotesi finite per il criterio dimensionale di invertibilità,
l'isomorfismo con il biduale e le prove dimensionali degli annullatori e
dell'immagine della trasposta. La catena stretta delle dimensioni infinite
è riportata come risultato assunto, con dimensioni cardinali e usuali
ipotesi di scelta, e non è usata per le dimostrazioni finite. La costruzione
di un'inversa sinistra fra insiemi richiede dominio non vuoto; la scelta
generale di un'inversa destra è distinta dai due esempi finiti e segnalata
in nota. Per il prodotto scalare reale scelto, una nota ne dà definizione
e spiega perché induce un isomorfismo in dimensione finita.

Aggiornato DIMOSTRAZIONI_DA_STUDIARE.md con famiglie B motivate per registro
delle operazioni, valutazione su basi, annullatori e inclusione più dimensioni;
conseguenze C accorpate. Distinti i risultati assunti; preservati appunti
personali, altre materie e assenza di dichiarazioni di studio dell'autore.

### Verifiche

Controlli esatti riproducibili in lavoro/verifiche/lezioni_19_21.py, con esiti
in CONTROLLI_LEZIONI_19-21_2026-11-12.json: ogni matrice intermedia stampata,
BA=A′, entrambe le moltiplicazioni dell'inversa, tre matrici elementari e
relative inverse, due diagrammi di funzioni finite, base duale non canonica,
annullatore concreto e matrice della trasposta con identità di valutazione.
Rilette le prove astratte e gli indici, senza usare il solo calcolo di esempi
come prova dei risultati generali.

Quattro nuovi TikZ: registro delle operazioni sui due blocchi, due esempi
finiti nello stesso schema, mappa canonica al biduale con valutazione,
composizione che definisce la trasposta e verso contrario sui duali.
Verificati matematicamente e nel rendering; eliminate una freccia di
annotazione ambigua e spezzature segnalate da mdframed. Ricontrollati i
raccordi dopo le rifiniture; indice stampato in corpo piccolo per conservare
una pagina leggibile invece di una seconda pagina con le sole voci del
capitolo nuovo. Sottomoduli nei segnalibri, non esportati come capitoli.

Compilazione condivisa completata senza errori o avvisi. Volume di 58 pagine:
3 preliminari; capitoli di 26, 10, 12 e 7 pagine. Il capitolo 1 mantiene
contenuto e impaginazione; cambiano il capitolo 2 dalla sezione inverse,
il capitolo 3 dalla nuova sezione invertibilità, la numerazione di alcuni
enunciati e i rimandi. Il capitolo 4 è nuovo. Pagine di testo 1–26, 27–36,
37–48, 49–55. Tutti gli estratti rigenerati; nessuna copia annotata modificata.
Verifiche finali e impronte in VERIFICA_LEZIONI_19-21_2026-11-12.json.


## Revisione totale successiva all'integrazione — 12 novembre 2026

Eseguita la seconda parte della richiesta: revisione di correttezza e
chiarezza dell'intera dispensa corrente, non soltanto delle lezioni 19–21.
Riletti tutti i 24 moduli matematici inclusi dai quattro capitoli, con
ricostruzione delle prove generali. Inventario per modulo, conteggi e hash
in INVENTARIO_REVISIONE_TOTALE_2026-11-12.json; resoconto leggibile in
REVISIONE_TOTALE_2026-11-12.md.

Precisati la scelta della prima colonna non nulla nel blocco di Gauss,
la disposizione dei generatori per usare le colonne pivot e la prova
della loro indipendenza risalendo le righe. Esplicitati inversa del
prodotto delle matrici elementari, reversibilità della sostituzione nel
registro in R5, convenzione K^0, inclusione del polinomio nullo, dimensioni
finite e basi degli esempi. Distinte la fibra f^{-1}({w}) e la valutazione
della funzione inversa; definiti sigma e caratteristica 2 prima dell'uso.
Riconosciuta la ripresa del medesimo esercizio in R4 con metodo alternativo,
lasciando nel riquadro rosa soltanto dati e richieste.

Tutti i calcoli sono stati ricontrollati mediante frazioni esatte, compresi
i capitoli precedenti e il cambio di basi dei polinomi. La riduzione del
parametro è verificata simbolicamente sui coefficienti, non soltanto su
valori campione. Aggiunti controlli delle basi duali non canoniche e del
doppio annullatore. Script riproducibile in
verifiche/revisione_totale_2026_11_12.py ed esiti in
CONTROLLI_REVISIONE_TOTALE_2026-11-12.json. I test numerici non sono usati
come prova dei teoremi generali, che sono stati riletti separatamente.

Riesaminati tutti i 17 TikZ per corrispondenza matematica e rendering;
ispezionate le tavole di tutte le 58 pagine e le viste ingrandite dei
passaggi più densi. Ricompilazione condivisa e verifica finale degli
estratti; aggiornati README, indice comune delle dimostrazioni e registri.
Le priorità A/B/C restano motivate dai medesimi metodi, senza attribuire
progressi di studio. I risultati infiniti e le ipotesi di scelta rimangono
distinti dalle prove finite complete.

Il volume resta di 58 pagine, con estratti di 26, 10, 12 e 7 pagine; cambia
la disposizione interna di alcune pagine di tutti i capitoli, senza nuove
modifiche alla numerazione degli enunciati rispetto all'integrazione 19–21.
Fonti originali integre; copie annotate separate e non modificate.
Esiti correnti in VERIFICA_REVISIONE_TOTALE_2026-11-12.json; la verifica
precedente delle lezioni 19–21 resta storica e documenta quella versione.


## 13 novembre 2026 — Enunciati e prove numerati

Riorganizzati i risultati con enunciati distinti mediante punti numerati e corrispondenti parti della prova; prove comuni e implicazioni fra punti segnalate esplicitamente. Contenuti e profondità conservati, senza nuove fonti né variazioni delle priorità di studio. Regola aggiunta al protocollo comune.

Volume: 58 → 60 pagine. Ricompilato senza avvisi; rigenerati e confrontati tutti i 4 estratti con il volume (testo, flussi, pagine e pixel). Ispezionati elenchi e raccordi; nessuna modifica alle copie Goodnotes. Resoconto: `../../strumenti/NUMERAZIONE_ENUNCIATI_2026-11-13.md`; verifica: `../../strumenti/VERIFICA_NUMERAZIONE_ENUNCIATI_2026-11-13.json`.

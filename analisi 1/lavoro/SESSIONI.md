# Registro delle sessioni

Questo file contiene informazioni di lavoro e non viene incluso nel PDF.

## Regole concordate

- Titolo: **Appunti di analisi 1**.
- Sotto il titolo: **Prof. Federico Cacciafesta**.
- Campo autore: **Jude De Sa'Pinto**.
- Indice per argomenti; numeri delle lezioni soltanto sotto i macroargomenti
  (capitoli), senza riferimenti alle pagine nel PDF.
- Prosa autonoma dai richiami narrativi alle lezioni; precisazioni di
  convenzione in note a piè di pagina, quando necessarie.
- Tutti gli enunciati, esempi e osservazioni delle fonti vanno mantenuti.
- Le abbreviazioni vanno sciolte e i passaggi necessari spiegati discorsivamente.
- Disegni TikZ dove aiutano a comprendere il contenuto.
- Registri e informazioni sull'avanzamento esclusi dal PDF.
- Lavoro distribuito in sessioni: ogni sessione termina con una parte
  concreta, compilabile e controllata.

## Sessione 1 — 20 ottobre 2026

### Contenuto elaborato

- Creata la cartella del progetto e configurata la compilazione in VS Code.
- Creati frontespizio, indice tematico, convenzioni e preambolo comuni.
- Inventariati e copiati tutti gli otto PDF; pagine complessive: 118.
  Le prime pagine sono copertine. Il manifest conserva le impronte SHA-256.
- Lezione 1: lettura visiva di tutte le pagine di contenuto (2–13).
- Capitolo «Logica e metodi di dimostrazione»: proposizioni, tutti i
  connettivi, contronominale, ragionamento per assurdo, quantificatori,
  esistenza unica e negazione dei quantificatori.
- Capitolo «Insiemi e relazioni»: nozione di insieme e appartenenza,
  rappresentazioni, insieme vuoto, inclusione, parti, operazioni,
  complementare, De Morgan, prodotto cartesiano, relazioni e ordini.
- Importata in coda, nel capitolo «Topologia della retta», la trascrizione
  completa della lezione 8 già revisionata, con tutti e tre i TikZ.
  Convenzioni e preambolo sono stati centralizzati.
- Aggiunti una tabella di verità e un diagramma di Venn come ausili
  esplicativi. Gli esempi aggiunti esplicitano le definizioni della fonte.

### Chiarimenti redazionali

- Distinti contrapposizione e ragionamento per assurdo, accostati negli
  appunti della lezione 1.
- Nelle relazioni d'ordine è usato il termine «antisimmetria», coerente con
  la formula del manoscritto.
- La lezione 8 mantiene la convenzione del docente sugli intorni laterali
  aperti che escludono il punto centrale; il significato è spiegato nel testo.
- Il testo originario della lezione 8, aperto all'inizio della richiesta,
  non è stato modificato; una copia è conservata in `fonti/`.

### Stato delle altre fonti alla chiusura della sessione 1

Le lezioni 2–7 sono state inventariate e ne è stato ricavato un orientamento
preliminare tramite estrazione del testo. Non sono ancora state lette
integralmente né trascritte: non sono da considerare incluse nel PDF attuale.
Le intestazioni tematiche di seguito sono pertanto un piano da confermare
sulle immagini, senza usare l'estrazione automatica come trascrizione affidabile.

### Verifiche

- Compilazione completa conclusa con `latexmk`: 14 pagine, senza errori,
  avvisi, riferimenti indefiniti o righe fuori margine.
- Controllati visivamente frontespizio, indice, tutte le pagine del corpo,
  tabella di verità e quattro disegni TikZ.
- Sistemati i salti di pagina per conservare titolo di sezione,
  provenienza e inizio del contenuto insieme.
- Verificata l'identità del corpo della lezione 8 rispetto alla trascrizione
  iniziale, al netto dei richiami alle fonti e dei titoli adattati ai
  segnalibri del PDF; conservati tutti e tre i TikZ originali.
- Verificati metadati del PDF: titolo e autore corrispondono alla richiesta.
- Verificata l'assenza di registri e note di avanzamento dal PDF.

**Sessione 1 conclusa.** Il volume attuale comprende le lezioni 1 e 8;
le lezioni 2–7 restano da elaborare nelle sessioni successive.

## Sessione 2 — 20 ottobre 2026

### Contenuto elaborato

- Lette visivamente tutte le pagine di contenuto della lezione 2 (2–11)
  e della lezione 3 (2–7), senza affidarsi alla loro estrazione automatica.
- Aggiunto il capitolo «Numeri naturali, induzione e combinatoria»:
  catena degli insiemi numerici, ordine dei naturali, principio del minimo
  intero assunto come assioma, induzione in entrambe le forme e prova per
  minimo controesempio, somma dei primi naturali con esempio da 1 a 100,
  disuguaglianza di Bernoulli e relativa dimostrazione completa.
- Inseriti permutazioni, disposizioni e combinazioni senza ripetizione,
  fattoriale, coefficienti binomiali, tutte e quattro le proprietà elencate
  nella lezione 2 e verifica algebrica della relazione di Pascal dalla
  lezione 3, compresi gli indici agli estremi.
- Inseriti triangolo di Tartaglia e formula del binomio di Newton.
- Avviato il capitolo «Sistemi numerici e completezza» con l'intera parte
  finale della lezione 3: interi come gruppo abeliano, razionali come campo
  ordinato, proprietà di Archimede nei razionali, densità fra razionali e
  numerabilità di tutti i razionali.
- Aggiunti due TikZ: triangolo di Tartaglia e griglia delle frazioni con
  percorrenza diagonale ed esempio di eliminazione delle ripetizioni.
- Inseriti i nuovi capitoli prima della topologia, mantenendo l'indice per
  argomenti e i richiami alle lezioni sotto le sezioni.

### Chiarimenti e integrazioni redazionali

- Precisato che gli oggetti contati nelle formule combinatorie sono
  distinti e scelti senza ripetizione; esplicitata la convenzione `0! = 1`.
- Il binomio di Newton è solo enunciato nel PDF della lezione 3: aggiunte
  una spiegazione combinatoria e una dimostrazione per induzione.
- Per il campo dei razionali, il gruppo moltiplicativo è correttamente
  riferito ai razionali non nulli. Esplicitate commutatività e distributività.
- Sviluppate le verifiche della proprietà di Archimede in Q e della densità
  fra estremi razionali. La densità di Q fra estremi reali, con la relativa
  prova dalla lezione 5, resta nel lavoro della prossima sessione.
- Completata la costruzione della lista di Q: eliminazione dei valori
  già comparsi, inserimento dello zero e dei negativi.

### Verifiche

- Confrontati tutti gli enunciati, esempi, osservazioni e calcoli delle
  pagine indicate con le nuove sezioni; aggiornata `COPERTURA.csv`.
- Compilazione completa con aggiornamento di indice e segnalibri.
- Controllate visivamente le nove pagine dei nuovi capitoli, i due TikZ
  e le due pagine dell'indice.
- Nessun errore, avviso, riferimento indefinito o riga fuori margine.
- Titolo, autore, fonti e parte della lezione 8 conservati; registri
  esclusi dall'output del PDF.

**Sessione 2 conclusa.** Il volume comprende ora integralmente le lezioni
1, 2, 3 e 8. Il PDF attuale ha 24 pagine complessive. Le lezioni 4–7
restano da sviluppare.

## Sessione 3 — 20 ottobre 2026

### Contenuto elaborato

- Lette visivamente tutte le pagine di contenuto della lezione 4 (2–14)
  e la prima parte della lezione 5 (2–11). La parte sulle funzioni della
  lezione 5, pp. 12–16, resta per la prossima sessione.
- Completato il capitolo «Sistemi numerici e completezza» con irrazionalità
  della radice di due, proprietà di campo ordinato dei reali, assioma di
  Dedekind, controesempio in Q e idea delle sezioni di Dedekind.
- Inseriti intervalli finiti e illimitati, estremi, centro, raggio,
  ampiezza e retta estesa; limitatezza e tutte le scelte numeriche di
  maggioranti e minoranti presenti nella fonte.
- Inseriti massimo e minimo, unicità, supremo e infimo, collegamento con
  massimo/minimo, esistenza degli estremi in R con prova da Dedekind,
  fallimento del teorema in Q ed estremi infiniti.
- Inserito il criterio operativo con epsilon per supremo e infimo,
  dimostrato in entrambi i versi per entrambi gli estremi.
- Inserita la dimostrazione del principio di Archimede nei reali e
  sviluppati tutti gli esempi della lezione 5: [0,1), [-1,2] unito a {5},
  reciproci dei naturali positivi, candidati errati per l'infimo,
  {n^3-1 : n in N} e l'unione definita da x^2<1 e (x-3)^2=0.
- Inserita la dimostrazione della densità di Q in R, esplicitando il
  passaggio sull'intero contenuto in un intervallo di ampiezza maggiore di 1.
- Aggiunti tre schemi TikZ: fasce epsilon di supremo e infimo, confronto
  fra intervallo e insieme con massimo isolato, dilatazione dell'intervallo
  nella prova della densità.
- Per facilitare gli aggiornamenti, il capitolo 04 include ora tre
  sottocapitoli sorgente: 04a-reali-e-completezza.tex,
  04b-intervalli-ed-estremi.tex e 04c-archimede-ed-esempi.tex.

### Chiarimenti e integrazioni redazionali

- Esplicitato che il separatore dell'assioma di Dedekind deve funzionare
  per tutte le coppie contemporaneamente; l'assioma non ne richiede l'unicità.
- Le tre condizioni sulle sezioni riportate nel manoscritto consentono
  due rappresentazioni di un razionale. Aggiunta la convenzione che la
  parte inferiore non abbia massimo, necessaria per una rappresentazione
  univoca. Dalla disgiunzione delle parti segue che i loro elementi sono
  strettamente ordinati.
- Esplicitati i due piccoli spostamenti razionali che escludono un
  separatore in Q per il taglio corrispondente alla radice di due.
- Corretto il passaggio algebrico della lezione 5, p. 6: quando
  0<epsilon<1, la richiesta 1/n < -1+epsilon è impossibile perché il
  secondo membro è negativo. Non si usa l'equivalenza errata del manoscritto
  ottenuta invertendo un numero negativo.
- Rispettata la potenza cubica dell'esercizio A1, verificata ingrandendo
  l'immagine. Conservato l'estremo 2 incluso nell'esempio B=[-1,2] unito a {5}.
- Anticipata tematicamente la prova di Archimede rispetto agli esempi che
  la usano, mantenendo per ogni sezione le pagine originali di provenienza.
- Le spiegazioni sulla costruzione delle sezioni, sui criteri operativi
  e sugli esercizi sviluppano le formulazioni sintetiche delle fonti.

### Verifiche

- Compilazione completa con `latexmk`, indice e segnalibri aggiornati.
- PDF di 32 pagine, senza errori, avvisi, riferimenti indefiniti o righe
  fuori margine.
- Controllate visivamente tutte le nove pagine toccate dai nuovi contenuti,
  i tre nuovi TikZ e le due pagine dell'indice.
- Aggiornato il registro di copertura per tutte le pagine 2–14 della
  lezione 4 e 2–11 della lezione 5.
- Registri e note di avanzamento restano esclusi dal PDF.

**Sessione 3 conclusa.** Il volume comprende integralmente le lezioni
1–4 e 8, oltre alla parte sui reali della lezione 5 (pp. 2–11).
Restano da elaborare la parte sulle funzioni della lezione 5 (pp. 12–16)
e le lezioni 6–7, poi da svolgere la revisione complessiva.

## Sessione 4 — 20 ottobre 2026

### Contenuto elaborato

- Lette visivamente tutte le pagine restanti della lezione 5 (12–16) e
  tutte le pagine di contenuto della lezione 6 (2–24): 28 pagine manoscritte.
- Creato il capitolo «Funzioni: definizioni e proprietà generali» con
  dominio, codominio, immagine, iniettività, suriettività, biettività,
  composizione sul dominio effettivo, grafico, fibre e funzione inversa.
- Conservato l'esempio f(x)=1+x² e g(x)=radice(x), in entrambi gli ordini
  di composizione, con i rispettivi domini. Conservato l'esempio del
  dominio naturale di 1/(x²-4).
- Inserite tutte le operazioni fra funzioni, le quattro nozioni di
  monotonia, i versi della composizione, il rapporto con l'iniettività,
  la monotonia dell'inversa, parità, disparità e periodicità.
- Inseriti limitatezza ed estremi delle funzioni, distinzione fra valori
  estremi e punti in cui sono raggiunti, grafico con due punti di massimo
  e un punto di minimo. Esplicitati anche estremi raggiunti agli estremi
  del dominio e differenza fra supremo e massimo.
- Creato il capitolo «Funzioni elementari» con potenze intere positive,
  radici pari e dispari, potenze razionali positive, valore assoluto,
  distanza e quattro assiomi di metrica.
- Inserite circonferenza goniometrica, seno, coseno e tangente, domini,
  immagini, simmetrie e periodi; inserite le tre restrizioni principali
  invertibili e arcoseno, arcocoseno, arcotangente con i relativi grafici.
- Aggiunti 11 schemi TikZ, alcuni con due grafici affiancati (15 ambienti
  tikzpicture): composizione, riflessione rispetto alla bisettrice,
  monotonia, reciproci, estremi, potenze/radici, modulo, circonferenza e
  tre coppie funzione/restrizione/inversa.
- Attivati i capitoli 05 e 06 prima della topologia. Sorgenti separati per
  proprietà generali delle funzioni reali, potenze/radici, modulo/distanza
  e trigonometria, per facilitare le integrazioni successive.

### Chiarimenti e integrazioni redazionali

- La composizione usa f(X) intersecato con il dominio di g; distinta la
  composizione sull'intero dominio dalla composizione sul sottoinsieme X'.
- Distinta la controimmagine come insieme dal valore della funzione
  inversa. Corretto il refuso della lezione 6, p. 2: la soluzione x
  appartiene al dominio di f, non al suo insieme immagine.
- Esplicitata la simmetria del dominio necessaria per parità e disparità.
- Conservato il grafico dei reciproci della lezione 6, p. 7, chiarendo
  che 1/x è iniettiva e decrescente su ciascuna semiretta, ma non è
  monotona sul dominio intero. Stessa distinzione per i rami della tangente.
- Nella periodicità mantenuta la convenzione del corso di escludere le
  funzioni costanti; la frase sui periodi arbitrari riguarda costanti su R.
- Per le potenze pari distinta la non negatività dalla positività stretta
  fuori da zero. La radice di zero è zero: nella definizione di radice si
  richiede «non negativo», non «positivo» per ogni argomento.
- Sviluppate le prove delle identità dell'inversa, della composizione di
  funzioni monotone, della monotonia dell'inversa, del segno e della
  monotonia delle potenze, delle proprietà del modulo e della metrica usuale.
- Aggiunta una prova dell'esistenza delle radici dalla completezza, mediante
  il supremo e la fattorizzazione della differenza di potenze; non usa
  continuità o teoremi dei valori intermedi non ancora trattati.
- Precisata l'indipendenza dalla rappresentazione della frazione per le
  potenze razionali su basi non negative; precisati i domini nelle identità
  di inversione delle funzioni trigonometriche.

### Verifiche

- Registro di copertura aggiornato per tutte le pagine delle lezioni 5 e 6.
- Compilazione completa con indice e segnalibri aggiornati: 45 pagine,
  senza errori, avvisi, riferimenti indefiniti o righe fuori margine.
- Controllate visivamente tutte le 13 nuove pagine e i grafici; corretta
  l'impaginazione per mantenere il grafico dell'arcotangente insieme al testo.
- Registri e note di avanzamento esclusi dal PDF; titolo, autore e corpo
  della lezione 8 conservati.

**Sessione 4 conclusa.** Il volume comprende integralmente le lezioni
1–6 e 8. Restano la lezione 7 e la revisione complessiva delle otto fonti.

## Sessione 5 — 20 ottobre 2026

### Contenuto elaborato

- Lette visivamente tutte le pagine di contenuto della lezione 7 (2–21).
- Integrato il capitolo sulle funzioni elementari con esponenziali e
  logaritmi per basi maggiori e minori di 1, numero di Nepero, esponenziale
  naturale, logaritmo naturale, domini, immagini e grafici.
- Inserite seno, coseno e tangente iperbolici, identità fondamentale con
  dimostrazione, collegamento geometrico con circonferenza e ramo destro
  dell'iperbole, simmetrie, monotonia, immagini e grafici.
- Inserite le tre inverse iperboliche con le notazioni alternative della
  fonte: derivazione completa dell'inversa del seno iperbolico tramite
  t=exp(y), scelta delle soluzioni per il coseno sul dominio non negativo
  e derivazione dell'inversa della tangente.
- Inserite parti positiva e negativa con le due identità per x e modulo,
  grafici e applicazione punto per punto alle funzioni; inserite parte
  intera e parte frazionaria con le notazioni alternative in nota,
  grafici con estremi aperti/chiusi ed esempi anche per numeri negativi.
- Inserite tutte le trasformazioni dei grafici: f(x)+a, f(x-b), -f(x).
- Svolto integralmente l'esercizio f(x)=4 arcsin(1-ln(x-1)): dominio
  [2,1+e²], prova della stretta decrescenza, immagine [-2pi,2pi], soluzione
  dell'equazione, inversa esplicita, estremi e grafico.
- Inserita l'introduzione alla topologia prima della parte della lezione 8:
  definizione di aperto per unione di intervalli, famiglia vuota, tutti gli
  esempi della fonte, definizione di chiuso e tutti gli esempi mediante
  complementare; criterio locale con prova nei due versi; esempio [0,1)
  né aperto né chiuso.
- Aggiunti i sorgenti 06d, 06e e 07a. Le parti nuove restano organizzate
  per tema e non per lezione.

### Chiarimenti matematici

- Distinto il caso a=1, che non dà una biezione esponenziale.
- Per la potenza a esponente reale, la costruzione rinviata nella fonte è
  richiamata con una definizione mediante il supremo in nota.
- Precisato che (cosh(t),sinh(t)) percorre soltanto il ramo destro
  dell'iperbole, non entrambi i rami.
- Precisata la restrizione a [0,+infinito) necessaria per invertire cosh.
- Corretto il refuso «non decr.» della lezione 7, p. 16: la funzione
  dell'esercizio è strettamente decrescente, coerentemente con i calcoli.
- Per la topologia distinta l'esclusione dell'insieme vuoto dalla nozione
  di intervallo dall'ammissione dell'unione di una famiglia vuota.

**Sessione 5 conclusa.** Tutte le lezioni 1–8 sono integrate.

## Sessione 6 — 20 ottobre 2026

### Revisione richiesta dall'utente

- Rimossi i richiami dettagliati sotto sezioni e sottosezioni. I riferimenti
  con pagine sono conservati nei commenti TeX e in COPERTURA.csv.
- Inserito un solo richiamo di provenienza per ciascuno dei sette capitoli:
  1; 1; 2–3; 3–4–5; 5–6; 6–7; 7–8.
- Riscritte tutte le frasi del corpo che rimandavano a una lezione, al
  manoscritto o al corso: dimostrazione dell'induzione, esempi di insiemi,
  formule combinatorie, costruzione dei reali, densità e intorni laterali.
- Convenzioni su intervallo vuoto, periodicità e intorni laterali chiarite
  in nota a piè di pagina. Note aggiuntive limitate alla costruzione
  dell'esponenziale reale e alle notazioni di parte intera/frazionaria.
- Aggiornato README.md per le stesse regole negli aggiornamenti futuri.

### Revisione matematica e di completezza

- Riletti tutti i capitoli e ricontrollate ipotesi, casi agli estremi,
  domini, codomini, immagini, implicazioni e passaggi delle dimostrazioni.
- Ricontrollata la copertura delle pagine già verificate nelle sessioni
  precedenti e completata la corrispondenza per la lezione 7: tutte le
  110 pagine di contenuto dei PDF sono associate ai sorgenti attivi.
- Verificata l'integrità delle otto fonti tramite le impronte del manifest.
- Confrontati i sorgenti con la copia precedente alla revisione:
  conservate tutte le formule in display e tutti i TikZ preesistenti.
- Corretto un dettaglio della dimostrazione aggiunta sull'esistenza delle
  radici: le stime intermedie usano <= e >=, così includono anche n=1;
  le disuguaglianze finali restano strette grazie alla scelta di h.
- Ricontrollati tutti gli esempi e i tre disegni della lezione 8, conservando
  il contenuto matematico e spostando la precisazione sugli intorni in nota.
- Conservata una copia dei sorgenti iniziali in
  lavoro/Sorgenti-prima-della-revisione.zip, esclusa dal PDF.

### Verifiche finali

- Compilazione completa con aggiornamento automatico di indice e segnalibri.
- PDF di 52 pagine complessive, senza errori, avvisi, riferimenti indefiniti
  o righe fuori margine.
- Controllo visivo dell'intero volume: frontespizio, tre pagine di indice,
  convenzioni, capitoli, note e grafici; controllo mirato delle pagine
  interessate dagli ultimi ritocchi.
- Migliorati i salti di pagina per non isolare l'inizio degli enunciati;
  verificati gli estremi dei grafici a gradini e a dente di sega.
- Verificati titolo, autore, esattamente sette richiami alle lezioni e
  assenza di registri, pagine delle fonti e richiami narrativi dal PDF.

**Sessione 6 conclusa.** Il documento comprende tutte le otto lezioni,
la revisione complessiva e le due modifiche redazionali richieste.

## Aggiornamenti futuri

Integrare i nuovi contenuti nei capitoli tematici, creare nuovi file inclusi
quando utile e aggiungere il numero della lezione soltanto al richiamo del
macroargomento. Conservare i riferimenti precisi nei commenti e nel registro
separato. Sviluppare gli argomenti in prosa autonoma e usare note a piè di
pagina per precisazioni di convenzione necessarie. Compilare e controllare
il risultato dopo ogni aggiornamento, lasciando i registri fuori dal PDF.


## Revisione matematica — 21 ottobre 2026

Riletti integralmente i sette capitoli di Analisi 1. Corretti un valore
nella tabella di verità e la spiegazione di punto isolato; aggiunte
precisazioni sui codomini delle identità dell’inversa, sul periodo
principale della parte frazionaria e sui risultati assunti per
l’esponenziale reale. Resoconto e limiti del controllo in
`REVISIONE_MATEMATICA_2026-10-21.md`. PDF: 53 pagine, compilazione
senza errori o avvisi. Fonti originali integre.

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

Revisionato integralmente il capitolo 1: struttura espositiva, distinzione
tra definizioni ed esempi, metodi di dimostrazione e sorgente con un
paragrafo logico per riga. Formule, label e numerazione conservate.
Compilazione e verifica degli estratti completate. Piano e resoconto
comuni in `../../lavoro/revisione-editoriale/`.


## Revisione editoriale — sessione 02, 22 ottobre 2026

Rimossi i rientri di prima riga e ridotti quelli degli elenchi nel
preambolo. Compilazione ed estratti verificati. Resoconto comune in
`../../lavoro/revisione-editoriale/SESSIONE_02.md`.


## Revisione editoriale — sessione 06, 22 ottobre 2026

Completato Insiemi e relazioni, comprese le prove di De Morgan. Sorgenti, esempi, ordine, elenchi e definizioni riorganizzati; disegni conservati. Compilazione, PDF e tutti gli estratti controllati. Dettagli in `../../lavoro/revisione-editoriale/SESSIONE_06.md`.


## Revisione editoriale — sessione 07, 22 ottobre 2026

Completato Numeri naturali, induzione e combinatoria. Prove organizzate per idee, esempi e casi estremi distinti; formule e TikZ conservati. Compilazione, PDF ed estratti verificati. Resoconto in `../../lavoro/revisione-editoriale/SESSIONE_07.md`.


## Revisione editoriale — sessione 08, 22 ottobre 2026

Completato Sistemi numerici e completezza, incluse tutte le prove e gli esempi. Formule, quattro TikZ e numerazione degli enunciati conservati. Compilazione, PDF ed estratti verificati. Capitolo di 11 pagine, volume di 53; cambiano di una pagina anche i numeri stampati dei capitoli successivi. Dettagli in `../../lavoro/revisione-editoriale/SESSIONE_08.md`.


## Revisione editoriale — sessione 09, 22 ottobre 2026

Completato il capitolo generale sulle funzioni. Prove distinte per idee, domini e notazioni chiariti; formule e cinque TikZ conservati. Compilazione, PDF ed estratti verificati. Volume di 54 pagine, capitolo di sette; numerazione dei capitoli 6–7 spostata di una pagina. Dettagli in `../../lavoro/revisione-editoriale/SESSIONE_09.md`.


## Revisione editoriale — sessione 10, 22 ottobre 2026

Completato Funzioni elementari, incluse tutte le prove presenti, i domini, le inverse e l’esercizio finale. Formule e 25 TikZ conservati; compilazione, PDF ed estratti verificati. Restano dichiarate in nota le proprietà assunte dell’esponenziale reale. Capitolo di 14 pagine, volume di 54. Dettagli in `../../lavoro/revisione-editoriale/SESSIONE_10.md`.


## Revisione editoriale — sessione 11, 22 ottobre 2026

Completata Topologia della retta: tutte le prove e gli esempi riorganizzati e verificati, con precisazioni sulle famiglie vuote, sulla densità degli irrazionali e sugli intorni nella retta estesa. Display, label e tre TikZ conservati. Compilazioni, estratti e controllo visivo delle sette sezioni completati; volume di 54 pagine, capitolo di sei. Resoconto in `../../lavoro/revisione-editoriale/SESSIONE_11.md`.


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

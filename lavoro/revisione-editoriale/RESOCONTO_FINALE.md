# Revisione conclusa — 22 ottobre 2026

Questo resoconto fotografa la revisione precedente alle successive modifiche visive richieste dall'autore. Lo stato corrente dello stile e dell'impaginazione è documentato in `SESSIONE_12.md` e `VERIFICA_STILE_12.json`: Analisi resta di 54 pagine; Geometria passa a 29. I limiti matematici descritti sotto restano validi.

Revisionate integralmente le due dispense attive in undici sessioni: sette capitoli di Analisi 1 e il capitolo Spazi vettoriali di Geometria 1, suddiviso in quattro sessioni di lavoro. Ambito e criteri sono in `CRITERI.md`; dettagli e controlli per sezione nei resoconti `SESSIONE_01.md`–`SESSIONE_11.md` e nei relativi JSON.

## Modifiche editoriali

- Distinte definizioni, proprietà, osservazioni ed esempi, con titoletti ed elenchi compatti dove rendono più leggibile la struttura.
- Riorganizzate tutte le dimostrazioni: versi delle equivalenze, doppie inclusioni, esistenza e unicità, costruzioni e invarianti riconoscibili. Conservate continue le prove brevi con un unico ragionamento.
- Conservati enunciati, esempi, formule, label e disegni. I controlli di conservazione delle singole sessioni sono riferiti ai sorgenti di partenza di ciascuna sessione; non sostituiscono una seconda trascrizione indipendente delle fonti.
- Un paragrafo logico per riga nei sorgenti; formule, ambienti, commenti e strutture separati. Nel controllo finale ricongiunte anche due didascalie di Geometria ancora spezzate su righe arbitrarie: questa pulizia non modifica alcun flusso di pagina dei PDF.
- Nessun rientro di prima riga; rientri minimi per gli elenchi, con punti o lettere secondo la funzione. Spazio fra corpo del testo e separatore delle note aumentato di 3 pt in entrambe le dispense.
- Indice stampato limitato a capitoli e sezioni principali; sottosezioni numerate conservate nel testo e nei segnalibri. Provenienza per numero di lezione soltanto sotto i capitoli; pagine delle fonti e registri esclusi dai PDF.

## Verifica matematica e precisazioni

La revisione odierna comprende la rilettura dei ragionamenti durante la riorganizzazione. Non sono stati individuati ulteriori errori negli enunciati. Sono stati resi espliciti, fra gli altri:

- il trasferimento dell'induzione da zero a un indice iniziale arbitrario;
- il passaggio da estremo superiore a estremo inferiore e la corestrizione nelle identità dell'inversa;
- esistenza e unicità della parte intera, e minimalità del periodo della parte frazionaria;
- casi degeneri, famiglie vuote, scelta di un razionale non nullo nella densità degli irrazionali e testimoni nei controesempi topologici;
- le fasi dello scambio, delle costruzioni di basi, delle operazioni nel quoziente e degli esercizi finali di Geometria.

Restano conservate le correzioni matematiche già documentate il 21 ottobre: una cella della tabella di verità, la definizione di punto isolato e l'assioma dell'unità nella formulazione abbreviata di spazio vettoriale. I rapporti storici delle due materie mantengono date, ambito e risultati originali.

### Limiti da conoscere per lo studio

- La costruzione completa dell'esponenziale reale, le leggi delle potenze reali, la stretta monotonia e l'immagine non sono dimostrate: restano assunte e dichiarate in nota nella sezione 6.9. Il rinvio è presente anche nella fonte; le prove successive che usano l'esponenziale dipendono da queste proprietà.
- La revisione riguarda il materiale consegnato e i sorgenti attivi: non attesta la copertura dell'intero programma d'esame. In Geometria i numeri complessi sono ancora in attesa di una fonte e non sono inclusi.
- Si tratta di una revisione manuale dell'assistente, senza una validazione indipendente del docente. Per una conferma indipendente, i punti prioritari sono il perimetro delle dimostrazioni richieste all'esame e la copertura del programma. Non restano ambiguità matematiche individuate che impediscano di chiudere questa revisione editoriale.

## Output verificati

| Volume | Pagine complessive | Capitoli esportati | Pagine stampate degli estratti |
| --- | ---: | ---: | --- |
| Analisi 1 | 54 | 7 | 1–3; 4–6; 7–12; 13–23; 24–30; 31–44; 45–50 |
| Geometria 1 | 28 | 1 | 1–25 |

Compilazione tramite configurazione condivisa e compilatore integrato riuscite per entrambi i progetti. Nessun errore, avviso LaTeX, riferimento indefinito o segnalazione di righe fuori margine. Gli otto estratti sono stati confrontati con il volume per flussi di pagina, testo, dimensioni e numerazione; verificate anche le destinazioni dei collegamenti rimasti negli estratti. L'esportatore emette messaggi diagnostici di `pypdf` sul confronto delle annotazioni; il controllo diretto delle destinazioni è riuscito e tali messaggi non sono avvisi del compilatore LaTeX.

Verificati tutti i 34 sorgenti attivi raggiungibili dai due documenti principali, inclusi i preamboli. Fonti originali integre rispetto ai manifest: otto PDF e la trascrizione iniziale in Analisi; sette PDF in Geometria. Ispezionate le sezioni durante ogni sessione; al termine controllati frontespizi, indici e flusso complessivo delle 82 pagine. La panoramica finale dell'impaginazione integra i controlli delle singole pagine, senza sostituire la lettura matematica.

Le revisioni hanno cambiato l'impaginazione dei capitoli: gli estratti attuali non riallineano le annotazioni delle copie precedenti. Nessuna copia annotata è stata sovrascritta.

Impronte correnti, risultati degli estratti e inventario strutturale sono in `VERIFICA_ANALISI-1.json`, `VERIFICA_GEOMETRIA-1.json` e `VERIFICA_CONCLUSIVA.json`. Nessun lavoro richiesto resta aperto sulle dispense attualmente fornite.

> **Documento storico delle sessioni precedenti.** Il registro corrente è `RINASCITA_2026-10-23.md`; le scelte delle prove sono in `SCELTA_DIMOSTRAZIONI.csv`. Questo documento non certifica il testo ricostruito.

> **Registro storico della prima stesura.** La revisione successiva su richiesta dell’autore rimuove gli ampliamenti autonomi e ripristina l’ordine A–L. Per stato corrente, integrazioni M–Z e limiti consultare `CONFRONTO_A-L_M-Z_2026-10-23.md` e `VERIFICA_FINALE.json`. La vecchia prova CSB e la codifica ternaria non appartengono più al testo attivo.

# Revisione matematica e scelte editoriali — 23 ottobre 2026

## Ambito e metodo

Letti visivamente tutti gli 11 PDF, per 65 pagine, mediante rendering delle pagine; il testo estraibile dei primi cinque file è assente e quello dei successivi è incompleto. La lettura è stata confrontata con la stesura tematica; `COPERTURA.csv` associa ogni pagina ai moduli attivi. I PDF originali sono copiati senza modifiche e verificati mediante SHA-256. I numeri delle lezioni derivano dai nomi dei file; le date manoscritte incongruenti non sono state normalizzate inventando una cronologia.

La presente è una revisione manuale dell'assistente, accompagnata dai controlli finiti ed editoriali registrati. Non equivale a una validazione indipendente del docente. Le proprietà di base di N e Z, induzione e buon ordinamento sono assunte; per i reali sono assunte struttura di campo ordinato completo, densità razionale e proprietà usuali delle radici. Queste dipendenze sono dichiarate nei preliminari.

## Riorganizzazione

- Operazioni e partizioni delle lezioni 1–3 sono riunite nei capitoli 1–2. La prova dell'associatività della differenza simmetrica conserva sia il criterio di appartenenza dispari sia la scomposizione nelle regioni dei tre insiemi.
- Definizioni e richiami su equivalenze, classi e razionali delle lezioni 2–4 sono fusi in un'unica trattazione. Sono conservati entrambi i versi delle prove, le due inclusioni per le classi, la corrispondenza inversa fra partizioni ed equivalenze, gli esempi e tutti gli esercizi di classificazione.
- Le funzioni delle lezioni 4–7 sono riunite nel capitolo 3. Il supporto primo è trattato una sola volta, includendo le versioni su N* e su N, le fibre e l'immagine esatta. Le giustificazioni aritmetiche sono rinviate esplicitamente al capitolo 5.
- Il capitolo 4 raccoglie finitezza, infinito, cardinalità e numerabilità. Il richiamo ai razionali è successivo alla loro costruzione; la prova della cardinalità dei reali segue la numerabilità di Q.
- Nel capitolo 5 la divisione precede il calcolo del MCD; l'esistenza del MCD non è presupposta nella prova dell'invarianza dei divisori comuni. L'infinità dei primi usa il lemma di esistenza di un divisore primo. Le formule di mcm seguono la fattorizzazione. L'irrazionalità di √p è posta accanto alle applicazioni della fattorizzazione.

## Correzioni e precisazioni

1. **Partizioni (L3 p. 1; L4 p. 1).** Esplicitati i blocchi non vuoti: copertura e implicazione «intersezione non vuota implica coincidenza» da sole lasciano aggiungere il blocco vuoto. Inclusa la partizione vuota di X vuoto.
2. **Parallelismo (L2 pp. 4–5).** L'equivalenza richiede di comprendere le rette coincidenti. Con parallelismo inteso soltanto tra rette distinte manca la riflessività.
3. **Divisibilità e confrontabilità (L2 pp. 5–6).** Distinte la totalità come confrontabilità e l'antisimmetria. Nell'insieme con 1, ±2, ±6, 18 tutte le coppie sono confrontabili, ma non si ottiene un ordine per la presenza degli associati distinti.
4. **Funzioni sui razionali (L4 pp. 1–4).** Le regole a/b↦a+b e (a/b,c/d)↦(a+c)/(bd) sono controesempi alla buona definizione. Per somma e prodotto ordinari sono verificati entrambi i cambi di rappresentante e i denominatori non nulli.
5. **Supporto primo (L4 p. 7; L6 pp. 1–2).** Distinte le immagini su N* e N. La seconda include P perché J(0)=P; non va descritta soltanto come famiglia di insiemi finiti. Precisato il carattere successivo delle giustificazioni tramite fattorizzazione e infinità dei primi.
6. **Inverse (L5 p. 7; L6 pp. 2–5).** Chiariti i lati delle identità, dimostrata la coincidenza dell'inversa sinistra e destra, mantenute le due radici come inverse destre distinte del quadrato. La costruzione dell'inversa sinistra richiede dominio non vuoto quando il codominio contiene punti fuori dall'immagine. La scelta simultanea nelle fibre arbitrarie per l'inversa destra è esplicitata.
7. **Insiemi infiniti (L7 pp. 2–3; L8 pp. 1–2).** Il passaggio da infinito a esistenza di una successione di elementi distinti è formulato nel quadro con scelta. La prova dello spostamento include separatamente i due punti nella copia di N, i due esterni e il caso misto.
8. **Confronto con suriezioni (L8 p. 3).** La definizione generale usa iniezioni; l'equivalenza con una suriezione nel verso opposto è limitata agli insiemi non vuoti. Ciò evita il caso errato della suriezione da un insieme non vuoto al vuoto.
9. **Unioni numerabili (L8 pp. 4–5).** Gestiti i membri vuoti prima di sceglierne enumerazioni; da N non esiste una suriezione sul vuoto. Dichiarata la scelta simultanea delle enumerazioni.
10. **Numerabilità di Q (L8 p. 4).** Per tutti i razionali il dominio della mappa quoziente è Z×N*, non N×N*: il secondo raggiunge solo razionali non negativi. Sono ammessi denominatori positivi senza perdere alcuna classe.
11. **Codifica del continuo (L9 p. 1).** La somma binaria su tutte le successioni non è iniettiva: (1,0,0,…) e (0,1,1,…) hanno entrambe somma 1 con i pesi della fonte. Usata invece la serie ternaria con cifre 0 e 2, con stima esplicita al primo indice diverso. L'altra iniezione usa i tagli razionali; completate entrambe le disuguaglianze con Cantor–Schröder–Bernstein.
12. **Infinità dei primi (L9 p. 4).** Il prodotto dei primi elencati più 1 non è necessariamente primo: si prende un suo divisore primo e si prova che è esterno alla lista. Il lemma del minimo divisore precede questa prova.
13. **Divisione euclidea (L10 pp. 2–3).** Conservati i casi a≥0,b>0; a<0,b>0; b<0. Nell'unicità si usa |r−r'|<|b|, senza assumere il segno della differenza. L'esistenza per il divisore negativo è svolta, non lasciata aperta.
14. **Algoritmo di Euclide (L11 p. 1).** Compreso il caso di resto iniziale zero: il risultato è il divisore iniziale positivo. Non si richiede sempre un resto positivo intermedio. L'algoritmo è presentato sui valori assoluti; Bézout riporta poi i segni ai dati originari.
15. **Primi e proprietà dei prodotti (L11 p. 4).** L'equivalenza richiede p≠0,±1: anche 0 e le unità soddisfano la sola implicazione sui prodotti in Z. La condizione è inclusa nell'enunciato e spiegata.
16. **Fattorizzazione (L11 pp. 4–6).** Primi scelti positivi, segno separato, esponenti positivi e lista distinta; nell'unicità si cancellano i fattori con ripetizione e si raccolgono poi gli esponenti. Non si confonde unicità letterale con unicità a meno dell'ordine o degli associati.
17. **mcm con zero (L10 p. 1).** La condizione (a,b)≠(0,0) non garantisce un mcm positivo: con un argomento nullo il solo multiplo comune è zero. Adottato mcm=0 in quel caso e positività solo per ab≠0; conservata la caratterizzazione mediante divisibilità. Le formule con esponenti includono anche ±1 tramite prodotti vuoti.

## Integrazioni sostanziali

- Svolti tutti gli esercizi e i controlli lasciati alle fonti: De Morgan e distributività, elementi neutri e annullamento, grafici delle tre relazioni, classificazioni, quozienti, funzioni a tratti e del piano, supporto primo, funzioni caratteristiche, chiusura della numerabilità, irrazionalità di √p.
- Aggiunti la prova del principio dei cassetti e il raccordo sull'enumerazione dei sottoinsiemi infiniti di N, per evitare di usare senza spiegazione l'impossibilità di un'iniezione non suriettiva su un insieme finito.
- Ricostruita integralmente la prova di Cantor–Schröder–Bernstein, il cui enunciato è presente nella fonte senza dimostrazione.
- Completate le identità per le immagini e controimmagini della composizione e la prova di unicità dell'inversa bilatera.
- Dimostrate terminazione di Euclide, identità di Bézout tramite i resti e caratterizzazione mediante la minima combinazione positiva. Esplicitata la possibilità di usare quest'ultima come prova alternativa indipendente dell'esistenza.
- Giustificato il limite √N del crivello; dimostrate le formule di MCD/mcm e tutti i casi richiesti nell'esercizio A^B.
- Ridisegnati i diagrammi utili con TikZ e accorpati quelli ripetuti: operazioni, regioni per la differenza simmetrica, complementare, grafici di relazioni, partizione, fibre, quadrato, spostamento e reticolo numerabile. Nessuna figura matematica necessaria dipende da immagini manoscritte ritagliate.

Queste integrazioni sono editoriali e non sono attribuite alla docente. Non sono aggiunti argomenti successivi come congruenze, gruppi o anelli astratti, che non compaiono nei materiali consegnati. Gli annunci Moodle e la data di una prova parziale restano nelle fonti, fuori dal testo matematico: non sono informazioni operative verificate.

## Limiti e ripresa

La prova per i reali assume completezza e densità, non costruisce R a partire dai tagli. L'ipotesi del continuo è soltanto enunciata, senza affermarne verità o falsità. Le proprietà elementari di radici e potenze non vengono ricostruite da assiomi. I numeri delle lezioni restano identificatori delle fonti ricevute; non certificano lezioni mancanti o copertura del programma. Ulteriori lezioni dell'altro docente potranno essere confrontate conservando separata la provenienza e verificando le differenze di programma.

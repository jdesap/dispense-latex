# Ricostruzione della dispensa — 23 ottobre 2026

Questo è il registro della ricostruzione del 23 ottobre. Per lo stato corrente dopo la lezione 12 leggere `LEZIONE_12_2026-10-24.md`. I registri delle sessioni 1–2 e i loro giudizi di copertura sono storici. La versione precedente completa, con sorgenti, PDF ed estratti, è conservata in `storico-prima-rinascita-2026-10-23/`.

## Metodo applicato

Ricostruzione dei cinque capitoli per unità logiche, dopo il riesame visivo delle fonti originali. La sequenza è A–L: operazioni, prodotti, parti; relazioni, ordini, partizioni, classi e razionali; funzioni, fibre, immagini, composte, inverse, caratteristiche; finitezza, confronto, numerabilità, Cantor e continuo; aritmetica degli interi. Restano accorpate le riprese effettive: associatività della differenza simmetrica A–L 3, estensione di J a zero A–L 6, svolgimento della funzione a tratti M–Z 7.

Per ciascuna prova sono stati controllati enunciato, ipotesi, prerequisiti e passaggi necessari. La scelta non dipende dal canale: M–Z è preferita per il sistema della funzione del piano, l'algoritmo esteso con ricorrenza esplicita e la prova del minimo positivo indipendente da Bézout. A–L è più completa per tutte le proprietà della composta e contiene l'unicità della fattorizzazione che M–Z rinvia. Per molte prove i metodi coincidono: si conserva un'unica esposizione completa. Sono mantenuti metodi distinti utili, come diagonali/codifica delle coppie e tabella/sostituzione a ritroso per Bézout.

`SCELTA_DIMOSTRAZIONI.csv` contiene **75 unità** con locator A–L/M–Z, motivo della scelta, prerequisiti e passaggi riesaminati. Le 65 righe di `COPERTURA.csv` e le 75 di `CONFRONTO_MZ.csv` rimandano ora a queste unità: il collegamento per pagina è un indice di provenienza, non sostituisce la verifica delle prove. Le istruzioni o gli annunci amministrativi nei PDF sono trattati come contenuto delle fonti, non come richieste operative.

## Cambiamenti rispetto alla versione criticata

- **Insiemi:** esposizione ricostruita a partire dall'appartenenza. La prova associativa della differenza simmetrica confronta i due membri mediante quattro regioni esplicite; non usa funzioni caratteristiche, parità o calcolo modulare. Logica e De Morgan sono collocati con le parti e i complementi. Ripristinate le consegne di De Morgan e annullamento con svolgimenti separati.
- **Relazioni:** distinte le verifiche di equivalenza, i controesempi e le condizioni degli ordini. La geometria usa angoli e direzioni, senza anticipare composizioni e inverse di funzioni. La formulazione originaria della partizione con «se e solo se» già impone blocchi non vuoti: non è corretta la precedente impressione di un'omissione della fonte. Classi: due inclusioni esplicite e verso inverso per riflessività. Partizioni: copertura, disgiunzione, tre proprietà e identificazione della classe mediante due inclusioni. La corrispondenza inversa rimane anche come esercizio autonomo della fonte.
- **Funzioni:** tutte e sei le applicazioni iniziali hanno immagine, iniettività e suriettività discusse, compresa J. Funzione a tratti: rami misti esclusi esplicitamente; funzione del piano: costruzione e verifica della preimmagine. Recuperate tutte le varianti d'intervallo M–Z. Distinti i quattro controesempi sulle composte. Costruzioni delle inverse su tutto il codominio, con ruolo del punto di appoggio e della scelta. Il criterio verticale è nel punto A–L dopo gli esempi. Esercizi e soluzioni sono separati.
- **Cardinalità:** esplicitati i tre casi dello spostamento, l'induzione dei prodotti finiti e i casi vuoti nell'unione numerabile. L'iniettività della codifica di N² usa soltanto cancellazione e disparità elementare, senza fattorizzazione unica. L'esercizio è B^A. Il verso con i tagli razionali è sviluppato; il verso analitico opposto resta assunto, senza sostituirlo con una teoria nuova.
- **Interi:** riscritta la catena logica completa. Divisione euclidea: parametro fissato, base, ipotesi, passo, casi di segno e unicità. Algoritmo: terminazione per buon ordinamento; insieme dei divisori comuni conservato con base e passo induttivo; conclusione sulla coppia finale. Bézout: due righe iniziali, ricorrenze di entrambi i coefficienti, sostituzione completa nel passo e correzione dei segni. Aggiunta la tabella effettiva di 72 e 420, confrontata con la risalita nelle divisioni e con il caso 72,-420. Minimo positivo: insieme non vuoto senza Bézout, due divisioni separate e condizione universale. Fattorizzazione: induzione forte per esistenza, induzione sul numero di fattori con base vuota per unicità, raccolta degli esponenti e segno. Formule MCD/mcm motivate nei due sensi tramite gli esponenti.

## Correzioni e integrazioni controllate

Restano corrette le lacune certe delle fonti: il prodotto dei primi più uno non è necessariamente primo; serve un suo divisore primo, ottenuto dal minimo divisore senza usare FTA. Per la suriezione sui razionali occorre un numeratore intero, non soltanto naturale. La somma binaria indicata in A–L non è iniettiva su tutte le successioni: il difetto è esplicitato, come limite del passo analitico. Un mcm positivo richiede entrambi gli argomenti non nulli; la caratterizzazione dei primi tramite i prodotti esclude 0 e le unità. Il criterio MCD tramite una combinazione dichiara la coppia non nulla. Per la riduzione a una coppia coprima, l'uso di d≠0 e la condizione universale sono espliciti.

Sono integrate le omissioni M–Z interne ai temi conclusi: proprietà delle famiglie, logica delle implicazioni, compatibilità di operazioni sul quoziente, criterio di iniettività tramite l'equivalenza indotta, fibre ulteriori e [168], proprietà generali di immagine/controimmagine, inverse destre del seno, famiglie come funzioni, non unicità dei coefficienti, insieme delle combinazioni dZ e divisori coprimi di uno stesso intero. Confronto totale e aritmetica cardinale generale sono integrati su autorizzazione espressa dell'autore. Non sono introdotti temi successivi, nuove prove di CSB, aritmetica modulare anticipata o codifiche ternarie autonome.

## Risultati assunti e dipendenze dichiarate

- Proprietà usuali di naturali/interi/reali, induzione e buon ordinamento; conteggio finito elementare.
- Assioma della scelta per famiglie arbitrarie di fibre/enumerazioni e la costruzione ricorsiva nell'insieme infinito.
- Cantor–Schröder–Bernstein, confronto totale e formule generali per somme/prodotti di cardinalità infinite: enunciati senza prova.
- Passo analitico che inietta le successioni binarie nei reali; indipendenza di CH: assunti senza prova, distinti da CH stessa, che non viene assunta.
- Nell'esempio J, infinità dei primi e fattorizzazione sono temporaneamente assunte e poi dimostrate nel capitolo sugli interi. Per seno/arcoseno sono dichiarate le proprietà analitiche usuali impiegate.

## Verifiche e risultato

Volume di **35 pagine**, 3 preliminari e 32 di testo; capitoli di 4, 6, 8, 5 e 9 pagine. Tutti i capitoli sono stati riscritti e tutti gli estratti cambiano rispetto alla versione di 34 pagine. Cambiano numerazione dei risultati e raccordi; le copie annotate separate non sono state modificate.

Compilazione condivisa e integrata riuscite. La verifica tecnica dei PDF, le impronte e i confronti degli estratti sono in `VERIFICA_FINALE.json` e nel rapporto condiviso dell'esportazione. Ispezione visiva dell'intero volume, comprese le induzioni e la tabella dei coefficienti; corretti un elenco fuori margine e due raccordi. Nessun registro è incluso nei PDF.

`CONTROLLI_RINASCITA_2026-10-23.json` contiene 32.160 controlli di divisione con tutti i segni e 40.400 coppie per Euclide, con verifica di 159.504 righe di ricorrenza e delle sei righe della tabella stampata. Restano i controlli finiti delle identità insiemistiche e delle applicazioni in `CONTROLLI_INTEGRAZIONE_MZ_2026-10-23.json`. Questi sono riscontri supplementari: non provano i teoremi generali e non costituiscono una certificazione formale o dell'intero programma d'esame.

La ricostruzione sui materiali ricevuti è conclusa. Le prossime lezioni A–L si integrano per nuove unità con questo metodo, senza riaprire da zero i capitoli completati salvo correzioni necessarie. Nessun commit, push o pubblicazione.

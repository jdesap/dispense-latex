# Revisione matematica — 21 ottobre 2026

## Ambito e metodo

Rilettura integrale del contenuto matematico dei sette capitoli di
**Analisi 1**, compresi tutti i file inclusi dal documento principale:
logica; insiemi e relazioni; induzione e combinatoria; numeri reali e
completezza; funzioni; funzioni elementari; topologia della retta.

Controllati gli enunciati, le ipotesi, l'ordine dei quantificatori, i
domini, i versi delle disuguaglianze, i passaggi delle dimostrazioni,
gli esempi numerici e le formule dei grafici TikZ. Confronto mirato delle
nozioni di completezza, supremo/infimo e punto isolato con le dispense
universitarie di John K. Hunter, University of California, Davis:

- [Numeri, sezioni 2.5–2.6](https://www.math.ucdavis.edu/~hunter/intro_analysis_pdf/ch2.pdf).
- [Topologia, definizione 5.22 ed esempi 5.25–5.27](https://www.math.ucdavis.edu/~hunter/intro_analysis_pdf/ch5.pdf).

La copertura delle pagine delle otto fonti originali è registrata in
`COPERTURA.csv`; la presente revisione riguarda la correttezza matematica
della trascrizione attuale.

## Problemi corretti

1. **Tabella di verità, capitolo 1.** Nella riga con P falsa e Q vera,
   la doppia implicazione era indicata come vera. Corretto il valore in
   falso. Ricontrollate tutte le 28 celle della tabella sulle quattro
   assegnazioni dei valori di verità.
2. **Punto isolato, capitolo 7.** La spiegazione collegava impropriamente
   l'isolamento alla sola presenza di punti esterni in ogni piccolo
   intervallo. Sostituita con la definizione corretta: esiste un raggio
   positivo tale che l'intersezione dell'intorno sferico con l'insieme
   sia il solo punto. Per gli interi è sufficiente il raggio 1/2.
   La mancata apertura di N e Z è ora dimostrata separatamente con un
   punto non intero esplicito in ogni intorno sferico.

## Precisazioni aggiunte

- **Identità dell'inversa, capitolo 5.** Esplicitata la corestrizione
  all'immagine nella seconda identità, affinché coincidano anche i
  codomini delle funzioni confrontate.
- **Parte frazionaria, capitolo 6.** Esplicitato perché 1 sia il periodo
  principale: un periodo positivo T deve soddisfare {T} = {0} = 0,
  quindi deve essere un intero positivo.
- **Esponenziale reale, capitolo 6.** La nota distingue la possibile
  costruzione mediante supremo dalle proprietà utilizzate come note.
  La costruzione completa, le leggi delle potenze reali e le proprietà
  di monotonia e suriettività dell'esponenziale non sono dimostrate nel
  volume attuale. Le prove che le utilizzano dipendono da tali risultati.

## Esito

Nessun altro errore matematico individuato nella rilettura. In particolare
sono stati verificati i ragionamenti per induzione, la formula di Newton,
la dimostrazione dell'irrazionalità della radice di due, il passaggio da
Dedekind all'esistenza degli estremi, i criteri con epsilon, Archimede,
la densità dei razionali, l'esistenza delle radici, le proprietà delle
inverse, le formule iperboliche e dell'esercizio con arcoseno e logaritmo,
le operazioni su aperti e chiusi e gli esempi topologici.

Si tratta di una revisione manuale dell'assistente, con riscontri esterni
mirati, e non di una certificazione indipendente del docente. L'esito
documenta gli errori trovati e il controllo effettuato; non dimostra
l'assenza assoluta di errori residui.

## Verifica dell'output

- Documento ricompilato: `build/main.pdf`, 53 pagine.
- Nessun errore o avviso di compilazione; nessun riferimento non risolto
  e nessuna segnalazione di contenuto fuori margine.
- Ispezionate visivamente le pagine della tabella, delle identità
  dell'inversa, della nota sull'esponenziale, della parte frazionaria e
  dei grafici vicini, dell'esercizio e dei punti isolati.
- I registri restano in `lavoro/`, esclusi dal PDF.

## Controlli aggiuntivi sullo stato aggiornato

Eseguita un'ulteriore rilettura matematica dei sorgenti attivi e
confermate le correzioni sopra descritte. Riscontro aggiuntivo su
supremo, Archimede, densità e radici con
[Jiří Lebl, Basic Analysis, sezione 1.2](https://www.jirka.org/ra/html/sec_setofreals.html).

Confrontate direttamente le immagini di tre punti delle fonti:

- Lezione 6, pagina 10: la definizione di periodicità esclude
  esplicitamente le funzioni costanti; la convenzione della dispensa
  è fedele alla fonte.
- Lezione 8, pagina 12: gli intorni laterali escludono il centro e il
  docente precisa che non sono intorni secondo la definizione generale.
  Ripristinato `-1/5` nell'elenco dei punti di `(-1,1)` per riprodurre
  il segno presente nella fonte. Anche `1/5` era un punto dell'intervallo:
  questo è un riallineamento della trascrizione, non la correzione di
  un'affermazione matematica falsa.
- Lezione 7, pagine 2–4: la definizione rigorosa della potenza a esponente
  reale è espressamente rinviata. Il numero `e` viene presentato con
  un'approssimazione e le proprietà esponenziali sono utilizzate senza
  costruirle da zero. Il limite già segnalato nella nota è quindi reale
  e coerente con la fonte, non una dimostrazione presente nella fonte
  che sia stata omessa dalla trascrizione.

Controlli con aritmetica esatta: 481 coppie di indici per Pascal e
simmetria; 275 casi del binomio di Newton; 186 casi di Bernoulli;
427 casi per parte intera, parte frazionaria e parti positiva/negativa.
Controlli numerici aggiuntivi delle formule: 21 casi per le funzioni
iperboliche e inverse; 103 casi per l'esercizio arcoseno/logaritmo,
compresi gli estremi del dominio e dell'immagine. Tutti riusciti.
I casi finiti supportano il controllo dei calcoli e non sostituiscono
le dimostrazioni degli enunciati universali, rilette separatamente.

Impronte dei sorgenti e del PDF aggiornati conservate in
`CONTROLLI_AGGIUNTIVI_2026-10-21.json`. La revisione non equivale a
un nuovo confronto integrale indipendente di tutte le 110 pagine
di contenuto delle fonti: la copertura rimane quella registrata
nelle sessioni precedenti, con i riscontri mirati appena elencati.

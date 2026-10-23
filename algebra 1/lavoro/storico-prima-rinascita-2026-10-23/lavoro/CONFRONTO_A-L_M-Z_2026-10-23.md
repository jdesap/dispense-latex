# Revisione corrente A–L / M–Z — 23 ottobre 2026

## Criterio concordato

Jude frequenta A–L e caricherà progressivamente le lezioni A–L. Questa serie determina il flusso, all’interno dei cinque capitoli per macroargomento. M–Z integra prove e passaggi mancanti, ma anche contenuti del tutto omessi all’interno di argomenti già conclusi in A–L. Non si anticipano nuovi temi plausibilmente rinviati. Per cambiare l’ossatura in favore di M–Z occorre chiedere all’autore.

L’autore ha confermato esplicitamente l’integrazione del confronto totale fra cardinalità e delle formule per somme/prodotti infiniti come enunciati assunti. Non è stata adottata una corrispondenza fra lezioni di uguale numero.

## Evidenza e conservazione

- A–L: 11 PDF, 65 pagine; M–Z: 11 PDF, 75 pagine. Tutte le pagine M–Z sono state lette visivamente; le pagine A–L erano state lette integralmente e quelle interessate dall’ordine e dai refusi sono state ricontrollate.
- Originali immutati, copie byte-identiche e impronte in `fonti/manifest.json`. M–Z è conservato separatamente in `fonti/M-Z/`.
- `COPERTURA.csv` mantiene 65 locator A–L; `CONFRONTO_MZ.csv` contiene 75 righe, una per pagina M–Z, con corrispondenze e decisioni.
- La prima revisione e il suo audit sono storici, non evidenze dello stato corrente. I sorgenti precedenti conservati in `storico-prima-mz/capitoli/` erano già successivi alla prima correzione della differenza simmetrica.

## Ripristino del flusso e rimozioni

1. **Insiemi:** operazioni, famiglie, esercizio sull’associatività, prodotti cartesiani, parti/complementi; ordine A–L L1–L2. Il ritorno A–L L3 sull’associatività è ricondotto alla consegna iniziale.
2. **Relazioni:** partizioni prima delle classi; quoziente dopo il risultato sulle classi; esempio incompatibile prima di somma e prodotto dei razionali.
3. **Funzioni:** esempi prima di iniettività/suriettività; esercizio a tratti prima della funzione del piano; biettività dopo le fibre nel punto A–L L5. Identità e notazione delle frecce ricondotte ai rispettivi punti. La ripresa effettiva di J in A–L L6 è accorpata al primo esercizio.
4. **Cardinalità:** eliminata la dimostrazione autonoma di Cantor–Schröder–Bernstein, assente da entrambe le serie. Eliminato il lemma dei cassetti con dimostrazione autonoma: il fatto finito usato nella prova è dichiarato assunto, come nelle fonti. Le domande finali A–L L8 precedono la trattazione di R di L9. Il materiale M–Z sull’aritmetica cardinale segue la trattazione A–L, con risultati assunti.
5. **Interi:** primi, infinità e crivello precedono MCD; seguono mcm, combinazioni/coprimalità, divisione, Euclide/Bézout, minimo positivo, lemma di Euclide, fattorizzazione e formule, radice di un primo. È l’ordine A–L L9–L11. La coprimalità dopo divisione per MCD è provata direttamente dalla definizione, senza anticipare Bézout.
6. Eliminati la prova ternaria autonoma della cardinalità di R, il risultato più forte non richiesto su A^B e l’ottimizzazione del crivello mediante radice quadrata. Conservate le correzioni certe e i completamenti strettamente necessari alle prove delle fonti.

## Integrazioni effettive da M–Z

| Fonte M–Z | Contenuto | Destinazione |
|---|---|---|
| L1 p.2 | Proprietà universali di unione/intersezione di famiglie | Insiemi, dopo definizione famiglie |
| L1 p.1; L2 pp.3–5; L3 p.1 | Tabelle delle operazioni; descrizioni per elementi/proprietà; implicazione, negazione e controesempio; esercizio sulla negazione | Insiemi, dopo leggi fra operazioni |
| L4 pp.3–4 | Criterio generale di compatibilità di un’operazione con il quoziente | Relazioni, dopo razionali e buona definizione |
| L4 p.5 | Quadrato con dominio non positivo | Funzioni, confronto con l’esempio A–L |
| L5 pp.2–3 | Prove separate di iniettività/suriettività della funzione del piano | Funzioni, consegna A–L L4 p.6 |
| L5 pp.4–5 | Iniettività iff equivalenza indotta uguale all’uguaglianza; fibre aggiuntive, inclusa [168] | Funzioni, fibre |
| L5 pp.7–8 | Inclusioni fra immagine/controimmagine e criteri delle uguaglianze; controimmagine vuota | Funzioni, dopo esempio quadrato |
| L6 p.6 | Esercizio su due inverse destre del seno | Funzioni, dopo criteri inverse |
| L7 pp.1–2 | Soluzione dell’esercizio a tratti ripreso tardi | Accorpata alla consegna A–L |
| L7 pp.5–7 | Famiglie indicizzate come funzioni | Funzioni, insieme delle funzioni |
| L8 p.6 | Totalità del confronto cardinale | Cardinalità, confronto; assunto |
| L8 p.7 | Indecidibilità relativa dell’ipotesi del continuo | Cardinalità, osservazione; assunta senza prova |
| L9 pp.2–3 | Conferma del limite analitico della prova del continuo | Cardinalità di R |
| L9 pp.4–5 | Somma/prodotto di cardinalità infinite | Fine del capitolo cardinalità; assunti |
| L9 pp.8–9 | Coprimalità dopo divisione per MCD senza Bézout | Interi, punto A–L L10 |
| L11 pp.1–2 | Non unicità coefficienti Bézout; insieme combinazioni = MCD Z | Interi, dopo Bézout e criterio coprimalità |
| L11 p.5 | Divisori coprimi di c implicano che il prodotto divide c | Interi, dopo lemma di Euclide |

I passaggi dimostrativi mancanti negli esercizi M–Z sono svolti nel testo; non si attribuisce al docente lo sviluppo aggiuntivo. Varianti dei medesimi esempi (città/persone, frazioni, intervalli) sono confrontate senza duplicare ogni dato numerico: conservati i dati A–L.

## Correzioni e limiti matematici correnti

- **Differenza simmetrica:** prova per le quattro regioni A0, B0, C0, T. Nessun uso di parità, funzioni caratteristiche o modulo 2. A–L L3 pp.1–2 e M–Z L2 p.6 confermano questo metodo.
- **Esercizio finale A–L L8 p.6:** la fonte chiede **B^A**, con A finito e B numerabile. La prima stesura aveva invertito base/esponente; consegna e soluzione corrette. B^A è numerabile anche nei casi vuoti, spiegati separatamente.
- **Continuo:** la somma binaria proposta in A–L L9 p.1 non è iniettiva su tutte le successioni (1,0,0,…) e (0,1,1,…) hanno somma 1. M–Z L9 p.3 rinvia il passo a un argomento analitico sulle serie senza svilupparlo. È quindi dichiarata assunta l’esistenza dell’iniezione inversa; la prova dei tagli razionali è completa. Non resta una prova completa nascosta dietro una formula sbagliata.
- **Supporto primo J:** come nelle lezioni, l’esempio usa proprietà aritmetiche usuali prima della trattazione formale degli interi. L’assunzione temporanea di infinità dei primi e fattorizzazione è esplicita in nota. Non si sviluppa anticipatamente il teorema fondamentale.
- **Seno:** si assume la biettività della restrizione a [-pi/2,pi/2] e l’identità sin(pi−t)=sin(t), proprietà analitiche usuali; si verificano poi le inverse destre.
- **Prodotto cardinale:** la formula col massimo richiede fattori non vuoti. L’enunciato M–Z L9 pp.4–5 è precisato per evitare il prodotto con cardinalità zero.
- **Ipotesi del continuo:** M–Z L8 p.7 suggerisce anche che la negazione comporti infinite cardinalità intermedie; questa inferenza non è corretta in generale e non è importata. L’indecidibilità è precisata rispetto alla coerenza della teoria usuale con scelta. Il nome storico attribuito al confronto totale nella fonte non è ripreso senza verifica.
- Restano assunti: aritmetica elementare, induzione/buon ordinamento, proprietà di base dei reali, fatto finito sulle iniezioni, scelta dove necessaria, CSB, passo analitico del continuo, confronto totale e aritmetica cardinale generale. Compilazione e controlli finiti non certificano formalmente tutte le dimostrazioni.

## Continuità

Non sono introdotti temi successivi all’orizzonte delle fonti A–L ricevute. L’unicità della fattorizzazione, rinviata da M–Z all’ultima pagina, resta perché è già svolta in A–L L11. Per nuovi caricamenti leggere prima `AGENTS.md` della materia, partire dal delta A–L e non ricostruire da zero la dispensa. Una nuova omissione plausibilmente rinviata va distinta da una lacuna di un argomento concluso, non riempita automaticamente.

Le modifiche alterano testo, ordine, numeri di risultati e impaginazione di tutti e cinque i capitoli. Le copie annotate Goodnotes restano separate. Numeri di pagine, impronte e verifiche correnti sono in `VERIFICA_FINALE.json` e nel manifest degli estratti.

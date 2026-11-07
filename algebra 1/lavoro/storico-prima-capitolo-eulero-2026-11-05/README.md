# Appunti di algebra 1

Dispensa di Jude De Sa'Pinto, organizzata per macroargomenti seguendo i 16 PDF A–L (101 pagine), con confronto dei 16 PDF M–Z (110 pagine) e integrazione dei contenuti pertinenti. Il nome della docente è riportato nella forma presente sulla prima fonte: **Prof.ssa E. Detomi**; il nome completo non è stato ricostruito per supposizione.

- Volume completo: [build/main.pdf](build/main.pdf).
- Estratti automatici: [build/capitoli/](build/capitoli/), un PDF per ciascuno dei sette capitoli numerati.
- Testo modificabile: `main.tex`, `preambolo.tex`, `capitoli/`.
- Originali conservati: `fonti/`; nomi originari, percorso di provenienza e impronte in `fonti/manifest.json`.
- Copertura pagina per pagina: `lavoro/COPERTURA.csv` (A–L) e `lavoro/CONFRONTO_MZ.csv` (110 pagine M–Z).
- Registro corrente: `lavoro/LEZIONE_16_2026-11-05.md`, successivo alle lezioni 13–15; scelte delle prove, prerequisiti e passaggi verificati in `lavoro/SCELTA_DIMOSTRAZIONI.csv` (126 unità integrate, inclusi i tre rinvii D01–D03 ora recuperati).
- Sessioni e versioni precedenti: `lavoro/SESSIONI.md`; le sessioni 1–2 e i vecchi registri sono storici. Snapshot completo precedente in `lavoro/storico-prima-rinascita-2026-10-23/`.
- Verifiche riproducibili: `lavoro/verifiche/`; risultati correnti in `lavoro/VERIFICA_FINALE.json`.

## Organizzazione

1. **Insiemi e operazioni**: operazioni, famiglie, prodotti cartesiani, parti, complementi e logica delle appartenenze.
2. **Relazioni, equivalenze e quozienti**: ordini, classi, partizioni, razionali, buona definizione e compatibilità sul quoziente.
3. **Funzioni**: proprietà, fibre, immagini, composizione, inverse e funzioni caratteristiche.
4. **Insiemi finiti, infiniti e cardinalità**: caratterizzazioni dell'infinito, confronto, numerabilità, continuo e somme/prodotti di cardinalità infinite.
5. **Aritmetica degli interi**: primi, MCD/mcm, divisione, Euclide, Bézout e fattorizzazione, nel flusso A–L; riprese M–Z della lezione 12 integrate nei punti pertinenti.
6. **Aritmetica modulare**: congruenze, classi resto, operazioni, invertibili e divisori dello zero; criteri MCD, congruenze lineari, riduzioni, sistemi e teorema cinese del resto.
7. **Anelli e campi**: assiomi e convenzioni, esempi numerici, polinomi, parti, funzioni, matrici, unità, domini/campi e prodotti di anelli; morfismi, isomorfismi, lettura strutturale del teorema cinese e funzione di Eulero.

**Riferimento permanente: A–L.** L’autore frequenta questo canale e i prossimi caricamenti ordinari saranno A–L. M–Z integra passaggi e contenuti omessi in argomenti già conclusi; non anticipa sviluppi plausibilmente rinviati. Le riprese effettive delle lezioni sono accorpate al punto pertinente. Per adottare l’ordine M–Z occorre chiedere all’autore. Le regole sono anche in `AGENTS.md` della materia.

Stato corrente: **lezione 16 A–L integrata con confronto M–Z; 58 pagine (4 preliminari + 54 di testo)**. La prossima lezione A–L da integrare è la **17**. I sette capitoli hanno 4, 6, 8, 5, 10, 10 e 11 pagine; le rispettive pagine stampate sono 1–4, 5–10, 11–18, 19–23, 24–33, 34–43 e 44–54.

Il confronto ha accorpato le riprese di U(R), unità modulo12/modulo primo e tavole modulo6 nel capitolo7. La biezione fra parti e caratteristiche resta dimostrata nel capitolo3; qui si aggiunge soltanto la verifica delle operazioni modulo2. Il teorema cinese costruttivo resta nel capitolo6; nel7 ne sono sviluppati il morfismo, l'isomorfismo per moduli coprimi e il corollario a più fattori, completando i passaggi lasciati come compito. Conservati anche il metodo alternativo con cardinalità finite, la valutazione di polinomi, le fibre della mappa non coprima Z12→Z2×Z6 e l'esercizio affine modulo36.

Morfismi ed Eulero sono ora introdotti da A–L16: i tre rinvii D01–D03 sono recuperati integralmente e `lavoro/MATERIALE_MZ_DA_RIPRENDERE.json` non ha unità pendenti. M–Z16 completa lo stesso tema di Eulero con moltiplicatività per coprimi, formula dalla fattorizzazione ed esempio600; le provenienze sono distinte nei registri. Non sono anticipati il teorema di Eulero/Fermat o la teoria dei gruppi. Le affermazioni informali sulla mancata conservazione di somme/prodotti sono precisate come “non in generale”, con controesempi; nel conteggio modulo p^k è incluso lo zero fra i multipli esclusi.

Cambia il capitolo7 e si aggiorna l'indice; capitoli1–6 con sorgenti, contenuto, numerazione e rendering delle43 pagine invariati. Non c'è riallineamento automatico delle annotazioni Goodnotes. Le copie annotate non sono modificate.

Compilazione condivisa e integrata riuscite senza avvisi; sette estratti verificati su tutte54 pagine per testo, flussi, formato, numerazione, pixel e collegamenti. Ispezione visiva dell'indice e dell'intero capitolo7. Riscontri finiti supplementari in `lavoro/CONTROLLI_LEZIONE_16_2026-11-05.json`: conteggio diretto di Eulero per999 moduli, moltiplicatività su1.448 coppie coprime,256 coppie di sottoinsiemi e tutte le classi degli esercizi nuovi. Questi riscontri non sostituiscono le dimostrazioni generali. Snapshot prima della sessione: `lavoro/storico-prima-lezione-16-2026-11-05/`.

Il testo è stato ricostruito per unità dalle fonti, con scelta motivata delle prove tra A–L e M–Z. Sono sviluppati esplicitamente parametro, base, ipotesi e passo delle induzioni. Per Euclide si distinguono terminazione, invariante dei divisori comuni e ricorrenza dei coefficienti di Bézout; sono presenti la tabella dell'algoritmo esteso e la sostituzione a ritroso. Gli esercizi hanno consegna e svolgimento separati.

L'associatività della differenza simmetrica usa soltanto regioni di insiemi. CSB, confronto totale, aritmetica cardinale generale e il passo analitico per la cardinalità di R restano risultati dichiarati assunti: non sono sostituiti da prove autonome estranee al flusso. I registri documentano le dipendenze e le correzioni. La copertura riguarda le fonti ricevute, non certifica l'intero programma d'esame.

## Compilazione e uso

Aprire questa cartella o la raccolta in VS Code e salvare: LaTeX Workshop usa `.latexmkrc` e la configurazione condivisa `../strumenti/latexmk-comune.pl`. Dal terminale, nella cartella della materia, eseguire `latexmk -pdf main.tex`. Il compilatore integrato di Codex permette anche l'anteprima del progetto; per aggiornare i PDF esportati si usa la compilazione condivisa.

L'esportazione riconosce i capitoli dai segnalibri numerati. Pagine, formule, disegni e numerazione stampata provengono direttamente dal volume. I link interni restano interni; i rimandi ad altri capitoli puntano a `../main.pdf` tramite collegamenti PDF remoti. Per seguirli occorre conservare la struttura delle cartelle e usare un lettore che supporti tali collegamenti. Importando un solo capitolo in Goodnotes, il testo del rimando resta leggibile, ma non è garantita l'apertura del volume esterno.

Le copie annotate in Goodnotes restano separate dai PDF rigenerati. Una nuova impaginazione non riallinea automaticamente le annotazioni. Non sono state modificate copie annotate né eseguiti commit o pubblicazioni.

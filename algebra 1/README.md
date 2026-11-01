# Appunti di algebra 1

Dispensa di Jude De Sa'Pinto, organizzata per macroargomenti seguendo i 15 PDF A–L (97 pagine), con confronto dei 15 PDF M–Z (106 pagine) e integrazione dei contenuti pertinenti. Il nome della docente è riportato nella forma presente sulla prima fonte: **Prof.ssa E. Detomi**; il nome completo non è stato ricostruito per supposizione.

- Volume completo: [build/main.pdf](build/main.pdf).
- Estratti automatici: [build/capitoli/](build/capitoli/), un PDF per ciascuno dei sette capitoli numerati.
- Testo modificabile: `main.tex`, `preambolo.tex`, `capitoli/`.
- Originali conservati: `fonti/`; nomi originari, percorso di provenienza e impronte in `fonti/manifest.json`.
- Copertura pagina per pagina: `lavoro/COPERTURA.csv` (A–L) e `lavoro/CONFRONTO_MZ.csv` (106 pagine M–Z).
- Registro corrente: `lavoro/LEZIONI_13-15_2026-11-01.md`, successivo alla lezione 12 e alla ricostruzione del 23 ottobre; scelte delle prove, prerequisiti e passaggi verificati in `lavoro/SCELTA_DIMOSTRAZIONI.csv` (113 unità: 110 integrate e 3 rinvii didattici espliciti).
- Sessioni e versioni precedenti: `lavoro/SESSIONI.md`; le sessioni 1–2 e i vecchi registri sono storici. Snapshot completo precedente in `lavoro/storico-prima-rinascita-2026-10-23/`.
- Verifiche riproducibili: `lavoro/verifiche/`; risultati correnti in `lavoro/VERIFICA_FINALE.json`.

## Organizzazione

1. **Insiemi e operazioni**: operazioni, famiglie, prodotti cartesiani, parti, complementi e logica delle appartenenze.
2. **Relazioni, equivalenze e quozienti**: ordini, classi, partizioni, razionali, buona definizione e compatibilità sul quoziente.
3. **Funzioni**: proprietà, fibre, immagini, composizione, inverse e funzioni caratteristiche.
4. **Insiemi finiti, infiniti e cardinalità**: caratterizzazioni dell'infinito, confronto, numerabilità, continuo e somme/prodotti di cardinalità infinite.
5. **Aritmetica degli interi**: primi, MCD/mcm, divisione, Euclide, Bézout e fattorizzazione, nel flusso A–L; riprese M–Z della lezione 12 integrate nei punti pertinenti.
6. **Aritmetica modulare**: congruenze, classi resto, operazioni, invertibili e divisori dello zero; criteri MCD, congruenze lineari, riduzioni, sistemi e teorema cinese del resto.
7. **Anelli e campi**: assiomi e convenzioni, esempi numerici, polinomi, parti, funzioni, matrici, unità, domini/campi e prodotti di anelli.

**Riferimento permanente: A–L.** L’autore frequenta questo canale e i prossimi caricamenti ordinari saranno A–L. M–Z integra passaggi e contenuti omessi in argomenti già conclusi; non anticipa sviluppi plausibilmente rinviati. Le riprese effettive delle lezioni sono accorpate al punto pertinente. Per adottare l’ordine M–Z occorre chiedere all’autore. Le regole sono anche in `AGENTS.md` della materia.

Stato corrente: **lezioni 13, 14 e 15 A–L integrate e confrontate con M–Z; 53 pagine (4 preliminari + 49 di testo)**. La prossima lezione A–L da integrare è la **16**. Capitoli di 4, 6, 8, 5, 10, 10 e 6 pagine, alle pagine stampate 1–4, 5–10, 11–18, 19–23, 24–33, 34–43 e 44–49.

Le sovrapposizioni sono state accorpate: operazioni, invertibili e criteri MCD non sono ripetuti; l’elenco delle unità modulo 84 completa lo svolgimento già esistente. Il capitolo 6 prosegue con congruenze lineari, conteggio delle classi, semplificazioni e sistemi; il capitolo 7 raccoglie gli anelli per macroargomento. Capitoli 1–5: sorgenti, contenuto, numerazione e rendering delle 33 pagine invariati. Cambia il capitolo 6 e si aggiunge il 7; l’indice è aggiornato. Non c’è riallineamento automatico delle annotazioni Goodnotes.

Sono confrontate e motivate le dimostrazioni: Bézout, tutte le soluzioni, conteggio delle classi e teorema cinese; negli esempi restano sostituzione e costruzione diretta come metodi distinti. Le convenzioni di anello con/senza unità e di divisore dello zero inclusivo dello zero sono esplicite. Corretta la generalizzazione M–Z sui sistemi con coefficienti arbitrari: occorre prima controllare la risolubilità di ogni congruenza.

I morfismi e gli sviluppi M–Z che ne dipendono sono nuovi rispetto ad A–L 15 e restano rinviati con locator e motivi in `lavoro/MATERIALE_MZ_DA_RIPRENDERE.json` (D01–D03). Non sono segnati come già integrati. Nessuna anticipazione della funzione di Eulero, soltanto annunciata nella fonte.

Compilazione senza avvisi; tutti i sette estratti verificati su 49 pagine per testo, flussi, formato, numerazione, pixel e collegamenti. Ispezione visiva di tutte le pagine nuove/variate. Riscontri numerici supplementari in `lavoro/CONTROLLI_LEZIONI_13-15_2026-11-01.json`: 91.871 congruenze, 339 sistemi CRT, 289 elementi di prodotti di campi e 2.401 matrici. Questi controlli non sostituiscono le dimostrazioni generali. Snapshot prima della sessione in `lavoro/storico-prima-lezioni-13-15-2026-11-01/`.

Il testo è stato ricostruito per unità dalle fonti, con scelta motivata delle prove tra A–L e M–Z. Sono sviluppati esplicitamente parametro, base, ipotesi e passo delle induzioni. Per Euclide si distinguono terminazione, invariante dei divisori comuni e ricorrenza dei coefficienti di Bézout; sono presenti la tabella dell'algoritmo esteso e la sostituzione a ritroso. Gli esercizi hanno consegna e svolgimento separati.

L'associatività della differenza simmetrica usa soltanto regioni di insiemi. CSB, confronto totale, aritmetica cardinale generale e il passo analitico per la cardinalità di R restano risultati dichiarati assunti: non sono sostituiti da prove autonome estranee al flusso. I registri documentano le dipendenze e le correzioni. La copertura riguarda le fonti ricevute, non certifica l'intero programma d'esame.

## Compilazione e uso

Aprire questa cartella o la raccolta in VS Code e salvare: LaTeX Workshop usa `.latexmkrc` e la configurazione condivisa `../strumenti/latexmk-comune.pl`. Dal terminale, nella cartella della materia, eseguire `latexmk -pdf main.tex`. Il compilatore integrato di Codex permette anche l'anteprima del progetto; per aggiornare i PDF esportati si usa la compilazione condivisa.

L'esportazione riconosce i capitoli dai segnalibri numerati. Pagine, formule, disegni e numerazione stampata provengono direttamente dal volume. I link interni restano interni; i rimandi ad altri capitoli puntano a `../main.pdf` tramite collegamenti PDF remoti. Per seguirli occorre conservare la struttura delle cartelle e usare un lettore che supporti tali collegamenti. Importando un solo capitolo in Goodnotes, il testo del rimando resta leggibile, ma non è garantita l'apertura del volume esterno.

Le copie annotate in Goodnotes restano separate dai PDF rigenerati. Una nuova impaginazione non riallinea automaticamente le annotazioni. Non sono state modificate copie annotate né eseguiti commit o pubblicazioni.

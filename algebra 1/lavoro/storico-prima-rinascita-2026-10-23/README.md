# Appunti di algebra 1

Dispensa di Jude De Sa'Pinto, organizzata per macroargomenti seguendo gli 11 PDF A–L (65 pagine), con confronto e integrazione degli 11 PDF M–Z (75 pagine). Il nome della docente è riportato nella forma presente sulla prima fonte: **Prof.ssa E. Detomi**; il nome completo non è stato ricostruito per supposizione.

- Volume completo: [build/main.pdf](build/main.pdf).
- Estratti automatici: [build/capitoli/](build/capitoli/), un PDF per ciascuno dei cinque capitoli numerati.
- Testo modificabile: `main.tex`, `preambolo.tex`, `capitoli/`.
- Originali conservati: `fonti/`; nomi originari, percorso di provenienza e impronte in `fonti/manifest.json`.
- Copertura pagina per pagina: `lavoro/COPERTURA.csv` (A–L) e `lavoro/CONFRONTO_MZ.csv` (75 pagine M–Z).
- Sessioni, correzioni e limiti: `lavoro/SESSIONI.md` e `lavoro/CONFRONTO_A-L_M-Z_2026-10-23.md`; il registro della prima stesura resta storico.
- Verifiche riproducibili: `lavoro/verifiche/`; risultati correnti in `lavoro/VERIFICA_FINALE.json`.

## Organizzazione

1. **Insiemi e operazioni**: operazioni, famiglie, prodotti cartesiani, parti, complementi e logica delle appartenenze.
2. **Relazioni, equivalenze e quozienti**: ordini, classi, partizioni, razionali, buona definizione e compatibilità sul quoziente.
3. **Funzioni**: proprietà, fibre, immagini, composizione, inverse e funzioni caratteristiche.
4. **Insiemi finiti, infiniti e cardinalità**: caratterizzazioni dell'infinito, confronto, numerabilità, continuo e somme/prodotti di cardinalità infinite.
5. **Aritmetica degli interi**: primi, MCD/mcm, divisione, Euclide, Bézout e fattorizzazione, nel flusso A–L.

**Riferimento permanente: A–L.** L’autore frequenta questo canale e i prossimi caricamenti ordinari saranno A–L. M–Z integra passaggi e contenuti omessi in argomenti già conclusi; non anticipa sviluppi plausibilmente rinviati. Le riprese effettive delle lezioni sono accorpate al punto pertinente. Per adottare l’ordine M–Z occorre chiedere all’autore. Le regole sono anche in `AGENTS.md` della materia.

Stato corrente: **34 pagine (3 preliminari + 31 di testo)**, cinque capitoli di 5, 5, 8, 5 e 8 pagine. Tutti sono cambiati rispetto alla prima stesura; impaginazione e numerazione dei risultati sono aggiornate. Gli esercizi delle fonti sono mantenuti e svolti; corretto il refuso B^A/A^B nella vecchia trascrizione.

La dimostrazione dell’associatività della differenza simmetrica usa le regioni degli insiemi. CSB, il passo analitico per la cardinalità di R e i risultati generali di confronto/aritmetica cardinale sono dichiarati assunti dove le prove non sono sviluppate. Le vecchie prove autonome di CSB e del continuo mediante cifre ternarie sono state rimosse. Provenienze, integrazioni e limiti sono nel registro corrente; la copertura riguarda le fonti ricevute, non certifica l’intero programma d’esame. Gli annunci amministrativi delle fonti non sono istruzioni operative.

## Compilazione e uso

Aprire questa cartella o la raccolta in VS Code e salvare: LaTeX Workshop usa `.latexmkrc` e la configurazione condivisa `../strumenti/latexmk-comune.pl`. Dal terminale, nella cartella della materia, eseguire `latexmk -pdf main.tex`. Il compilatore integrato di Codex permette anche l'anteprima del progetto; per aggiornare i PDF esportati si usa la compilazione condivisa.

L'esportazione riconosce i capitoli dai segnalibri numerati. Pagine, formule, disegni e numerazione stampata provengono direttamente dal volume. I link interni restano interni; i rimandi ad altri capitoli puntano a `../main.pdf` tramite collegamenti PDF remoti. Per seguirli occorre conservare la struttura delle cartelle e usare un lettore che supporti tali collegamenti. Importando un solo capitolo in Goodnotes, il testo del rimando resta leggibile, ma non è garantita l'apertura del volume esterno.

Le copie annotate in Goodnotes restano separate dai PDF rigenerati. Una nuova impaginazione non riallinea automaticamente le annotazioni. Non sono state modificate copie annotate né eseguiti commit o pubblicazioni.

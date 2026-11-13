# Appunti di algebra 1

**Revisione editoriale del 13 novembre 2026:** enunciati distinti e parti delle prove numerati in corrispondenza, senza abbreviazioni. Volume corrente: **69 pagine**; estratti di capitolo: 5, 6, 8, 5, 10, 10, 9, 12 pagine. [Resoconto e verifiche](../strumenti/NUMERAZIONE_ENUNCIATI_2026-11-13.md). I conteggi nei resoconti delle integrazioni precedenti descrivono le rispettive versioni storiche.

Dispensa di Jude De Sa'Pinto, organizzata per macroargomenti seguendo i 18 PDF A–L (119 pagine), con confronto dei 18 PDF M–Z (123 pagine) e integrazione dei contenuti pertinenti. Il nome della docente è riportato nella forma presente sulla prima fonte: **Prof.ssa E. Detomi**; il nome completo non è stato ricostruito per supposizione.

- Volume completo: [build/main.pdf](build/main.pdf).
- Estratti automatici: [build/capitoli/](build/capitoli/), un PDF per ciascuno degli otto capitoli numerati.
- Testo modificabile: `main.tex`, `preambolo.tex`, `capitoli/`.
- Originali conservati: `fonti/`; nomi originari, percorso di provenienza e impronte in `fonti/manifest.json`.
- Copertura pagina per pagina: `lavoro/COPERTURA.csv` (A–L) e `lavoro/CONFRONTO_MZ.csv` (123 pagine M–Z).
- Registro corrente: `lavoro/LEZIONI_17-18_2026-11-11.md`, successivo alla ricollocazione di Eulero nel capitolo8; scelte delle prove, prerequisiti e passaggi verificati in `lavoro/SCELTA_DIMOSTRAZIONI.csv` (147 unità:146 integrate e1 esempio M–Z rinviato per prerequisiti).
- Sessioni e versioni precedenti: `lavoro/SESSIONI.md`; le sessioni 1–2 e i vecchi registri sono storici. Snapshot completo precedente in `lavoro/storico-prima-rinascita-2026-10-23/`.
- Verifiche riproducibili: `lavoro/verifiche/`; risultati correnti in `lavoro/VERIFICA_FINALE.json`.

## Organizzazione

1. **Insiemi e operazioni**: operazioni, famiglie, prodotti cartesiani, parti, complementi e logica delle appartenenze.
2. **Relazioni, equivalenze e quozienti**: ordini, classi, partizioni, razionali, buona definizione e compatibilità sul quoziente.
3. **Funzioni**: proprietà, fibre, immagini, composizione, inverse e funzioni caratteristiche.
4. **Insiemi finiti, infiniti e cardinalità**: caratterizzazioni dell'infinito, confronto, numerabilità, continuo e somme/prodotti di cardinalità infinite.
5. **Aritmetica degli interi**: primi, MCD/mcm, divisione, Euclide, Bézout e fattorizzazione, nel flusso A–L; riprese M–Z della lezione 12 integrate nei punti pertinenti.
6. **Aritmetica modulare**: congruenze, classi resto, operazioni, invertibili e divisori dello zero; criteri MCD, congruenze lineari, riduzioni, sistemi e teorema cinese del resto.
7. **Anelli e campi**: assiomi e convenzioni, esempi numerici, polinomi, parti, funzioni, matrici, unità, domini/campi e prodotti di anelli; morfismi, isomorfismi e lettura strutturale del teorema cinese.
8. **Funzione di Eulero e gruppi**: phi e unità, gruppi e potenze, simmetrico e affini, sottogruppi e generati, coniugati, centralizzanti e centri. Sottomoduli08a–08c inclusi nello stesso capitolo, senza estratti separati.

**Riferimento permanente: A–L.** L’autore frequenta questo canale e i prossimi caricamenti ordinari saranno A–L. M–Z integra passaggi e contenuti omessi in argomenti già conclusi; non anticipa sviluppi plausibilmente rinviati. Le riprese effettive delle lezioni sono accorpate al punto pertinente. Per adottare l’ordine M–Z occorre chiedere all’autore. Le regole sono anche in `AGENTS.md` della materia.

Stato corrente: **lezioni17–18 A–L integrate con confronto M–Z;69 pagine (4 preliminari+65 di testo)**. Prossima lezione A–L: **19**. Gli otto capitoli hanno 5, 6, 8, 5, 10, 10, 9 e 12 pagine. Le verifiche e i conteggi dell’integrazione dell’11 novembre, richiamati sotto, sono storici; per l’impaginazione corrente vale la verifica del 13 novembre collegata in apertura.

Le riprese di phi, della moltiplicatività e dell'esempio600 in AL17 sono accorpate al testo già presente. Nel7 sono aggiunti i termini omomorfismo ed endomorfismo; nel8 prosegue soltanto il materiale delle lezioni ricevute: gruppi, potenze, permutazioni, affini, sottogruppi, coniugati e centralizzanti. La paginaAL18:1 ripeteAL17:9 ed è trattata una sola volta. Conservati i due esempi distinti di composizione di permutazioni e i due sottogruppi razionali delle affinità (solo pendenza razionale, oppure entrambi coefficienti razionali).

I passaggi lasciati come compito sono sviluppati: criteri/intersezioni/unioni, generati, traslazioni, punti fissi, potenze inS5, coniugati inS4, centralizzanti e centri diS3 eAff(R). Distinte composizione e prodotto puntuale sulle funzioni; precisato che l'estremo superiore è il minimo sottogruppo contenente entrambi. Per il centralizzante di una traslazione è esplicita l'ipotesi parametro non nullo e il caso identità è trattato separatamente. I simboli sono introdotti prima dell'uso; i due diagrammi TikZ sono verificati matematicamente e nel PDF.

D01–D03 restano recuperati. Il solo rinvio attuale è **D04**, l'esempio M–Z17:3 sull'anello End_K(V) e sul gruppo degli automorfismi lineari, che richiede spazi vettoriali e linearità non introdotti nel flusso corrente di Algebra. Locator e contenuto sono conservati in `lavoro/MATERIALE_MZ_DA_RIPRENDERE.json`. Nessuna pagina A–L17–18 resta da integrare. Non sono anticipati Lagrange o il teorema di Eulero.

Aggiornato anche [l'indice delle dimostrazioni](../DIMOSTRAZIONI_DA_STUDIARE.md), secondo il protocollo A/B/C: metodi comuni raggruppati, priorità motivate, collegamenti ai sorgenti correnti e rinvii distinti. Preservate le annotazioni e tutte le sezioni delle altre materie; nessuno stato personale di studio attribuito.

Cambiano i capitoli7 e8 e l'indice; il7 resta di9 pagine, l'8 passa da2 a10. Capitoli1–6 con sorgenti e rendering delle43 pagine invariati; nel7 cambiano solo le pagine stampate44 e49. Le copie annotate restano separate e intatte.

Compilazione condivisa senza avvisi e compilazione integrata riuscite. Tutti otto estratti e tutte62 pagine verificati per testo, flussi, formato, numerazione, pixel e link. Ispezionati indice, pagine modificate del7, intero8 e i due diagrammi. Tutti36 originali byte-identici. Riscontri supplementari riproducibili in `lavoro/verifiche/controlli_lezioni_17_18.py`:576 prodotti inS4,64 sottoinsiemi/centralizzanti e36 coppie di sottogruppi inS3,486 identità di potenze,900 coppie di affinità razionali, tutti gli esempi scritti. I riscontri finiti non sostituiscono il riesame delle prove per unità. Risultati in `lavoro/CONTROLLI_LEZIONI_17-18_2026-11-11.json` e `lavoro/VERIFICA_FINALE.json`; snapshot precedente `lavoro/storico-prima-lezioni-17-18-2026-11-11/`.

Il testo è stato ricostruito per unità dalle fonti, con scelta motivata delle prove tra A–L e M–Z. Sono sviluppati esplicitamente parametro, base, ipotesi e passo delle induzioni. Per Euclide si distinguono terminazione, invariante dei divisori comuni e ricorrenza dei coefficienti di Bézout; sono presenti la tabella dell'algoritmo esteso e la sostituzione a ritroso. Gli esercizi hanno consegna e svolgimento separati.

L'associatività della differenza simmetrica usa soltanto regioni di insiemi. CSB, confronto totale, aritmetica cardinale generale e il passo analitico per la cardinalità di R restano risultati dichiarati assunti: non sono sostituiti da prove autonome estranee al flusso. I registri documentano le dipendenze e le correzioni. La copertura riguarda le fonti ricevute, non certifica l'intero programma d'esame.

## Compilazione e uso

Aprire questa cartella o la raccolta in VS Code e salvare: LaTeX Workshop usa `.latexmkrc` e la configurazione condivisa `../strumenti/latexmk-comune.pl`. Dal terminale, nella cartella della materia, eseguire `latexmk -pdf main.tex`. Il compilatore integrato di Codex permette anche l'anteprima del progetto; per aggiornare i PDF esportati si usa la compilazione condivisa.

L'esportazione riconosce i capitoli dai segnalibri numerati. Pagine, formule, disegni e numerazione stampata provengono direttamente dal volume. I link interni restano interni; i rimandi ad altri capitoli puntano a `../main.pdf` tramite collegamenti PDF remoti. Per seguirli occorre conservare la struttura delle cartelle e usare un lettore che supporti tali collegamenti. Importando un solo capitolo in Goodnotes, il testo del rimando resta leggibile, ma non è garantita l'apertura del volume esterno.

Le copie annotate in Goodnotes restano separate dai PDF rigenerati. Una nuova impaginazione non riallinea automaticamente le annotazioni. Non sono state modificate copie annotate né eseguiti commit o pubblicazioni.

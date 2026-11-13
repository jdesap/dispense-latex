# Appunti di algebra 1

**Stato corrente — 13 novembre 2026:** lezioni **19–20 A–L integrate**, con confronto M–Z; completata la **revisione totale di completezza e chiarezza degli otto capitoli**. Prossima lezione A–L: **21**. Volume: **83 pagine**, 4 preliminari e79 di testo; otto estratti di5,6,9,6,10,11,10 e22 pagine. Rispetto alla versione79 pagine cambiano tutti gli otto capitoli e l’indice. Copie annotate separate e non modificate.

Dispensa di Jude De Sa'Pinto, organizzata per macroargomenti seguendo i **20 PDF A–L (138 pagine)**, con confronto dei **20 PDF M–Z (137 pagine)**. Il nome della docente è riportato nella forma presente sulla prima fonte: **Prof.ssa E. Detomi**; il nome completo non è stato ricostruito per supposizione.

- Volume completo: [build/main.pdf](build/main.pdf).
- Estratti automatici: [build/capitoli/](build/capitoli/), un PDF per ciascuno degli otto capitoli numerati; nessun estratto autonomo dei sottomoduli.
- Testo modificabile: `main.tex`, `preambolo.tex`, `capitoli/`.
- Originali conservati: `fonti/`; nomi, provenienze e impronte in `fonti/manifest.json` (40 PDF,275 pagine).
- Copertura pagina per pagina: `lavoro/COPERTURA.csv` (138 pagine A–L) e `lavoro/CONFRONTO_MZ.csv` (137 pagine M–Z).
- Registro corrente: [revisione totale](lavoro/revisione-totale-2026-11-13/REVISIONE.md), con inventario per unità e fonti; integrazione19–20 conservata nel relativo resoconto storico. Scelte delle prove, prerequisiti e passaggi in `lavoro/SCELTA_DIMOSTRAZIONI.csv`:155 unità,154 integrate (G28 distingue l’enunciato generale senza prova) e1 esempio M–Z rinviato.
- Sessioni e versioni storiche: `lavoro/SESSIONI.md`; snapshot prima della revisione totale in `lavoro/revisione-totale-2026-11-13/prima/`; precedente integrazione in `lavoro/storico-prima-lezioni-19-20-2026-11-13/`.
- Verifiche riproducibili: `lavoro/verifiche/`; risultati correnti in `lavoro/VERIFICA_FINALE.json`; riscontri finiti della precedente integrazione in `lavoro/CONTROLLI_LEZIONI_19-20_2026-11-13.json`.

## Organizzazione

1. **Insiemi e operazioni**: operazioni, famiglie, prodotti cartesiani, parti, complementi e logica delle appartenenze.
2. **Relazioni, equivalenze e quozienti**: ordini, classi, partizioni, razionali, buona definizione e compatibilità sul quoziente.
3. **Funzioni**: proprietà, fibre, immagini, composizione, inverse e funzioni caratteristiche.
4. **Insiemi finiti, infiniti e cardinalità**: caratterizzazioni dell'infinito, confronto, numerabilità, continuo e somme/prodotti di cardinalità infinite.
5. **Aritmetica degli interi**: primi, MCD/mcm, divisione, Euclide, Bézout e fattorizzazione, nel flusso A–L; riprese M–Z della lezione 12 integrate nei punti pertinenti.
6. **Aritmetica modulare**: congruenze, classi resto, operazioni, invertibili e divisori dello zero; criteri MCD, congruenze lineari, riduzioni, sistemi e teorema cinese del resto.
7. **Anelli e campi**: assiomi e convenzioni, esempi numerici, polinomi, parti, funzioni, matrici, unità, domini/campi e prodotti di anelli; morfismi, isomorfismi e lettura strutturale del teorema cinese.
8. **Funzione di Eulero e gruppi**: phi e unità, gruppi e potenze, simmetrico e affini, sottogruppi e generati, coniugati, centralizzanti e centri, morfismi, ordine e classificazione dei ciclici, sottogruppi/divisori, generatori e primi cicli di permutazioni. Sottomoduli08a–08f inclusi nello stesso capitolo, senza estratti separati.

**Riferimento permanente: A–L.** L’autore frequenta questo canale. M–Z integra prove, passaggi e contenuti pertinenti omessi; non anticipa sviluppi futuri. Le riprese sono accorpate nel punto pertinente. Per adottare l’ordine M–Z occorre chiedere all’autore. Le regole sono in `AGENTS.md` della materia e nel protocollo comune.

Il generato di un insieme X generalizza in08b il caso già presente di due sottogruppi; le riprese del ciclico e delle potenze sono accorpate. Seguono, nello stesso8, tutti i sottogruppi di Z, inclusioni e MCD/mcm, morfismi di gruppi ed esempi affini/esponenziale, ordine degli elementi, due modelli dei ciclici, sottogruppi e divisori, ordine di classi/potenze, generatori e phi, eserciziU16/U17, inclusioni fra simmetrici e primi cicli. Conservati gli esempi distinti delle due serie; reticolo dei sottogruppi di Z contenenti12Z distinto da quello di Z/12Z. Esercizi con consegna e svolgimento separati.

Correzioni registrate: AL20:5 dà divisibilità N|sd, non l’uguaglianza sd=N; l’unicità del sottogruppo si prova col minimo esponente, completando la struttura M–Z. MZ19:3: l’intersezione è il massimo sottogruppo contenuto in entrambi. Ordine/cardinalità e buona definizione non sono usati circolarmente. Casi banali e negativi espliciti; phi resta definita per moduli almeno2. Terminologia: «congrui modulo m».

D01–D03 restano recuperati; D04 (End_K(V)/automorfismi lineari, MZ17:3) resta rinviato perché spazi vettoriali e linearità non sono introdotti nel flusso di Algebra. Le nuove fonti non cambiano questi prerequisiti. Nessuna pagina A–L19–20 resta da integrare. La decomposizione generale in cicli disgiunti è riportata come enunciato senza prova, come nelle fonti, con i due esempi svolti; la prova generale resta da riprendere. Non sono aggiunti Lagrange, teorema di Eulero, segno delle permutazioni o formula generale dell’ordine di una permutazione. Per l’esponenziale si assumono esplicitamente le proprietà analitiche usuali.

Aggiornato [l’indice delle dimostrazioni](../DIMOSTRAZIONI_DA_STUDIARE.md): priorità B per il metodo comune minimo/divisione, classificazione tramite n↦g^n e riduzione dell’ordine tramiteMCD; conseguenze ricostruibili inC. Assunzioni e rinvii separati, annotazioni e altre materie conservate; nessuno stato personale di studio attribuito. I riscontri numerici finiti sono supplementari al riesame delle prove per unità e non costituiscono certificazione formale o copertura dell’intero programma d’esame.

La revisione editoriale precedente del13 novembre (69 pagine) ha numerato gli enunciati distinti e le parti corrispondenti delle prove: [resoconto](../strumenti/NUMERAZIONE_ENUNCIATI_2026-11-13.md). È conservata; la stessa regola è applicata alle nuove unità. I resoconti11 novembre e precedenti descrivono le rispettive versioni storiche (per esempio66 pagine dopo17–18), non il volume corrente.

La revisione totale ha confrontato154 unità integrate e il rinvioD04 con tutte40 fonti:242 pagine1–18 rilette visivamente e33 pagine19–20 già lette nella stessa sessione. Recuperati esempi distinti e terminologia, completate le conseguenze sulla numerabilità e la potenza di potenza, chiariti criterio MCD e caso modulo1; recuperato il compito costruttivo MZ14:5 sui sistemi. Prove conservate, punti corrispondenti numerati,39 esercizi separati dai39 svolgimenti. Tutte83 pagine ispezionate; compilazioni riuscite senza avvisi,79 pagine degli otto estratti e relativi link confrontati con il volume. Il controllo è manuale e documentato; non costituisce certificazione formale.

## Compilazione e uso

Aprire questa cartella o la raccolta in VS Code e salvare: LaTeX Workshop usa `.latexmkrc` e la configurazione condivisa `../strumenti/latexmk-comune.pl`. Dal terminale, nella cartella della materia, eseguire `latexmk -pdf main.tex`. Il compilatore integrato di Codex permette anche l'anteprima del progetto; per aggiornare i PDF esportati si usa la compilazione condivisa.

L'esportazione riconosce i capitoli dai segnalibri numerati. Pagine, formule, disegni e numerazione stampata provengono direttamente dal volume. I link interni restano interni; i rimandi ad altri capitoli puntano a `../main.pdf` tramite collegamenti PDF remoti. Per seguirli occorre conservare la struttura delle cartelle e usare un lettore che supporti tali collegamenti. Importando un solo capitolo in Goodnotes, il testo del rimando resta leggibile, ma non è garantita l'apertura del volume esterno.

Le copie annotate in Goodnotes restano separate dai PDF rigenerati. Una nuova impaginazione non riallinea automaticamente le annotazioni. Non sono state modificate copie annotate né eseguiti commit o pubblicazioni.

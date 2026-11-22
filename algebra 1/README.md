# Appunti di algebra 1

**Aggiornati alla lezione 24 A–L, con confronto M–Z. La prossima è la 25.** L’edizione del 22 novembre 2026 comprende 90 pagine e otto capitoli. Le lezioni 21–24 proseguono il capitolo «Funzione di Eulero e gruppi». Il riesame ha portato anche a correzioni nei capitoli 1, 5, 6 e 7.

Dispensa di Jude De Sa'Pinto. La docente è indicata nella prima fonte come Prof.ssa E. Detomi.

- [Volume completo](build/main.pdf) e [PDF degli otto capitoli](build/capitoli/).
- [Resoconto delle lezioni 21–24 e del riesame](lavoro/LEZIONI_21-24_2026-11-22.md) e [verifiche dell’edizione corrente](lavoro/VERIFICA_FINALE.json).
- [Inventario delle fonti](fonti/manifest.json), con 24 PDF A–L (171 pagine) e 24 PDF M–Z (170 pagine). Il materiale per pagina è nei registri [A–L](lavoro/COPERTURA.csv) e [M–Z](lavoro/CONFRONTO_MZ.csv).
- [Scelte delle dimostrazioni](lavoro/SCELTA_DIMOSTRAZIONI.csv) e [indice per lo studio](../DIMOSTRAZIONI_DA_STUDIARE.md). L’esempio M–Z sugli endomorfismi di uno spazio vettoriale resta nel [registro dei rinvii](lavoro/MATERIALE_MZ_DA_RIPRENDERE.json).
- [Sessioni precedenti](lavoro/SESSIONI.md) e [revisione del 13 novembre](lavoro/revisione-totale-2026-11-13/REVISIONE.md). I sorgenti del volume sono in `main.tex`, `preambolo.tex` e `capitoli/`.

## Organizzazione

1. **Insiemi e operazioni**: operazioni, famiglie, prodotti cartesiani, parti, complementi e logica delle appartenenze.
2. **Relazioni, equivalenze e quozienti**: ordini, classi, partizioni, razionali, buona definizione e compatibilità sul quoziente.
3. **Funzioni**: proprietà, fibre, immagini, composizione, inverse e funzioni caratteristiche.
4. **Insiemi finiti, infiniti e cardinalità**: caratterizzazioni dell'infinito, confronto, numerabilità, continuo e somme/prodotti di cardinalità infinite.
5. **Aritmetica degli interi**: primi, MCD/mcm, divisione, Euclide, Bézout e fattorizzazione, nel flusso A–L; riprese M–Z della lezione 12 integrate nei punti pertinenti.
6. **Aritmetica modulare**: congruenze, classi resto, operazioni, invertibili e divisori dello zero; criteri MCD, congruenze lineari, riduzioni, sistemi e teorema cinese del resto.
7. **Anelli e campi**: assiomi e convenzioni, esempi numerici, polinomi, parti, funzioni, matrici, unità, domini/campi e prodotti di anelli; morfismi, isomorfismi e lettura strutturale del teorema cinese.
8. **Funzione di Eulero e gruppi**. Funzione di Eulero, gruppi, sottogruppi, morfismi e ciclici. Seguono calcolo con le permutazioni, segnatura, gruppi diedrali, classi laterali, Lagrange, Eulero e Fermat, normalità e gruppi quoziente (§§8.8–8.11).

**Riferimento permanente: A–L.** L’autore frequenta questo canale. M–Z integra prove, passaggi e contenuti pertinenti omessi; non anticipa sviluppi futuri. Le riprese sono accorpate nel punto pertinente. Per adottare l’ordine M–Z occorre chiedere all’autore. Le regole sono in `AGENTS.md` della materia e nel protocollo comune.

I registri conservano le correzioni e le scelte precedenti, compresa la prova mediante minimo esponente per i sottogruppi ciclici. Gli esercizi hanno consegna e svolgimento separati. In aritmetica modulare si usa la dizione «congrui modulo m».

## Compilazione e uso

Aprire questa cartella o la raccolta in VS Code e salvare: LaTeX Workshop usa `.latexmkrc` e la configurazione condivisa `../strumenti/latexmk-comune.pl`. Dal terminale, nella cartella della materia, eseguire `latexmk -pdf main.tex`. Il compilatore integrato di Codex permette anche l'anteprima del progetto; per aggiornare i PDF esportati si usa la compilazione condivisa.

L'esportazione riconosce i capitoli dai segnalibri numerati. Pagine, formule, disegni e numerazione stampata provengono direttamente dal volume. I link interni restano interni; i rimandi ad altri capitoli puntano a `../main.pdf` tramite collegamenti PDF remoti. Per seguirli occorre conservare la struttura delle cartelle e usare un lettore che supporti tali collegamenti. Importando un solo capitolo in Goodnotes, il testo del rimando resta leggibile, ma non è garantita l'apertura del volume esterno.

Le copie annotate in Goodnotes restano separate dai PDF rigenerati. Una nuova impaginazione non riallinea automaticamente le annotazioni. Non sono state modificate copie annotate né eseguiti commit o pubblicazioni.

# Appunti di geometria 1

Appunti di **Jude De Sa'Pinto** dal corso del **Prof. Francesco Bottacin**.
La dispensa cresce per sessioni: nel PDF attivo entrano soltanto le parti
confrontate con la fonte, compilate e controllate nell'impaginazione.

## Stato attuale

Sono integrate le **lezioni 5–18** (13 PDF, 65 pagine di fonti).
Il capitolo 1 raccoglie spazi vettoriali e sottospazi; il capitolo 2,
**Sistemi lineari e matrici**, comprende Gauss, rango, prodotto e trasposta,
inverse, sistemi omogenei, Rouché–Capelli ed esercizi con parametro.
Il nuovo capitolo 3, **Applicazioni lineari**, comprende linearità,
isomorfismi, nucleo e immagine, teorema della dimensione, proiezioni e
simmetrie, matrici associate, operazioni e cambiamento di basi.
Il volume aggiornato al 2 novembre 2026 ha **45 pagine**, con 3 preliminari,
26 pagine per il capitolo 1, 7 per il capitolo 2 e 9 per il capitolo 3.
La parte sui numeri complessi resta in attesa di consegna separata.

La revisione editoriale integrale, svolta in quattro sessioni per Spazi
vettoriali, è conclusa. Resoconto comune e verifiche aggiornate in
`../lavoro/revisione-editoriale/RESOCONTO_FINALE.md`.
Le barre laterali, i numeretti blu delle note, il rientro delle prove e le
spaziature si regolano nel blocco **STILE MATEMATICO** di `preambolo.tex`,
I parametri e gli ultimi controlli sono descritti in
`../lavoro/revisione-editoriale/SESSIONE_15.md`.

La prima stesura che raccoglieva tutte le lezioni è conservata in
`lavoro/bozze/` come materiale **non verificato**. Non fa parte del PDF
attivo e non documenta una copertura completa delle fonti.

## Struttura

- `main.tex`: frontespizio, convenzioni, indice per argomento e inclusioni.
- `preambolo.tex`: ambienti, notazioni, impaginazione e stili TikZ.
- `capitoli/`: un file per ogni macroargomento, con sorgenti interni
  separati per temi aggiornabili. Un capitolo può riunire più lezioni.
- `fonti/`: copie dei PDF consegnati e manifest con impronte SHA-256.
- `lavoro/SESSIONI.md`: registro delle sessioni e delle verifiche.
- `lavoro/COPERTURA.csv`: stato di ogni pagina delle fonti.
- `lavoro/REVISIONE_MATEMATICA_2026-10-21.md`: correzioni, controlli
  matematici effettuati e limiti della revisione.
- `lavoro/REVISIONE_LEZIONE_7_2026-10-21.md`: verifica della nuova
  fonte, riordino e controlli della versione aggiornata.
- `lavoro/VERIFICA_LEZIONE_7_2026-10-21.json`: impronte e risultati
  della versione aggiornata.
- `lavoro/bozze/`: materiale preliminare non incluso.
- `build/main.pdf`: PDF attivo compilato.

## Compilazione e aggiornamento

Aprire la cartella in Visual Studio Code e lavorare su `main.tex`;
LaTeX Workshop è configurato in `.vscode/`. Dal terminale:

```sh
latexmk main.tex
```

Salva/Build in VS Code e la compilazione da terminale esportano anche
automaticamente un PDF per ciascun capitolo numerato in `build/capitoli/`.
Anche i nuovi capitoli avranno il proprio PDF, senza un elenco da aggiornare. Gli estratti mantengono impaginazione, numerazione e
segnalibri del volume e si possono importare singolarmente in Goodnotes.
Le copie annotate vanno tenute separate dai file generati; una riscrittura
del capitolo può modificarne l'impaginazione e richiedere il trasferimento
delle annotazioni coinvolte.

Per ogni nuova sessione: confrontare la fonte pagina per pagina;
integrare il materiale nella sezione tematica appropriata; spiegare i
passaggi impliciti; compilare; controllare il PDF; aggiornare il registro
e la copertura. I numeri delle lezioni compaiono solo sotto i capitoli
di macroargomento. Pagine delle fonti, avanzamento e decisioni
editoriali restano fuori dal PDF. Un nuovo capitolo nasce quando cambia
il macroargomento, non quando cambia il numero della lezione.

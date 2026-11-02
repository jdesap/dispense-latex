# Appunti di analisi 1

Appunti di **Jude De Sa'Pinto** dal corso del **Prof. Federico Cacciafesta**.
Revisione editoriale integrale conclusa il 22 ottobre 2026; lezione 13 integrata
il 2 novembre: 83 pagine, nove capitoli. Resoconto e limiti della revisione editoriale in
`../lavoro/revisione-editoriale/RESOCONTO_FINALE.md`.
La lezione 9 completa il capitolo di topologia con interno, frontiera,
punti isolati, aderenza e accumulazione; dettagli e aggiunte redazionali in
`lavoro/LEZIONE_9_2026-10-23.md`.
Le lezioni 10–12 completano Topologia con estremi e accumulazione e avviano
il capitolo «Successioni e limiti»: proprietà definitive e frequenti, estrazioni,
limiti finiti e infiniti, unicità, permanenza del segno, confronti, algebra e
avvicinamento da sopra o da sotto. Mappa degli accorpamenti, correzioni e
aggiunte in `lavoro/LEZIONI_10_12_2026-10-28.md`; controlli in
`lavoro/VERIFICA_LEZIONI_10_12_2026-10-28.json`.
La lezione 13 completa il capitolo 8 con reciproci, quozienti, termine dominante,
limiti di polinomi e funzioni razionali e limite del valore assoluto. Apre inoltre
il capitolo 9 «Continuità», con definizione tramite successioni, ruolo del dominio
e operazioni fra funzioni continue. Accorpamenti, correzioni e letture alternative
di un esponente sono documentati in `lavoro/LEZIONE_13_2026-11-02.md`;
verifiche in `lavoro/VERIFICA_LEZIONE_13_2026-11-02.json`.
Le barre laterali, i numeretti blu delle note, il rientro delle prove e le
spaziature si regolano nel blocco **STILE MATEMATICO** di `preambolo.tex`,
I parametri e gli ultimi controlli sono descritti in
`../lavoro/revisione-editoriale/SESSIONE_15.md`.
Il documento è organizzato per argomenti. I numeri delle lezioni di
provenienza sono indicati soltanto sotto i titoli dei capitoli.
I riferimenti precisi alle pagine restano nei commenti TeX e nel registro
di copertura, esclusi dal PDF.

## File da aprire

- `main.tex`: documento principale, frontespizio e indice automatico.
- `preambolo.tex`: notazioni, ambienti, impaginazione e stili TikZ comuni.
- `capitoli/`: contenuto, suddiviso per argomento.
- `fonti/`: copie dei PDF originali e trascrizione della lezione 8 da cui si è partiti.
- `fonti/manifest.json`: inventario e impronte delle fonti.
- `lavoro/SESSIONI.md`: avanzamento, piano delle sessioni e controlli.
- `lavoro/COPERTURA.csv`: corrispondenza tra pagine delle fonti e contenuti.
- `lavoro/REVISIONE_MATEMATICA_2026-10-21.md`: correzioni, controlli
  matematici effettuati e limiti della revisione.
- `build/`: PDF compilato e file temporanei, separati dai sorgenti.

I file di `lavoro/` e il manifest delle fonti non sono inclusi nel PDF.
Il frontespizio mantiene il titolo, il nome del docente e il campo autore
richiesti. L'indice contiene capitoli e sezioni principali; le sottosezioni
restano nel testo e nei segnalibri, senza una divisione
in capitoli denominati «Lezione 1», «Lezione 2», ecc.

## Compilare e leggere

Aprire questa cartella in Visual Studio Code e lavorare su `main.tex`.
La configurazione per l'estensione **LaTeX Workshop** è già nella cartella
`.vscode/`; l'estensione, se non presente, è elencata fra le raccomandate.
Non è stata installata automaticamente.

Dal terminale, nella cartella del progetto:

```sh
latexmk main.tex
```

Il risultato è `build/main.pdf`. `latexmk` esegue anche i passaggi necessari
ad aggiornare indice e collegamenti. I commenti `TeX root` permettono di
compilare il documento principale anche mentre si modifica un capitolo.

La stessa compilazione, anche con Salva/Build in VS Code, esporta
automaticamente i nove capitoli in `build/capitoli/`, con nomi tematici.
I nuovi capitoli saranno riconosciuti senza configurazioni aggiuntive.
Gli estratti mantengono impaginazione, numeri di pagina e segnalibri
del volume; possono essere importati singolarmente in Goodnotes.
Le copie annotate restano separate dai file generati. Se viene riscritto
un capitolo, il PDF aggiornato non riallinea automaticamente le annotazioni
già fatte nella vecchia versione.

## Aggiornare gli appunti

1. Salvare il nuovo PDF in `fonti/` e aggiornarne l'inventario.
2. Integrare il contenuto nel capitolo dell'argomento corrispondente,
   conservando esempi, enunciati e osservazioni della fonte.
3. Aggiornare la provenienza soltanto sotto il macroargomento, per esempio
   `\fonti{Lezioni 6, 7 e 9}`. Annotare le pagine nei commenti del sorgente
   e in `lavoro/COPERTURA.csv`; non inserirle nel PDF.
4. Per un nuovo argomento, creare un file in `capitoli/` con la prima riga
   `% !TeX root = ../main.tex` e inserirlo con `\input` in `main.tex`.
5. Compilare, controllare formule e impaginazione, e aggiornare i registri
   separati in `lavoro/`. La numerazione e l'indice si aggiornano da soli.

I richiami narrativi alla lezione sono esclusi dal testo. Le convenzioni
che richiedono una precisazione sono spiegate in nota a piè di pagina.
Lo stato effettivo del lavoro e le verifiche sono in `lavoro/SESSIONI.md`.

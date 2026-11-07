# Dispense LaTeX

Raccolta di appunti organizzata per materia. Ogni sottocartella contiene
i sorgenti LaTeX, le fonti, la configurazione di compilazione e il PDF.

Indice di studio condiviso: [Dimostrazioni da studiare](DIMOSTRAZIONI_DA_STUDIARE.md), aggiornato insieme alle integrazioni delle dispense.

## Leggere gli appunti

- [Analisi 1 — PDF](<analisi 1/build/main.pdf>)
- [Geometria 1 — PDF](<geometria 1/build/main.pdf>)
- [Algebra 1 — PDF](<algebra 1/build/main.pdf>)

### Importare un capitolo in Goodnotes

Ogni compilazione aggiorna automaticamente anche i PDF in:

- `analisi 1/build/capitoli/`: un PDF per ciascuno degli otto capitoli attuali.
- `geometria 1/build/capitoli/`: attualmente `01-spazi-vettoriali.pdf`.
- `algebra 1/build/capitoli/`: cinque capitoli, dagli insiemi all'aritmetica degli interi.

Su iPad importare in Goodnotes soltanto il PDF del capitolo che si vuole
studiare. I file hanno nomi riconoscibili e mantengono le pagine e la
numerazione stampata del volume completo, con i segnalibri del capitolo.
Non includono frontespizio, indice generale o convenzioni preliminari:
questi restano nel volume completo. I nuovi capitoli vengono riconosciuti
automaticamente, senza aggiornare elenchi manuali.

La copia annotata in Goodnotes rimane separata dai PDF rigenerati. Se cambia
il testo di un capitolo già annotato, le annotazioni non si riallineano
automaticamente: conservare la copia annotata prima di importare una
nuova versione. L'esportazione per capitoli evita di reimportare anche
gli altri capitoli, ma non congela l'impaginazione del capitolo modificato.

Lo stesso workflow va usato per Algebra e per le nuove materie: il modello
di configurazione è in `modelli/nuova-materia/`, le regole in `AGENTS.md`.
La procedura usa Python e `pypdf`; su questo Mac riutilizza automaticamente
il runtime già presente di Codex. Su un altro computer occorrono Python
con `pypdf` e LaTeX; si può indicare l'interprete con `DISPENSE_PYTHON`.

## Modificare e compilare in VS Code

1. Aprire la cartella generale `dispense latex` con **File → Apri cartella**.
   Le impostazioni funzionano anche aprendo una singola materia.
2. Per modificare il testo, aprire il file `.tex` pertinente dentro
   `capitoli/`. `main.tex` riunisce i capitoli nella dispensa.
3. Salvare con **⌘S**: LaTeX Workshop compila automaticamente. Il pulsante
   **Build** esegue la stessa compilazione.
4. Per leggere il risultato, aprire `build/main.pdf` nella materia interessata.

Ogni materia conserva il proprio PDF e tutti i file di compilazione nella
propria cartella `build/`. I file temporanei sono nascosti nell'elenco di
VS Code; il PDF rimane visibile. I sorgenti da modificare sono i file `.tex`.
Non occorre cancellare i file temporanei a ogni compilazione: servono a
gestire indice, riferimenti e collegamenti con l'anteprima.

Se era già aperta un'anteprima del PDF creato fuori da `build/`,
chiuderla e aprire il PDF aggiornato dalla cartella `build/`.

## Aggiornare su GitHub

Usare questa cartella, `dispense latex`, come radice di un'unica repository
privata, comprendendo tutte le materie.

1. Modificare gli appunti e compilare il `main.tex` della materia interessata.
2. In GitHub Desktop controllare le modifiche, scrivere una breve descrizione
   e premere **Commit**, poi **Push origin**.
3. Sugli altri computer, usare **Fetch origin** e **Pull origin** per scaricare
   gli aggiornamenti. Per la sola lettura, aprire il PDF nella repository
   su GitHub con il proprio account.

Il PDF compilato in ciascuna cartella `build/` viene incluso nella repository;
i file temporanei di compilazione sono esclusi tramite `.gitignore`.
Le modifiche vengono rilevate da GitHub Desktop, ma sono caricate su GitHub
soltanto dopo il commit e il push.

# Dispense LaTeX

Raccolta di appunti organizzata per materia. Ogni sottocartella contiene
i sorgenti LaTeX, le fonti, la configurazione di compilazione e il PDF.

## Leggere gli appunti

- [Analisi 1 — PDF](<analisi 1/build/main.pdf>)
- [Geometria 1 — PDF](<geometria 1/build/main.pdf>)

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

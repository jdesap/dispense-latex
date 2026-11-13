# Workflow delle dispense

Queste regole valgono per tutte le materie della raccolta, inclusa Algebra.
Le richieste dell'autore e le convenzioni della singola dispensa prevalgono.

- Organizzare capitoli per macroargomenti, non per numero di lezione.
- Prima di integrare nuove fonti, confrontarle con i contenuti già presenti:
  individuare sovrapposizioni, integrazioni, correzioni e argomenti nuovi.
  Scegliere autonomamente la collocazione più coerente con il percorso
  didattico e aggiornare anche le sezioni precedenti quando necessario.
  Accorpare le ripetizioni conservando tutti i contenuti distinti e la
  provenienza; non aggiungere automaticamente ogni nuova lezione in coda.
- Conservare il PDF completo in `build/main.pdf` e generare automaticamente
  anche un PDF per ogni capitolo numerato in `build/capitoli/`.
- Usare la configurazione condivisa `strumenti/latexmk-comune.pl` tramite
  `.latexmkrc`. Per una nuova materia copiare
  `modelli/nuova-materia/.latexmkrc` nella cartella della materia.
- Conservare segnalibri PDF numerati per i capitoli (`hyperref` e `bookmark`):
  sono usati per riconoscere i confini, senza elenchi manuali da aggiornare.
- I PDF dei capitoli devono mantenere pagine, numerazione, formule e disegni
  del volume completo. Non dividere in file separati i semplici sottomoduli.
- Dopo ogni sessione compilare, verificare gli estratti e aggiornare i registri
  esterni al PDF. Non inserire avanzamento o registri nei PDF per capitolo.
- Gli estratti sono file rigenerati: le copie annotate dall'autore in
  Goodnotes restano separate. Non sovrascrivere copie annotate e non
  presentare l'esportazione per capitoli come riallineamento automatico
  delle annotazioni quando il testo di un capitolo cambia impaginazione.
- Non congelare errori matematici per mantenere l'impaginazione: segnalare
  quali capitoli cambiano quando sono necessarie correzioni.

- Negli esercizi separare sempre la consegna (`esercizio`) dalla soluzione
  (`svolgimento`): il riquadro rosa contiene soltanto dati e richieste.
  Conservare esempi illustrativi e dimostrazioni nei rispettivi ambienti.
  Evitare consegne isolate in fondo pagina prima dello svolgimento.

- A ogni nuovo caricamento verificare le sovrapposizioni con tutte le parti già scritte, scegliere la collocazione per macroargomento e integrare nel testo precedente i contenuti pertinenti. Evitare duplicazioni e registrare le scelte di accorpamento e le prove alternative utili.

- Mantenere aggiornato `DIMOSTRAZIONI_DA_STUDIARE.md` a ogni integrazione di fonti o revisione sostanziale delle dimostrazioni. Seguire il protocollo interno del file: priorità A/B/C motivate dall'idea richiesta, collegamenti ai sorgenti correnti, accorpamento dei metodi comuni e distinzione dei risultati assunti o rinviati. Conservare gli appunti personali dell'autore e non attribuirgli progressi di studio non dichiarati.

- Definire simboli, notazioni e oggetti prima del loro primo uso; riprendere brevemente le notazioni quando un richiamo lontano rende poco leggibile il testo o un estratto. Usare esempi e diagrammi quando chiariscono il processo, verificando sia la correttezza matematica sia il rendering effettivo dei TikZ, senza ambiguità di indici, direzioni o dimensioni.

- Nei risultati con più enunciati distinti (proposizioni, teoremi, lemmi e corollari), numerare gli enunciati e organizzare la dimostrazione con gli stessi numeri, rendendo immediata la corrispondenza. Per equivalenze usare i numeri dei punti nelle implicazioni; per prove comuni indicare esplicitamente i punti trattati insieme. Conservare integralmente ipotesi, passaggi, profondità e provenienza: la numerazione serve a separare le idee, non a riassumere le prove o frammentare un ragionamento unitario. Applicare la regola a tutte le dispense e verificare il rendering degli elenchi.

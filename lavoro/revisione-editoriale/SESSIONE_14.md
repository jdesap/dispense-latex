# Sessione 14 — Barra sul margine del testo, 22 ottobre 2026

Stato successivo: separazione esercizi/svolgimenti e impaginazione corrente in `SESSIONE_15.md` e `VERIFICA_STILE_15.json`.

## Modifica richiesta

La barra degli ambienti è ora allineata al margine sinistro del testo normale (`leftmargin=0pt`), con il contenuto spostato a destra di 9.6 pt, circa 3.4 mm: 1.6 pt di barra e 8 pt di spazio interno. Il margine destro resta quello ordinario; diminuisce di 9.6 pt la larghezza disponibile dentro gli ambienti. Parametri nei due `preambolo.tex`, blocco **STILE MATEMATICO** dalla riga 51, allineamento nello stile `barraDispensa` dalla riga 91.

Conservati colori, intestazioni nere, due punti negli esempi, numeretti delle note blu elettrico, rientro delle prove e formule guida. Aggiunta soltanto un'indicazione di spazio necessario prima della sezione sul binomio in Analisi, per evitare una pagina finale contenente il solo esempio. Nessuna modifica ai testi, alle formule o ai disegni: confronto delle impronte dei sorgenti riuscito, con la sola eccezione dei preamboli e dell'indicazione di impaginazione documentata.

## Verifiche e pagine

Compilazioni tramite configurazione condivisa e compilatore integrato riuscite per entrambe le materie. Nessun errore o avviso LaTeX, comprese segnalazioni di formule o righe fuori margine. Verificati tutti gli otto estratti: contenuti di pagina, testo, dimensioni, numerazione e collegamenti. Destinazioni delle note conservate. Controllata la panoramica di tutte le 84 pagine, più dettagli su barre, formule, note e raccordi; ricontrollate le due pagine finali del capitolo 3 dopo il correttivo.

Analisi passa da 54 a 55 pagine: il capitolo 3 passa da sei a sette pagine, con la sezione sul binomio interamente sull'ultima pagina. Gli estratti misurano ora 3, 3, 7, 11, 7, 14 e 6 pagine; cambia di una pagina la numerazione dei capitoli 4–7. Geometria resta di 29 pagine, con 26 per Spazi vettoriali. L'impaginazione interna degli ambienti può cambiare in tutti i capitoli. Copie annotate non modificate.

Audit correnti in `VERIFICA_STILE_14.json` e nei due file di verifica per materia; snapshot precedenti in `storico-prima-stile-14/`. Questa sessione riguarda l'impaginazione; restano i limiti matematici dichiarati in `RESOCONTO_FINALE.md`.

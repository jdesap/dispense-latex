# Sessione 13 — Barre laterali e note, 22 ottobre 2026

Allineamento successivamente aggiornato nella `SESSIONE_14.md`; questo resoconto conserva la versione precedente.

## Modifiche

- Sostituite le etichette colorate con una barra laterale estesa all'intero ambiente: blu/lilla per i risultati, verde per le definizioni, giallo oro per gli esempi, rosa acceso per gli esercizi e grigio per le osservazioni. Intestazioni nere, nessun fondo colorato. Conservati i corpi corsivi degli enunciati e quelli diritti degli altri ambienti.
- Barra di 1.6 pt, distanza interna di 8 pt, collocata nel margine: la larghezza del testo e delle formule resta invariata. I blocchi brevi fino a otto righe di base restano interi; quelli più lunghi possono proseguire sulla pagina successiva.
- Numeretti delle note blu elettrico, sia nel testo sia a piè di pagina: RGB `0,85,255` (`#0055FF`). Conservati numerazione, collegamenti e posizione ordinaria delle note, anche dentro gli ambienti con barra.
- Intestazioni degli esempi non numerati terminate da due punti: «Esempio:» oppure «Esempio (titolo):». Uniformato anche un titoletto manuale in Topologia.
- Conservati rientro di 4 mm delle prove, spazio di `0.42\baselineskip` fra i paragrafi e riquadri sottili delle formule guida. Spazio sopra e sotto i display delle prove regolato a 8 pt per evitare pagine finali quasi vuote.

Il riferimento personale ha ispirato soltanto la barra laterale. Aggiunti `mdframed` e `footnotehyper`; non importati altri stili, pacchetti o comandi del file personale. I parametri si trovano in entrambi i `preambolo.tex`, nel blocco **STILE MATEMATICO**, dalla riga 51: colori alle righe 53–59, spessore e distanza della barra subito sotto, quindi rientro e spazi delle prove. La punteggiatura è nello stile `esempioDispensa` dalla riga 113.

## Controlli

Compilazione condivisa e compilatore integrato riusciti in entrambe le materie, senza errori o avvisi LaTeX. Verificati tutti gli otto estratti: flussi di pagina, testo, dimensioni, numerazione e destinazioni dei collegamenti identici alle pagine corrispondenti del volume completo. Panorama visivo di tutte le 83 pagine e controlli di dettaglio su barre, prove, note e pagine finali.

Confronto delle impronte dei sorgenti con la versione precedente: tutti i capitoli e i documenti principali invariati, salvo la sola sostituzione «Esempio.» → «Esempio:» nel titoletto di Topologia. Conservati contenuti matematici, formule, disegni, label e contatori. Verificate direttamente le istruzioni colore dei PDF: dieci numeretti blu in Analisi e quattordici in Geometria, due per ognuna delle cinque e sette note; destinazioni `Hfootnote` conservate.

Analisi resta di 54 pagine e i sette estratti di 3, 3, 6, 11, 7, 14 e 6 pagine. Geometria resta di 29 pagine, con 26 per Spazi vettoriali. Può cambiare l'impaginazione interna di tutti i capitoli; nessuna copia annotata modificata.

Risultati in `VERIFICA_STILE_13.json` e nei due audit per materia. Fotografia dei precedenti audit in `storico-prima-stile-13/`. I limiti matematici di `RESOCONTO_FINALE.md` restano validi.

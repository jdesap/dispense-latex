# Sessione 12 — Stile visivo, 22 ottobre 2026

Stile successivamente aggiornato: parametri correnti e barre laterali in `SESSIONE_13.md` e `VERIFICA_STILE_13.json`. Il contenuto seguente documenta la versione storica della sessione 12.

Applicate alle due dispense le modifiche richieste dopo la revisione integrale.

## Resa e sorgenti

- Tutte le dimostrazioni sono rientrate di 4 mm sul lato sinistro, comprese formule ed elenchi. I paragrafi interni hanno uno spazio aggiuntivo di `0.42\baselineskip`; non è aggiunto alcun rientro di prima riga.
- Ambienti distinti per teorema, lemma, proposizione, corollario, assioma, definizione, esempio, esercizio e osservazione. Le etichette hanno un fondo leggero e testo colorato: blu/lilla per i risultati, verde per le definizioni, giallo oro per gli esempi, rosa acceso per gli esercizi, grigio per le osservazioni. Il corpo resta nero, con il corsivo degli enunciati conservato.
- Le formule che indicano inclusioni e versi sono scritte con `\passomath{...}`, in una cornice neutra di 0.35 pt. Rimossa la parola «Inclusione» dai titoli delle fasi; abbreviati anche altri titoletti ridondanti. I ragionamenti interni restano invariati.
- Uniformate alcune prove che erano semplici paragrafi: equivalenza per la limitatezza, esistenza/unicità del floor, periodo principale, derivazioni delle inverse iperboliche e doppia inclusione dell'esempio topologico. Gli svolgimenti degli esercizi lunghi usano lo stesso rientro, senza rientrare i titoli di sezione o sottosezione.
- L'esercizio finale di Analisi usa l'etichetta rosa. Eliminati i punti elenco ridondanti dove i riquadri delle due inclusioni identificano già le fasi.
- Corretto un cambio di pagina che lasciava isolata la sola frase conclusiva di De Morgan.

Nessun nuovo pacchetto. Gli stili sono contenuti direttamente nei due preamboli, così funzionano anche compilando una singola materia nell'editor integrato. Il sorgente dei capitoli conserva un paragrafo logico per riga.

## Dove modificare i parametri

In entrambe le materie, `preambolo.tex`, blocco **STILE MATEMATICO: parametri modificabili**, dalla riga 49:

| Parametro | Funzione | Valore attuale |
| --- | --- | --- |
| `coloreRisultati`, `coloreDefinizioni`, `coloreEsempi`, `coloreEsercizi`, `coloreOsservazioni` | Colore delle rispettive etichette | Valori RGB commentati nel sorgente |
| `coloreFasi` | Colore del bordo delle formule guida | Grigio neutro |
| `\tintaEtichette` | Percentuale di colore nel fondo | 9 |
| `\rientroDimostrazione` | Rientro sinistro dell'intera prova | 4 mm |
| `\spazioParagrafiProva` | Spazio fra paragrafi/fasi della prova | `0.42\baselineskip` |
| `\spessoreBoxFase` | Spessore delle cornici | 0.35 pt |
| `\margineBoxFase` | Spazio interno delle cornici | 2.2 pt |

Per una nuova fase matematica usare, per esempio, `\passomath{A\subseteq B}` oppure `\passomath{\Rightarrow}`, seguito dal ragionamento sulla stessa riga sorgente. Separare due paragrafi logici con una riga vuota; la spaziatura nella prova è gestita dal preambolo. Per mantenere lo stesso stile nelle due materie, riportare le variazioni dei parametri in entrambi i preamboli.

## Verifiche e impaginazione

Compilazioni condivise e compilatore integrato riusciti; nessun errore o avviso LaTeX. Verificati tutti gli otto estratti per flussi di pagina, testo, dimensioni, numerazione e destinazioni dei collegamenti. Ispezionata la panoramica dei due volumi e pagine rappresentative a risoluzione leggibile; ricontrollato il raccordo di De Morgan dopo la correzione.

Confronto con i sorgenti anteriori a questa sessione: conservati tutti i display matematici, gli ambienti di calcolo, i 47 TikZ, le note, le label e la sequenza degli enunciati numerati. Le formule in linea dei contenuti sono conservate; due frecce nei vecchi titoletti sulla monotonia sono state eliminate insieme ai titoletti abbreviati, mantenendo i medesimi ragionamenti. Nessun enunciato o calcolo matematico modificato.

Analisi resta di 54 pagine, con i sette estratti di 3, 3, 6, 11, 7, 14 e 6 pagine. Geometria passa da 28 a 29 pagine; Spazi vettoriali passa da 25 a 26. L'impaginazione interna cambia in tutti i capitoli per effetto dello stile: le copie annotate restano separate e non sono state modificate.

Risultati correnti in `VERIFICA_STILE_12.json` e nei due audit per materia. Le verifiche anteriori sono conservate in `storico-prima-stile-12/`; `RESOCONTO_FINALE.md` documenta la precedente revisione editoriale. I limiti matematici lì dichiarati restano gli stessi.

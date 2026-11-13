# Revisione totale di Geometria 1 — 12 novembre 2026

La revisione segue le inclusioni del `main.tex`: quattro capitoli e tutti i
24 moduli matematici attivi, oltre a convenzioni, rimandi e impaginazione.
Le bozze e gli archivi non inclusi non fanno parte del volume controllato.
Le lezioni 19–21 risultano già integrate e coperte pagina per pagina; questa
è la successiva revisione dell'intera dispensa, non soltanto delle aggiunte.

Sono state ricostruite tutte le dimostrazioni correnti, controllando ipotesi,
ambiente di ogni oggetto, entrambi i versi delle equivalenze, esistenza e
unicità, buona definizione, uso delle basi, terminazione dei procedimenti e
assenza di dipendenze circolari. Il controllo non costituisce una verifica
formale mediante un assistente di prova e non stabilisce richieste d'esame.

## Esito e interventi

I risultati e i calcoli della dispensa sono confermati dalla rilettura e dai
controlli esatti. Sono stati risolti passaggi procedurali ambigui e lacune di
spiegazione: prima colonna non nulla nel blocco di Gauss; uso delle colonne
pivot dopo aver disposto i generatori per colonne; prova della loro
indipendenza dal basso; inversa del prodotto delle operazioni elementari;
composizione delle operazioni nel registro in R5; fibra distinta dal valore
della funzione inversa; ipotesi finite, basi canoniche e alias introdotti
prima dell'uso; convenzione K^0 e inclusione del polinomio nullo.

L'esercizio sui tre generatori di R4 viene riconosciuto come ripresa con un
metodo diverso: si conserva il confronto fra relazione diretta e Gauss,
non si presenta la seconda richiesta come un contenuto indipendente.

## Moduli controllati

| Sorgente corrente | Esito della verifica di correttezza e chiarezza |
| --- | --- |
| [01a-spazi-e-sottospazi](../capitoli/01a-spazi-e-sottospazi.tex) | Assiomi, proprietà derivate, esempi, criterio di sottospazio, intersezione e controesempi: prove corrette; esplicitata la convenzione K^0. |
| [01b-sottospazio-generato](../capitoli/01b-sottospazio-generato.tex) | Costruzione per intersezione, minimalità, due inclusioni e somme vuote: corrette; esercizi verificati. |
| [01b-somme-di-sottospazi](../capitoli/01b-somme-di-sottospazi.tex) | Somma finita, unicità, criterio di intersezione nulla e criterio per più sottospazi: entrambi i versi ricostruiti; controesempio delle tre rette corretto. |
| [01c-indipendenza-basi-coordinate](../capitoli/01c-indipendenza-basi-coordinate.tex) | Famiglie e insiemi distinti, coefficiente non nullo, unicità e coordinate: corretti, comprese famiglie vuote e dipendenze con coefficienti nulli. |
| [01c-basi-e-dimensione](../capitoli/01c-basi-e-dimensione.tex) | Estrazione finita, polinomi di grado arbitrario, scambio con invariante di generazione e cardinalità delle basi: prove complete senza circolarità. |
| [01d-estrazione-e-basi-di-sottospazi](../capitoli/01d-estrazione-e-basi-di-sottospazi.tex) | Eliminazione con coefficienti espliciti, completamento e terminazione; tre esercizi in R4 corretti. |
| [01e-equazioni-cartesiane](../capitoli/01e-equazioni-cartesiane.tex) | Necessità e sufficienza dell’eliminazione dei parametri entrambe presenti e verificate. |
| [01f-prodotti](../capitoli/01f-prodotti.tex) | Assiomi per componenti e base del prodotto con generazione/indipendenza: corretti. |
| [01g-quozienti](../capitoli/01g-quozienti.tex) | Equivalenza, uguaglianza delle classi, indipendenza dai rappresentanti, assiomi e dimensione: prove corrette; finitezza della base del sottospazio giustificata prima di usarla. |
| [01h-grassmann-complementi](../capitoli/01h-grassmann-complementi.tex) | Base adattata all’intersezione, indipendenza, dimensioni, esistenza e non unicità dei complementari: corretti. |
| [01i-costruzioni-in-r5](../capitoli/01i-costruzioni-in-r5.tex) | Relazione, matrici del registro, cartesiane nei due versi, complementare e intersezioni: corretti; esplicitata la composizione R2←R1−3R2 in due operazioni reversibili. |
| [01j-equazioni-di-polinomi](../capitoli/01j-equazioni-di-polinomi.tex) | Equazioni, base del nucleo, cambio di coefficienti e inverse: corretti; incluso esplicitamente il polinomio nullo. |
| [02a-gauss](../capitoli/02a-gauss.tex) | Operazioni equivalenti e basi per righe corrette; precisata la scelta della prima colonna non nulla del blocco. Distinti i generatori per righe dalle colonne della trasposta da selezionare; riconosciuta la ripresa dell’esercizio precedente. |
| [02b-operazioni](../capitoli/02b-operazioni.tex) | Dimensioni dei prodotti, associatività per somme finite, distributività, identità e trasposizione: indici e prove corretti; entrambe le moltiplicazioni numeriche verificate. |
| [02d-matrici-elementari](../capitoli/02d-matrici-elementari.tex) | Effetto del prodotto a sinistra, inversi delle tre operazioni, registro BA=A′ e calcolo inversa: corretti. Aggiunta la formula dell’inversa del prodotto per giustificare la reversibilità accumulata. |
| [02c-rango-sistemi](../capitoli/02c-rango-sistemi.tex) | Invarianza di tutte le relazioni fra colonne, due disuguaglianze, sistemi e parametri: corretti. Esplicitata l’indipendenza delle colonne pivot risalendo dalle ultime righe, senza presupporre determinanti. Riduzione del parametro verificata simbolicamente. |
| [03a-linearita-nucleo-immagine](../capitoli/03a-linearita-nucleo-immagine.tex) | Linearità, eccezione F2, inversa, nucleo/immagine, coordinate e rango–nullità: corretti; i casi di base vuota sono coerenti con K^0. Nessuna generalizzazione indebita da n generatori a dimensione n. |
| [03e-invertibilita](../capitoli/03e-invertibilita.tex) | Inverse unilatere, dominio vuoto, scelta e criterio finito: corretti; due esempi e tutte le composizioni verificati. |
| [03b-proiezioni-simmetrie](../capitoli/03b-proiezioni-simmetrie.tex) | Buona definizione dalla somma diretta, nuclei/immagini e identità: corrette. Anticipato l’alias sigma prima dell’uso e spiegata la caratteristica 2 nella nota. |
| [03c-matrici-associate](../capitoli/03c-matrici-associate.tex) | Immagini di una base, formula coordinate, esercizio, fibre, rango, Hom e composizione: corretti. Esplicitate ipotesi finite e distinta la fibra f^{-1}({w}) dal valore della funzione inversa. |
| [03d-cambi-di-base](../capitoli/03d-cambi-di-base.tex) | Verso delle matrici dell’identità e formula QAP^{-1}: corretto; aggiunto richiamo alla dimensione finita; esempio verificato anche con una coppia ulteriore di basi. |
| [04a-duale-biduale](../capitoli/04a-duale-biduale.tex) | Base duale e delta, righe/colonne, bilinearità, buona definizione di alpha, iniettività e suriettività finite: corrette. Basi canoniche esplicite nell’esempio. Catena infinita mantenuta come assunta, non usata come prova. |
| [04b-annullatori](../capitoli/04b-annullatori.tex) | Ambienti V/V*, sottospazi, dimensione e doppio annullatore tramite separazione: corretti; nessun prodotto scalare implicito e nessuna identificazione illegittima di V con V**. |
| [04c-trasposta](../capitoli/04c-trasposta.tex) | Verso contravariato, composizione, nucleo e inclusione dell’immagine più dimensioni, matrice A^T nelle basi duali: corretti. Esplicitate le basi nell’esempio rettangolare. |

## Metodi e risultati assunti

Le prove portanti restano scambio, Grassmann, quoziente, uguaglianza dei
ranghi e rango–nullità. Le prove su duale, biduale e annullatori si accorpano
per valutazione su basi e completamento, quelle sulla trasposta per
inclusione e confronto delle dimensioni. Le precisazioni aggiunte non
introducono un nuovo metodo da memorizzare. L'indice comune delle
`DIMOSTRAZIONI_DA_STUDIARE.md` è stato aggiornato senza attribuire progressi
personali all'autore.

Resta assunto, come dichiarato nella fonte, il risultato sulle dimensioni
cardinali del duale in dimensione infinita. La scelta generale di un
antecedente per ogni fibra di una suriezione arbitraria è distinta dalle
costruzioni finite. Le prove finite non dipendono dalla catena infinita.
I risultati su simmetrie sono su R, con la precisazione su caratteristica 2
in nota; la parametrizzazione dei sistemi su un campo finito è distinta
dall'affermazione di infinità delle soluzioni reali.

## Calcoli e verifica visiva

Lo script `verifiche/revisione_totale_2026_11_12.py` ricontrolla i calcoli
dei capitoli precedenti e richiama i controlli delle lezioni 19–21:
coefficienti, relazioni, basi, cartesiane nei due versi, complementari,
intersezioni, matrici intermedie, inverse e prodotti, cambiamenti di basi,
duale in basi non canoniche, annullatori e trasposta. La riduzione del
parametro è stata verificata sui coefficienti polinomiali, per ogni valore
del parametro, oltre ai casi numerici. I conteggi dei ranghi sono eseguiti
con frazioni esatte. Le prove astratte sono verificate con la rilettura,
non dedotte dall'esito di alcuni esempi.

Controllati il significato matematico di tutti i 17 TikZ e il rendering
nell'intero volume. Le figure sono coerenti con somme, scomposizioni,
parallelismi, versi delle applicazioni e dimensioni delle matrici. Tutte
le pagine sono state ispezionate nelle tavole di rendering; i diagrammi e
i passaggi più densi erano stati verificati anche nelle viste ingrandite.

Ricompilazione con configurazione condivisa, nessun errore o avviso;
verifica finale di tutti gli estratti rispetto al volume, comprese
numerazione e pagine. La versione resta di 58 pagine (3 preliminari e
capitoli di 26, 10, 12 e 7 pagine). Cambia la disposizione interna di alcune
pagine di tutti e quattro i capitoli. Le copie annotate non sono state
modificate; i file in build/capitoli sono estratti rigenerati.

## Evidenze

- `INVENTARIO_REVISIONE_TOTALE_2026-11-12.json`: ogni modulo, hash e conteggi.
- `CONTROLLI_REVISIONE_TOTALE_2026-11-12.json`: controlli aritmetici completi.
- `CONTROLLI_LEZIONI_19-21_2026-11-12.json`: verifica dei nuovi esercizi.
- `VERIFICA_REVISIONE_TOTALE_2026-11-12.json`: build finale, estratti e hash.
- `COPERTURA.csv` e `fonti/manifest.json`: copertura e integrità delle fonti.

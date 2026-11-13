# Capitolo Funzione di Eulero e gruppi — 5 novembre 2026

Richiesta dell'autore: organizzare le aggiunte già ricavate dalle lezioni affinché phi ricada in un nuovo capitolo «Funzione di Eulero e gruppi». Precisazione esplicita: non iniziare autonomamente la teoria dei gruppi e non aggiungere contenuti estranei alle lezioni.

## Confronto e decisione prima della ricollocazione

La sezione finale7.6 conteneva già trasporto delle unità, definizione di phi, valori/cautele, conteggio sulle potenze prime, moltiplicatività per coprimi, formula dalla fattorizzazione ed esempio600: unitàN21–N25, recuperoD03. Dipende dai morfismi/CRT/unità prodotto del capitolo7; si può separare senza anticipare alcun prerequisito. Il resto degli anelli e morfismi resta nel7. Nessuna nuova unità matematica o fonte da introdurre; le prove non cambiano.

## Modifica

Spostata integralmente la sezione finale in `capitoli/08-eulero-e-gruppi.tex`, capitolo numerato8 con provenienza A–L16. Nessuna aggiunta di definizioni, esempi o teoremi sui gruppi; il titolo accoglierà quel materiale quando arriverà dalle lezioni. Il capitolo7 conserva la provenienza15–16. Aggiunta inclusione nel volume, senza cambiare il preambolo o il sistema automatico di esportazione. Aggiornata collocazione per unità e per pagina nei registri. Snapshot: `storico-prima-capitolo-eulero-2026-11-05/`.

## Verifica di conservazione richiesta

Confrontare esattamente il corpo spostato con la precedente sezione7.6; conservare gli altri capitoli e tutti gli enunciati/prove/esempi. Compilare il volume ed esportare anche il capitolo8; verificare rendering, numerazione, indice e rimandi dal nuovo8 al7. Aggiornare lo stato corrente distinguendo questa riorganizzazione dalla precedente integrazione.

## Esito

- Confronto esatto del sorgente: la precedente sezione7.6 è identica al corpo del nuovo8, inclusi esempi, quattro dimostrazioni e formule. Nessuna nuova teoria dei gruppi o unità matematica; restano126 unità. Restante corpo7 conservato esattamente; sorgenti1–6, preambolo e manifest delle fonti invariati.
- Volume58 pagine,4 preliminari+54 testo. Capitolo7:9 pagine stampate44–52; nuovo8:2 pagine53–54. I risultati di Eulero sono rinumerati8.1–8.5, con riferimenti risolti; nessun altro contenuto rimosso.
- Compilazione condivisa senza avvisi/overfull/underfull e compilazione integrata riuscite sul sorgente finale. Otto estratti verificati integralmente sulle54 pagine per testo, flussi, formato, numerazione, pixel e collegamenti. Verificato anche il rimando dal capitolo8 al corollario7.12. Tutti32 originali ancora byte-identici.
- Confronto grafico con lo snapshot: le52 pagine dei capitoli1–7 (PDF5–56) hanno pixel e numerazione identici. Ispezionati l’indice, il raccordo finale7 e tutte le pagine8: nessun problema visivo aperto.
- Risultati: `VERIFICA_CAPITOLO_EULERO_E_GRUPPI_2026-11-05.json`, `../../strumenti/VERIFICA_ESPORTAZIONE_2026-11-05.json`, stato corrente `VERIFICA_FINALE.json`. Verifica della conservazione riproducibile con `verifiche/verifica_ricollocazione_eulero.py`, dopo la verifica PDF condivisa.
- Prossima lezioneA–L17. Nessun materiale ricevuto pendente; nessuna copia annotata modificata, nessun commit/push/pubblicazione.


**Aggiornamento11 novembre2026:** questo è il registro storico della sola ricollocazione. Le lezioni17–18 sono ora integrate, inclusa la teoria dei gruppi effettivamente presente nelle nuove fonti. Stato corrente in `LEZIONI_17-18_2026-11-11.md` e `VERIFICA_FINALE.json`.

# Revisione editoriale e tipografica delle dispense matematiche

Agisci come un editor scientifico specializzato in dispense universitarie di matematica. Revisiona direttamente i sorgenti LaTeX delle dispense presenti nel progetto.

L'obiettivo non è riscrivere il materiale da zero né renderlo il più breve possibile, ma trasformarlo in **dispense rigorose, dense, ben strutturate e facili da studiare, consultare e modificare**.

Adotta uno stile da appunti universitari di alta qualità, non da manuale divulgativo, articolo narrativo o testo scolastico.

## 1. Principio editoriale fondamentale

Massimizza il rapporto tra contenuto matematico, chiarezza e quantità di testo.

- Elimina ridondanze, preamboli inutili e spiegazioni di ovvietà che non svolgono alcuna funzione.
- Mantieni e, se necessario, sviluppa i passaggi matematicamente o concettualmente importanti.
- Non confondere sintesi con omissione: una dimostrazione può essere lunga quando il ragionamento lo richiede.
- Non dare a ogni dettaglio lo stesso peso espositivo.
- Evita formulazioni artificiose, enfatiche o eccessivamente didascaliche.

**Criterio:** esplicita ciò che serve a comprendere il ragionamento, non tutto ciò che sarebbe possibile dire.

## 2. Struttura delle parti esplicative

Intervieni anche sulle sezioni non dimostrative: introduzioni, osservazioni, commenti alle definizioni, proprietà ed esempi.

- Privilegia una presentazione schematica e visivamente organizzata.
- Quando un paragrafo contiene informazioni concettualmente distinte, separale in punti, paragrafi brevi o blocchi opportunamente titolati.
- Utilizza titoletti in grassetto per identificare idee o proprietà rilevanti.
- Evita lunghe enumerazioni in prosa, specialmente quelle in cui molti risultati sono separati da punti e virgola.
- Raggruppa le informazioni strettamente collegate anziché creare un bullet per ogni singola frase.
- Non trasformare ogni spiegazione in un elenco: mantieni paragrafi discorsivi quando il ragionamento è unitario e una presentazione continua risulta più naturale.

Le dispense devono poter essere consultate rapidamente, identificando a colpo d'occhio definizioni, risultati, proprietà e osservazioni.

## 3. Definizioni, proprietà ed esempi

Dopo una definizione, distingui chiaramente:

- Il contenuto della definizione.
- Le osservazioni immediate sulla struttura definita.
- Le proprietà che seguono dalla definizione e che eventualmente richiedono dimostrazione.
- Gli esempi e i controesempi significativi.

Non presentare una proprietà derivata come se fosse un assioma della definizione.

Per gli esempi, privilegia una presentazione compatta e matematica: identifica l'oggetto, specificane le caratteristiche pertinenti e indica perché è interessante nel contesto.

Non scrivere lunghi paragrafi narrativi per elencare esempi di campi, gruppi, spazi vettoriali o altre strutture.

## 4. Dimostrazioni

Le dimostrazioni devono essere rigorose, leggibili ed eleganti, senza eccessiva frammentazione.

**Struttura logica:**

- Quando una dimostrazione procede per doppia inclusione, distingui esplicitamente le due inclusioni mediante punti titolati in grassetto, per esempio **\(A\subseteq B\)** e **\(B\subseteq A\)**.
- Quando un'equivalenza viene dimostrata nelle due direzioni, usa analogamente **\((\Rightarrow)\)** e **\((\Leftarrow)\)**.
- Applica lo stesso principio alle prove di esistenza e unicità o ad altre fasi logicamente distinte.
- Concludi esplicitamente il ragionamento quando ciò rende chiara la chiusura della dimostrazione.

**Sviluppo del ragionamento:**

- Se una fase contiene diverse idee che contribuiscono allo stesso obiettivo, sviluppale coerentemente al suo interno, senza necessariamente trasformarle in punti distinti.
- Se una dimostrazione consiste in un unico ragionamento continuo, non imporre suddivisioni artificiali.
- Non spezzare le prove in una sequenza di micro-passaggi banali.
- Non eliminare passaggi fondamentali solo per ottenere una dimostrazione più breve.
- Quando un'idea è sottile, una costruzione non è immediata o un'implicazione richiede attenzione, dedica lo spazio necessario a chiarirla.

Privilegia la naturalezza matematica rispetto all'applicazione meccanica di un modello espositivo.

## 5. Grassetti e gerarchia visiva

Usa il grassetto in modo coerente e selettivo per:

- Titoletti di osservazioni, proprietà e fasi dimostrative.
- Elementi concettuali particolarmente importanti.
- Distinzioni che facilitano la consultazione.

Non evidenziare indiscriminatamente parole o frasi. Il grassetto deve trasmettere gerarchia, non decorazione.

Mantieni uno stile tipografico omogeneo fra le diverse lezioni.

## 6. Sorgente LaTeX

Rendi il codice sorgente facile da leggere e modificare manualmente.

- Elimina i ritorni a capo arbitrari all'interno dei periodi e dei paragrafi.
- Preferisci un paragrafo logico per riga sorgente, anche quando la riga è lunga.
- Separa chiaramente paragrafi, ambienti matematici e strutture LaTeX.
- Usa gli ambienti appropriati per elenchi, teoremi, definizioni e dimostrazioni.
- Mantieni un'indentazione coerente.
- Preserva macro, comandi personalizzati, label, riferimenti e struttura del progetto, salvo modifiche effettivamente necessarie.
- Non introdurre nuovi pacchetti o macro se quelli già disponibili sono sufficienti.
- Non alterare accidentalmente il comportamento di commenti, spazi o comandi sensibili ai ritorni a capo.

La pulizia del sorgente non deve compromettere la compilazione o il risultato tipografico.

## 7. Correttezza matematica

Preserva il contenuto matematico e il livello di rigore.

- Non modificare silenziosamente enunciati, ipotesi o conclusioni.
- Non sostituire una dimostrazione corretta con una più breve ma incompleta.
- Se individui imprecisioni o errori matematici, correggili quando la correzione è inequivocabile e segnalali nel resoconto finale.
- Se la correzione non è sicura, non inventarla: segnala il problema.
- Non introdurre nuovo materiale matematico estraneo agli argomenti già trattati, salvo brevi chiarimenti indispensabili.

## 8. Procedura di lavoro

1. Esamina la struttura dei sorgenti e individua le convenzioni esistenti.
2. Revisiona integralmente le parti discorsive e le dimostrazioni secondo i criteri precedenti.
3. Uniforma lo stile tipografico e ripulisci il sorgente LaTeX.
4. Verifica che le modifiche non abbiano introdotto errori matematici o tecnici.
5. Se l'ambiente lo consente, compila il documento e controlla che il PDF sia corretto.

Lavora direttamente sui file del progetto, preservandone l'organizzazione.

Al termine, produci un resoconto sintetico con le modifiche editoriali principali, le eventuali correzioni matematiche e i punti che richiedono ancora una revisione umana.

**Risultato atteso:** dispense che sembrino scritte e curate da uno studente universitario matematicamente competente, con attenzione alla precisione, all'eleganza delle dimostrazioni e all'efficienza espositiva. Non devono sembrare un testo generato automaticamente che cerca di spiegare ogni dettaglio con uguale enfasi.
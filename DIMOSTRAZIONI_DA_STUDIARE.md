# Dimostrazioni da studiare

Ultimo aggiornamento: 13 novembre 2026. Riferimento: sorgenti attualmente inclusi nei tre `main.tex`, non versioni storiche o bozze.

Questa è una selezione ragionata per distribuire il tempo di studio, non un elenco ufficiale delle richieste d'esame. Le priorità riguardano la **dimostrazione**: anche per una prova di livello C bisogna conoscere enunciato, ipotesi e significato. La difficoltà di ricostruzione è personale: le valutazioni iniziali si possono correggere dopo una prova a libro chiuso.

## Come usare le priorità

- **A — Studiare la prova.** C'è una costruzione, una stima o una concatenazione che non conviene improvvisare. Saperla riprodurre a libro chiuso, capendo perché ogni passaggio serve.
- **B — Imparare l'idea.** Ricordare il passaggio decisivo e ricostruire il resto; fare almeno una verifica a libro chiuso. Una prova corta può comunque meritare B se insegna un metodo riutilizzabile.
- **C — Ricostruire dalle definizioni.** Nessuna memorizzazione separata: verificare una volta di saperla scrivere correttamente. Se ci si blocca, promuoverla a B.
- **Assunta/rinviata.** Nessuna prova completa nel testo corrente: studiare l'enunciato e sapere che cosa viene assunto. Non confondere questa voce con una prova facile.

Nelle tabelle, argomenti strettamente dipendenti sono raggruppati per evitare di studiare lo stesso meccanismo più volte. I collegamenti puntano ai sorgenti, così restano utili quando cambia l'impaginazione.

## Analisi 1

### A — Da studiare davvero

| Dimostrazione | Che cosa devi portarti a casa | Dove |
| --- | --- | --- |
| Esistenza della radice n-esima | Costruire il candidato come supremo; controllare la variazione della potenza; escludere entrambi i casi di disuguaglianza. L'unicità è invece immediata dalla monotonia. | [Radici](<analisi 1/capitoli/06a-potenze-e-radici.tex>) |
| Densità dei razionali nei reali | Usare Archimede per scegliere una scala abbastanza fine e poi un intero che collochi una frazione fra i due reali. | [Archimede e densità](<analisi 1/capitoli/04c-archimede-ed-esempi.tex>) |
| Algebra dei limiti: prodotto e reciproco | Nel prodotto, spezzare la differenza e controllare il fattore variabile tramite limitatezza; nel reciproco, tenere il denominatore lontano da zero. Studiare bene i limiti finiti, poi capire gli adattamenti ai casi infiniti. | [Algebra dei limiti](<analisi 1/capitoli/08c-confronti-e-algebra.tex>) |
| Criterio del rapporto e passaggio dal rapporto alla radice | Scegliere costanti sopra/sotto il limite del rapporto e iterare fino a ottenere confronti geometrici. Nel passaggio alla radice distinguere limite positivo, nullo e infinito. | [Rapporti e radici](<analisi 1/capitoli/10b-geometriche-rapporti-radici.tex>) |
| Esistenza del numero e | Riscrivere con Newton per la monotonia; maggiorare con i reciproci dei fattoriali e una geometrica; usare il supremo per la convergenza. | [Numero di Nepero](<analisi 1/capitoli/10c-nepero-esponenziale-logaritmo.tex>) |
| Limite sin(x)/x | Capire il confronto geometrico delle aree che dà sin(t) < t < tan(t), poi applicare i carabinieri. Il limite del coseno è un breve seguito algebrico. | [Limiti trigonometrici](<analisi 1/capitoli/10a-limiti-trigonometrici.tex>) |
| Limite (exp(x)-1)/x | Ricavare exp(t) ≥ 1+t da Bernoulli e dalla rappresentazione assunta dell'esponenziale; usarla anche in -t per il secondo vincolo. Il limite logaritmico segue con un cambio di variabile. | [Limiti esponenziale e logaritmico](<analisi 1/capitoli/10c-nepero-esponenziale-logaritmo.tex>) |

### B — Ricordare il passaggio decisivo

| Dimostrazione | Idea da ricordare | Dove |
| --- | --- | --- |
| Principio di induzione dal minimo | Se esistesse un controesempio, prenderne il minimo e usare il predecessore. | [Induzione](<analisi 1/capitoli/03-numeri-naturali-e-combinatoria.tex>) |
| Bernoulli; binomio di Newton | Per Bernoulli, moltiplicare l'ipotesi induttiva per 1+x ≥ 0; per Newton, raggruppare i coefficienti usando Pascal. Non imparare a memoria gli sviluppi. | [Induzione e combinatoria](<analisi 1/capitoli/03-numeri-naturali-e-combinatoria.tex>) |
| Irrazionalità di √2 | Frazione ridotta ai minimi termini e parità di numeratore e denominatore. Breve, ma il trucco va conosciuto. | [Completezza](<analisi 1/capitoli/04a-reali-e-completezza.tex>) |
| Esistenza del supremo da Dedekind | Applicare Dedekind all'insieme e all'insieme dei suoi maggioranti. Infimo tramite cambio di segno. | [Supremo e infimo](<analisi 1/capitoli/04b-intervalli-ed-estremi.tex>) |
| Principio di Archimede | Supporre N limitato, prendere il supremo e contraddirlo con una traslazione di 1. | [Archimede](<analisi 1/capitoli/04c-archimede-ed-esempi.tex>) |
| Intersezioni finite di aperti | Minimo dei finitissimi raggi positivi. Sapere perché il ragionamento non si estende alle intersezioni infinite. I chiusi seguono per complemento. | [Topologia](<analisi 1/capitoli/07-topologia.tex>) |
| Estremo non raggiunto ⇒ accumulazione | Usare la caratterizzazione del supremo/infimo per trovare punti distinti arbitrariamente vicini. | [Estremi e accumulazione](<analisi 1/capitoli/07c-estremi-e-accumulazione.tex>) |
| Estrazione da una proprietà frequente | Scegliere ricorsivamente indici strettamente crescenti che soddisfano la proprietà. | [Sottosuccessioni](<analisi 1/capitoli/08a-successioni-e-sottosuccessioni.tex>) |
| Unicità del limite; convergente ⇒ limitata; permanenza del segno | Intorni disgiunti; coda controllata più parte iniziale finita; intorno che non attraversa zero. Sono brevi ma fondamentali come modelli di prova. | [Proprietà dei limiti](<analisi 1/capitoli/08b-limiti-e-proprieta.tex>) |
| Carabinieri; somma di limiti; limitata × infinitesima | Soglia comune e stime con epsilon; per la somma dividere il margine, per il prodotto assorbire la costante della limitatezza. | [Confronti e algebra](<analisi 1/capitoli/08c-confronti-e-algebra.tex>) |
| Geometriche e radice n-esima di una costante | Bernoulli; reciproco per basi sotto 1; sottosuccessioni pari/dispari per basi negative. | [Geometriche](<analisi 1/capitoli/10b-geometriche-rapporti-radici.tex>) |

### C — Non memorizzare separatamente

- De Morgan, contrapposizione, proprietà elementari di insiemi e funzioni.
- Stretta monotonia ⇒ iniettività; identità iperboliche ottenute espandendo le definizioni.
- Caratterizzazione epsilon di supremo e infimo, una volta capita la negazione di «maggiorante/minorante migliore».
- Limite delle sottosuccessioni; continuità della composta nella formulazione per successioni.
- Limiti di polinomi e confronto dei gradi: raccogliere la potenza dominante.
- Limite (1-cos(x))/x² dal limite del seno; limite logaritmico da quello esponenziale.
- Gerarchia fra n^n, n!, q^n e n^k: applicare il criterio del rapporto ai quozienti. È il criterio a richiedere studio, non tre nuove prove autonome.

### Risultati assunti o rinviati

- Proprietà generali delle potenze reali e continuità delle funzioni elementari nei termini dichiarati nella dispensa.
- Rappresentazioni generali dell'esponenziale mediante limiti e somme, con la relativa proprietà moltiplicativa: la prova per e da sola non le dimostra.
- Confronto fra potenze e logaritmi: dimostrazione rinviata.

## Algebra 1

### A — Da studiare davvero

| Dimostrazione | Che cosa devi portarti a casa | Dove |
| --- | --- | --- |
| Caratterizzazioni degli insiemi infiniti | Estrarre una successione di elementi distinti e costruire lo spostamento che omette il primo elemento lasciando fisso il resto. | [Infiniti](<algebra 1/capitoli/04-cardinalita.tex>) |
| Numerabilità di N² e unione numerabile di numerabili | Una costruzione concreta per enumerare le coppie; poi due indici, uno per scegliere l'insieme e uno per l'elemento. La numerabilità di Q si ricava da questo; le potenze finite di un insieme numerabile infinito si trasportano mediante una biezione con N. Per un’unione, un membro infinito dà anche la disuguaglianza opposta. | [Numerabilità](<algebra 1/capitoli/04-cardinalita.tex>) |
| Teorema di Cantor | Costruire D = {x : x non appartiene a f(x)} e mostrare che non è un valore di f. Corta, ma l'idea diagonale non viene dalla sola definizione. | [Cantor](<algebra 1/capitoli/04-cardinalita.tex>) |
| Algoritmo di Euclide e identità di Bézout | Distinguere terminazione, conservazione dei divisori comuni e risalita/costruzione dei coefficienti. Sono parti dello stesso percorso. | [Euclide e Bézout](<algebra 1/capitoli/05-interi.tex>) |
| Teorema fondamentale dell'aritmetica | Esistenza per induzione; unicità usando il lemma sui primi che dividono un prodotto. Non confondere i due ragionamenti. | [Fattorizzazione](<algebra 1/capitoli/05-interi.tex>) |
| Tutte le soluzioni di una congruenza lineare e loro numero | Sottrarre una soluzione particolare, dividere per il MCD e usare coprimalità; contare le classi distinte modulo il modulo originario. | [Congruenze](<algebra 1/capitoli/06-aritmetica-modulare.tex>) |
| Teorema cinese del resto | Costruire i fattori M/m_i e i loro inversi locali, sommarli con i resti richiesti; separare verifica e unicità. | [Teorema cinese](<algebra 1/capitoli/06-aritmetica-modulare.tex>) |
| Teorema di Lagrange | Identificare la partizione in classi laterali e costruire la biezione di ciascun blocco con H. Solo allora si possono sommare le cardinalità. | [Classi laterali](<algebra 1/capitoli/08g-diedrali-laterali.tex>) |
| Congruenze e sottogruppi normali | Ritrovare H come classe del neutro, ricostruire i laterali e usare entrambi i lati per provare la compatibilità del prodotto. Per passare dall’inclusione all’uguaglianza applicare l’ipotesi a g inverso. | [Normalità e quozienti](<algebra 1/capitoli/08h-quozienti.tex>) |

### B — Ricordare il passaggio decisivo

| Dimostrazione | Idea da ricordare | Dove |
| --- | --- | --- |
| Equivalenze e partizioni | Le classi che si incontrano coincidono; nel verso inverso definire la relazione tramite l'appartenenza allo stesso blocco. | [Relazioni](<algebra 1/capitoli/02-relazioni.tex>) |
| Inverse a sinistra/destra | Costruire la preimmagine; per l'inversa sinistra assegnare anche i punti fuori dall'immagine; per la destra sapere dove interviene la scelta. | [Inverse](<algebra 1/capitoli/03-funzioni.tex>) |
| Divisione euclidea | Induzione sul dividendo non negativo; adattamento dei segni mantenendo il resto non negativo; unicità dalla differenza dei resti, di valore assoluto minore del divisore. | [Interi](<algebra 1/capitoli/05-interi.tex>) |
| Infinità dei primi | Prodotto dei primi supposti tutti, più 1; il nuovo numero ha un divisore primo, non necessariamente è primo. | [Primi](<algebra 1/capitoli/05-interi.tex>) |
| Minimo positivo e divisione: combinazioni, sottogruppi di Z e dei ciclici | Scegliere il minimo positivo nell'insieme pertinente e dividere per esso: il resto appartiene ancora all'insieme e, se positivo, contraddice il minimo. Per i ciclici si minimizza l'esponente; nel caso finito dividere anche l'ordine N per r per ottenere r\|N. La corrispondenza divisori/sottogruppi e l'unicità seguono da questo stesso metodo, non sono prove da memorizzare separatamente. | [Combinazioni](<algebra 1/capitoli/05-interi.tex>), [sottogruppi di Z](<algebra 1/capitoli/08b-sottogruppi.tex>), [sottogruppi ciclici](<algebra 1/capitoli/08e-gruppi-ciclici.tex>) |
| Lemma di Euclide e primi sui prodotti | Moltiplicare un'identità di Bézout. Breve, ma è il ponte verso l'unicità della fattorizzazione. | [Lemma di Euclide](<algebra 1/capitoli/05-interi.tex>) |
| Unità e divisori dello zero modulo m | Inverso da Bézout; annullatore non nullo m/MCD(a,m). Ricordare la costruzione, inclusa la convenzione sullo zero. | [Unità modulari](<algebra 1/capitoli/06-aritmetica-modulare.tex>) |
| Esistenza di soluzioni di ax ≡ b modulo m | Necessità per divisibilità; sufficienza moltiplicando Bézout per b/d. | [Congruenze lineari](<algebra 1/capitoli/06-aritmetica-modulare.tex>) |
| Teorema cinese come isomorfismo | Mappa sulle classi ben definita; esistenza e unicità della soluzione modulo il prodotto danno suriettività e iniettività. Non richiede ancora la nozione di nucleo. | [Morfismi](<algebra 1/capitoli/07-anelli.tex>) |
| Moltiplicatività di phi per moduli coprimi | Il cinese induce una biezione fra le unità; nel prodotto le unità si scelgono coordinata per coordinata. | [Funzione di Eulero](<algebra 1/capitoli/08-eulero-e-gruppi.tex>) |
| Costruzione del gruppo affine e formule di composizione/inversa | Applicare prima la funzione a destra e risolvere y=ax+b. Il criterio di commutazione e i coniugati si ricavano da queste stesse formule: un solo metodo, senza memorizzare conti distinti. | [Affinità](<algebra 1/capitoli/08a-gruppi.tex>), [coniugati](<algebra 1/capitoli/08c-centralizzanti.tex>) |
| Criterio di sottogruppo con hk⁻¹ | Il non vuoto permette di ottenere 1=hh⁻¹, poi gli inversi e infine i prodotti. Ricordare come si recuperano le tre condizioni; intersezioni, sottogruppi generati e stabilizzatori riusano questo criterio. | [Sottogruppi](<algebra 1/capitoli/08b-sottogruppi.tex>) |
| Unione di due sottogruppi | Se nessuno contiene l'altro, scegliere un elemento in ciascuno dei due scarti; il loro prodotto, in qualunque fattore cada, produce una contraddizione usando un inverso. Merita B per questa scelta, non per la lunghezza della prova. | [Unioni](<algebra 1/capitoli/08b-sottogruppi.tex>) |
| Centralizzanti e calcolo dei centri | Per C_G(X) applicare il criterio hk⁻¹ e verificare che il coniugato di ogni x resti x; il centro è il caso X=G. Negli esempi bastano elementi opportuni: traslazione e omotetia in Aff(R), oppure il punto fisso unico di uno scambio in S3. Ricordare la scelta che forza i parametri, non tutte le moltiplicazioni. | [Centralizzanti e centri](<algebra 1/capitoli/08c-centralizzanti.tex>) |
| Ordine e classificazione dei gruppi ciclici | Usare n↦g^n. Nel caso aperiodico una collisione forza a−b=0; nel caso periodico dividere per il minimo m con g^m=1, ottenere g^k=1 se e solo se m divide k e distinguere i resti. Provare così cardinalità e buona definizione dell'isomorfismo sulle classi, senza supporle a vicenda. Il passaggio sulle classi riusa il metodo del cinese come isomorfismo. | [Ordine e due modelli](<algebra 1/capitoli/08e-gruppi-ciclici.tex>) |
| Ordine di [a] modulo N e delle potenze; generatori | Da N\|ka dividere per d=MCD(a,N), poi usare coprimalità per ottenere N/d\|k. Il minimo k dà l'ordine; il criterio dei generatori e il loro numero phi(N) sono conseguenze, non nuove prove. L'esercizio U16/U17 applica questi criteri con calcoli di potenze, senza Lagrange o teorema di Eulero. | [Ordine e generatori](<algebra 1/capitoli/08e-gruppi-ciclici.tex>) |
| Cicli disgiunti e coniugio | Il primo ritorno costruisce il ciclo e il complemento è stabile. Per il coniugio scegliere una corrispondenza fra cicli ugualmente lunghi e il punto di partenza di ognuno. L’ordine si ricava dai tempi di ritorno simultanei. | [Calcolo con i cicli](<algebra 1/capitoli/08f-cicli-permutazioni.tex>) |
| Segnatura | Seguendo una coppia di punti attraverso due permutazioni, ciascuna inversione cambia il verso. Il conteggio modulo 2 dà la moltiplicatività, da cui segue la parità di ogni scrittura in trasposizioni. | [Segnatura](<algebra 1/capitoli/08f-cicli-permutazioni.tex>) |
| Simmetrie e centro del diedrale | Fissare l’immagine di un vertice e il verso. Per il centro basta commutare con rotazione e riflessione, e quindi risolvere la divisibilità di 2i per n. | [Gruppi diedrali](<algebra 1/capitoli/08g-diedrali-laterali.tex>) |
| Assenza di sottogruppi di ordine 6 in A₄ | Un sottogruppo di indice due sarebbe normale. Nel quoziente di ordine due tutti gli otto 3-cicli dovrebbero finire nel neutro. | [Esercizio su A₄](<algebra 1/capitoli/08h-quozienti.tex>) |

### C — Non memorizzare separatamente

- Identità fra insiemi, distributività, De Morgan e associatività della differenza simmetrica: ricostruire mediante appartenenze/operazioni; la lunghezza di uno sviluppo non è un'idea nuova da imparare.
- Proprietà elementari di composizione, immagini e controimmagini: applicare le definizioni con attenzione; conoscere quali uguaglianze diventano soltanto inclusioni.
- Unicità dell'inversa, zero assorbente, regole dei segni negli anelli, campo ⇒ dominio.
- Buona definizione delle operazioni su classi: applicare il criterio di compatibilità, senza memorizzare ogni espansione.
- Formule per MCD e mcm dalla fattorizzazione; riduzione di coefficienti e modulo nelle congruenze.
- Unità di prodotti di anelli e trasporto delle unità tramite isomorfismi.
- phi(p^k): togliere dai p^k resti i p^(k-1) multipli di p; formula generale di phi usando moltiplicatività e fattorizzazione.
- Unicità di neutro e inverso nei gruppi, cancellazione ai due lati e inverso del prodotto: usare gli assiomi rispettando l'ordine dei fattori. [Gruppi](<algebra 1/capitoli/08a-gruppi.tex>).
- Leggi delle potenze e sottogruppo ciclico: concatenare/cancellare le potenze, includendo zero ed esponenti negativi; per (a^m)^n usare induzione su n non negativo e poi inversi; chiusura e minimalità del generato si ricostruiscono da queste leggi. [Potenze](<algebra 1/capitoli/08a-gruppi.tex>), [ciclici](<algebra 1/capitoli/08b-sottogruppi.tex>).
- Gruppi delle unità e simmetrico: verificare chiusura, neutro e inversi; per S_n riusare le biezioni e contare le scelte senza ripetizioni. I calcoli di prodotti e coniugati di permutazioni sono applicazioni delle definizioni, non nuove prove da memorizzare.
- Intersezioni, sottogruppo generato come intersezione e permutazioni che fissano punti: applicare il criterio già classificato B. Omotetie, traslazioni e coefficienti razionali si controllano con le formule del gruppo affine; il generato di omotetie e traslazioni è tutto il gruppo perché f_(a,b)=f_(1,b)∘f_(a,0).
- Generato di X mediante parole: concatenazione, inversa in ordine rovesciato e minimalità; includere la parola vuota. Combinazioni intere nel caso abeliano, join=MCD e intersezione=mcm in Z riusano risultati già studiati. [Generati e Z](<algebra 1/capitoli/08b-sottogruppi.tex>).
- Morfismi di gruppi: neutro da cancellazione, inversi applicando f al prodotto, potenze per induzione; inversa di un isomorfismo usando le preimmagini. Pendenza, restrizioni a omotetie/traslazioni e inclusioni S_m→S_n sono verifiche della legge, da ricostruire. [Morfismi](<algebra 1/capitoli/08d-morfismi-gruppi.tex>), [permutazioni](<algebra 1/capitoli/08f-cicli-permutazioni.tex>).
- Reticoli dei sottogruppi contenenti 12Z e di Z/12Z, liste di generatori e decomposizioni concrete in cicli: applicazioni dei criteri o della definizione. Saper distinguere gli oggetti dei due reticoli; nessuna nuova prova generale da memorizzare per i disegni.
- Ordine degli elementi, ciclicità in ordine primo, Eulero e Fermat si ricostruiscono da Lagrange scegliendo rispettivamente il sottogruppo generato o il gruppo delle unità. Per Fermat separare il caso in cui il primo divide la base. [Corollari di Lagrange](<algebra 1/capitoli/08g-diedrali-laterali.tex>).
- Per un sottogruppo di indice due, la classe laterale di un elemento esterno è tutto il complemento da entrambi i lati. Per la proiezione canonica, prodotto, suriettività e fibra del neutro si leggono dalla definizione. [Quozienti](<algebra 1/capitoli/08h-quozienti.tex>).

### Risultati assunti o parzialmente dimostrati

- Cantor–Schröder–Bernstein e confronto totale delle cardinalità: assunti.
- Aritmetica generale delle cardinalità infinite: assunta.
- Cardinalità di R uguale a quella di P(N): il verso mediante tagli razionali è svolto; l'iniezione delle successioni binarie in R è assunta. Capire la mappa x ↦ {q razionale : q < x}; non cercare una prova completa nel testo attuale.
- L’esempio M–Z dell’anello End_K(V) e del gruppo degli automorfismi lineari è rinviato (D04): spazi vettoriali e linearità non sono introdotti nel flusso attuale di Algebra. Non è una prova già inclusa da studiare.
- Per l'esempio dell'esponenziale sono assunte legge della somma, stretta monotonia e immagine uguale ai reali positivi. [Esponenziale](<algebra 1/capitoli/08d-morfismi-gruppi.tex>).

## Geometria 1

### A — Da studiare davvero

| Dimostrazione | Che cosa devi portarti a casa | Dove |
| --- | --- | --- |
| Teorema dello scambio | Sostituire progressivamente generatori con vettori indipendenti senza perdere la generazione; capire perché ogni volta c'è un coefficiente utilizzabile. | [Scambio](<geometria 1/capitoli/01c-basi-e-dimensione.tex>) |
| Formula di Grassmann | Base dell'intersezione, due completamenti e prova dell'indipendenza della famiglia unita: è questo l'ostacolo, non il conteggio finale. | [Grassmann](<geometria 1/capitoli/01h-grassmann-complementi.tex>) |
| Base e dimensione del quoziente | Completare una base del sottospazio; le classi dei vettori aggiunti generano e sono indipendenti. | [Quoziente](<geometria 1/capitoli/01g-quozienti.tex>) |
| Uguaglianza fra rango per righe e per colonne | Le operazioni sulle righe conservano tutte le relazioni fra colonne; eliminando le righe nulle, lo spazio delle colonne accorciate ha ancora dimensione c ed è un sottospazio di K^r, dunque c ≤ r. Applicare poi l’argomento alla trasposta. | [Rango](<geometria 1/capitoli/02c-rango-sistemi.tex>) |
| Teorema della dimensione: rango + nullità | Completare una base del nucleo e dimostrare che le immagini dei vettori aggiunti formano una base dell'immagine. | [Teorema della dimensione](<geometria 1/capitoli/03a-linearita-nucleo-immagine.tex>) |

### B — Ricordare il passaggio decisivo

| Dimostrazione | Idea da ricordare | Dove |
| --- | --- | --- |
| Estrazione e completamento di basi | Eliminare vettori dipendenti oppure aggiungere vettori fuori dallo span; lo scambio assicura il limite e la terminazione. Uguaglianza delle cardinalità delle basi con le due disuguaglianze. | [Basi e dimensione](<geometria 1/capitoli/01c-basi-e-dimensione.tex>), [completamento](<geometria 1/capitoli/01d-estrazione-e-basi-di-sottospazi.tex>) |
| Somma diretta ⇔ unicità della scomposizione | Sottrarre due scomposizioni per produrre un vettore nell'intersezione. | [Somme dirette](<geometria 1/capitoli/01b-somme-di-sottospazi.tex>) |
| Esistenza di un complementare | Completare una base e prendere lo span dei vettori aggiunti; controllare che l'intersezione sia nulla. | [Complementari](<geometria 1/capitoli/01h-grassmann-complementi.tex>) |
| Rouché–Capelli e parametri liberi | Compatibilità significa b nello spazio delle colonne; per i parametri contare pivot e variabili libere. Dopo avere capito il rango, la prova è breve. | [Rouché–Capelli](<geometria 1/capitoli/02c-rango-sistemi.tex>) |
| Formula di cambiamento di basi | Scrivere le quattro relazioni fra vecchie/nuove coordinate, poi calcolare l'uscita in due modi. Ricostruire il verso delle matrici, non ricordare una formula senza convenzioni. | [Cambi di base](<geometria 1/capitoli/03d-cambi-di-base.tex>) |
| Matrice della composta = prodotto delle matrici | Applicare in sequenza le due formule delle coordinate; questo spiega anche l'ordine del prodotto. | [Matrici associate](<geometria 1/capitoli/03c-matrici-associate.tex>) |
| Matrici elementari e registro delle operazioni di Gauss | Scegliere a ogni passo la prima colonna non nulla del blocco rimasto; leggere il prodotto a sinistra come combinazione delle righe; accumulare E_s⋯E_1 e applicarlo a (A affiancata a I) per ottenere (BA affiancata a B). Ricordare il metodo, non i numeri dei due esercizi. | [Matrici elementari e inverse](<geometria 1/capitoli/02d-matrici-elementari.tex>) |
| Base duale e isomorfismo canonico con il biduale | Valutare sui vettori di base per leggere i coefficienti; poi valutare alpha_v sui funzionali della base duale per riconoscere v. La suriettività del biduale usa la dimensione finita, non una scelta nella definizione di alpha. Un unico metodo di valutazione, senza memorizzare due sviluppi separati. | [Duale e biduale](<geometria 1/capitoli/04a-duale-biduale.tex>) |
| Dimensione dell'annullatore e doppio annullatore | Completare una base di U e azzerare i primi coefficienti duali. Per il doppio annullatore, separare v esterno a U scegliendo il funzionale duale che vale 1 su v e 0 sulla base di U. È la stessa costruzione con una condizione in più. | [Annullatori](<geometria 1/capitoli/04b-annullatori.tex>) |
| Nucleo e immagine della trasposta | Il nucleo è la condizione «annulla l'immagine»; per l'immagine provare l'inclusione e poi confrontare le dimensioni tramite rango–nullità e dimensione degli annullatori. Non confondere i due ambienti V* e W*. | [Trasposta](<geometria 1/capitoli/04c-trasposta.tex>) |

### C — Non memorizzare separatamente

- Criteri di sottospazio, intersezione di sottospazi, descrizione dello span mediante combinazioni lineari.
- Criterio di dipendenza e unicità delle coordinate: isolare un coefficiente non nullo oppure sottrarre due rappresentazioni.
- Base/dimensione del prodotto: separare le coordinate.
- Buona definizione di somma e prodotto per scalare nel quoziente: la differenza dei rappresentanti resta nel sottospazio.
- Nucleo e immagine sono sottospazi; iniettività ⇔ nucleo nullo: applicare linearità, soprattutto a v-w.
- Soluzioni non omogenee = soluzione particolare + nucleo: sottrarre una soluzione particolare. Distinguere la fibra f⁻¹({w}), insieme di antecedenti, dal valore dell’eventuale funzione inversa; [fibre e nucleo](<geometria 1/capitoli/03c-matrici-associate.tex>).
- Linearità dell'inversa e della composta; un'applicazione lineare è determinata dalle immagini di una base.
- Isomorfismo delle coordinate: leggere i coefficienti nella base ordinata e ricostruire il vettore con la combinazione lineare; verificare che le due mappe siano inverse. Resta C perché la prova si ricostruisce dall'esistenza e unicità delle coordinate, senza un nuovo artificio. Distinguere una base di n elementi da n generatori eventualmente ridondanti: in quest'ultimo caso la ricostruzione da K^n è suriettiva ma può non essere iniettiva. [Prova esplicitata e controesempio](<geometria 1/capitoli/03a-linearita-nucleo-immagine.tex>), [unicità delle coordinate](<geometria 1/capitoli/01c-indipendenza-basi-coordinate.tex>).
- Proprietà di proiezioni e simmetrie: scrivere il vettore nella somma diretta e applicare la definizione.
- Unicità dell'inversa di una matrice e regole elementari di trasposizione. L'associatività del prodotto si può ricostruire con gli indici: non memorizzare lo sviluppo delle somme.

- Criterio di invertibilità a dimensioni uguali, rango massimo e sufficienza di un'inversa unilatera quadrata: conseguenze del teorema della dimensione già studiato; la distinzione fra inverse di funzioni generali riprende il metodo classificato B in Algebra. [Invertibilità](<geometria 1/capitoli/03e-invertibilita.tex>).
- Inverse delle tre matrici elementari: invertire l'operazione sulla riga; nessuna nuova prova da memorizzare oltre al metodo di Gauss. [Matrici elementari](<geometria 1/capitoli/02d-matrici-elementari.tex>).
- Bilinearità della valutazione, buona definizione e linearità di alpha e di f*: verifiche punto per punto. La matrice di f* nelle basi duali è A^T: valutare f*(w_i*) su v_j e leggere a_ij; è il metodo della base duale già classificato B, con scambio degli indici. [Duale e biduale](<geometria 1/capitoli/04a-duale-biduale.tex>), [trasposta](<geometria 1/capitoli/04c-trasposta.tex>).
- Annullatori sottospazi e isomorfismo da un prodotto scalare reale scelto: applicare le definizioni; per il secondo, nucleo nullo dalla positività e suriettività dalla dimensione finita. [Annullatori](<geometria 1/capitoli/04b-annullatori.tex>), [nota sul prodotto scalare](<geometria 1/capitoli/04a-duale-biduale.tex>).

### Risultati assunti o rinviati

- In dimensione infinita, la catena stretta dim V < dim V* < dim V** per il duale algebrico, con le usuali ipotesi di scelta, è soltanto citata: non è dimostrata e non viene usata per le prove finite. L'isomorfismo canonico con il biduale in dimensione finita è invece dimostrato e classificato B. [Ambito e osservazione](<geometria 1/capitoli/04a-duale-biduale.tex>).
- La scelta di un antecedente in ogni fibra di una suriezione arbitraria richiede l'assioma della scelta, segnalato in nota; i diagrammi finiti e i loro esempi di inverse unilatere sono verificati esplicitamente. [Inverse da un lato](<geometria 1/capitoli/03e-invertibilita.tex>).

## Protocollo di aggiornamento

1. A ogni integrazione di fonti o revisione sostanziale delle prove, confrontare questo indice con **tutto il testo corrente pertinente**, seguendo le inclusioni dei `main.tex`; escludere archivi e bozze non inclusi.
2. Classificare ogni nuova prova o famiglia omogenea in A/B/C, indicando per A e B il passaggio decisivo e il sorgente. Una prova lunga per soli calcoli non diventa automaticamente A; una breve costruzione ingegnosa può esserlo.
3. Accorpare le conseguenze dello stesso metodo, distinguendo il risultato portante dai corollari. Segnalare le alternative utili senza imporre di memorizzare duplicati.
4. Verificare lo stato effettivo: prova completa, prova con ingredienti assunti, solo enunciato o rinvio. Rimuovere un risultato dai rinvii quando viene effettivamente dimostrato e riclassificarlo.
5. Aggiornare data, collegamenti e priorità coinvolte. Conservare eventuali annotazioni personali e giudizi dell'autore; non segnare mai una prova come già studiata senza sua indicazione.
6. Registrare qui sotto l'aggiornamento con una riga sintetica. Il file resta esterno ai PDF; modificarlo da solo non richiede ricompilazione LaTeX. Se si modificano i sorgenti, applicare le verifiche ordinarie del protocollo delle dispense.

## Registro

- 2026-11-05 — Prima selezione ragionata sui sorgenti correnti di Analisi 1, Algebra 1 e Geometria 1; distinte prove da studiare, idee da ricordare, verifiche ricostruibili e risultati assunti/rinviati. Nessuno stato personale di apprendimento assegnato.

- 2026-11-10 — Geometria: esplicitate le due mappe inverse nell’isomorfismo delle coordinate e la distinzione fra generatori e base; confermata priorità C per ricostruzione da esistenza e unicità. Riesaminati i metodi comuni in sistemi, prodotto e applicazioni: priorità A/B invariate, nessun nuovo risultato assunto o rinviato e nessun progresso personale assegnato.

- 2026-11-11 — Algebra17–18: accorpate riprese di phi e metodi comuni; aggiunte priorità B per costruzione affine, criterio dei sottogruppi, unione e centralizzanti/centri, con conseguenze C. Collegamenti ai sottomoduli correnti, rimosso il rinvio generale ai gruppi ora sviluppati; distinto l’esempio End_K(V) rinviato e i teoremi di Eulero/Lagrange non ancora sviluppati. Preservate le annotazioni e le altre materie; nessuno stato personale di studio assegnato.

- 2026-11-12 — Geometria19–21: integrate matrici elementari, criterio di invertibilità, duale/biduale, annullatori e trasposta. Nuove famiglie B motivate dal registro delle operazioni, valutazione sui vettori di base, separazione e inclusione più dimensioni; conseguenze C accorpate. Distinti i risultati infiniti e la scelta generale assunti. Collegamenti ai sorgenti correnti, note personali e altre materie conservate; nessuno stato di studio assegnato.

- 2026-11-12 — Revisione totale di Geometria: riletti tutti i 24 moduli dei quattro capitoli; precisati Gauss, selezione dei generatori tramite colonne della trasposta, indipendenza delle colonne pivot, inversa del prodotto, fibre, ipotesi finite e notazioni. A/B/C confermate perché non cambia l’idea richiesta; aggiornati i richiami ai metodi comuni, preservati risultati assunti e appunti personali. Nessuno stato di studio attribuito.


## Revisione editoriale del 13 novembre 2026

Enunciati distinti e relative prove numerati in tutte e tre le dispense, con corrispondenza esplicita dei punti. Nessuna prova abbreviata, nessun cambiamento alle priorità A/B/C o ai risultati assunti/rinviati. I collegamenti ai sorgenti restano validi; la paginazione dei PDF è cambiata. Le annotazioni personali e i progressi dichiarati sono conservati. [Resoconto e controlli](strumenti/NUMERAZIONE_ENUNCIATI_2026-11-13.md).

- 2026-11-13 — Algebra19–20: metodo minimo positivo/divisione accorpato con sottogruppi di Z e ciclici; B per classificazione tramite potenze e ordine/MCD, conseguenze e verifiche dirette inC. Assunte esplicitamente le proprietà dell’esponenziale; decomposizione generale in cicli solo enunciata, non conteggiata come prova. Collegamenti correnti, nessuna modifica alle altre materie o attribuzione di progressi personali.

- 2026-11-13 — Revisione totale di Algebra: completate le conseguenze sulla numerabilità inA, precisato il criterio MCD prima dell’esistenza generale, conservati entrambi i metodi Euclide/minimo positivo. InC esplicitata la prova della potenza di potenza usata nei ciclici; gruppo banale definito senza estendere phi(1). Le nuove precisazioni riusano metodi già classificati, senza nuove priorità o progressi personali; altre materie e appunti preservati.

- 2026-11-22 — Algebra 21–24. Inserite le prove di Lagrange e dei criteri di normalità, le idee di cicli, coniugio, segnatura e diedrali e le applicazioni di Eulero e Fermat. Il precedente enunciato sulla decomposizione in cicli è ora accompagnato da una prova per primo ritorno. D04 rimane rinviato.

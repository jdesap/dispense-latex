# Appunti di geometria 1

Appunti di **Jude De Sa'Pinto** dal corso del **Prof. Francesco Bottacin**.
Il volume è organizzato per argomenti. I numeri delle lezioni compaiono
soltanto sotto i quattro macroargomenti; le pagine delle fonti e lo stato
del lavoro sono registrati fuori dal PDF.

## Struttura

- `main.tex`: frontespizio, convenzioni, indice e ordine dei capitoli.
- `preambolo.tex`: ambienti, notazioni, impaginazione e stili TikZ.
- `capitoli/`: quattro moduli tematici aggiornabili separatamente.
- `fonti/`: copie dei sei PDF consegnati e manifest con le impronte SHA-256.
- `lavoro/SESSIONI.md`: attività, verifiche e decisioni editoriali.
- `lavoro/COPERTURA.csv`: corrispondenza fra ogni pagina delle fonti e il testo.
- `build/main.pdf`: volume compilato; gli altri file di `build/` sono temporanei.

Sono integrate le lezioni **5, 6, 8, 9, 10, 11 e 12**. Le lezioni non
consegnate e la parte sui numeri complessi potranno essere inserite nei
moduli pertinenti quando saranno disponibili, senza cambiare l'impianto.

## Compilazione

Aprire questa cartella in Visual Studio Code e lavorare su `main.tex`.
La configurazione di LaTeX Workshop è in `.vscode/`. Dal terminale:

```sh
latexmk main.tex
```

Il risultato è `build/main.pdf`. `latexmk` aggiorna indice e segnalibri.
Ogni capitolo indica `main.tex` come radice per la compilazione.

## Aggiornare gli appunti

1. Salvare il nuovo PDF in `fonti/` e aggiornarne il manifest.
2. Integrare definizioni, proprietà, prove, esempi ed esercizi nel modulo
   tematico appropriato o creare un nuovo file in `capitoli/`.
3. Indicare i numeri delle lezioni solo con `\fonti{...}` subito sotto il
   titolo del capitolo. Conservare i riferimenti alle pagine nei commenti
   TeX e in `lavoro/COPERTURA.csv`.
4. Scrivere in prosa autonoma, sciogliere i passaggi impliciti e usare
   note a piè di pagina per precisazioni necessarie.
5. Compilare, controllare l'impaginazione e annotare la sessione in
   `lavoro/SESSIONI.md`.

I file di `lavoro/` e il manifest non sono inclusi nel documento.

- Add competition contribute to fitness

- Use random.Generator to generate random variables (as suggested in numpy documentation)

- Far notare che si è risparmiato lo spazio del vettore (matrice) v e che si è usato un 
algoritmo ricorsivo per calcolare la reazione avvenuta in Gillespie

- Spiegare bene tutti tipi di fitness landscape

- Cambiare `source/` with `src/` and `fixed_pop-static_fit/` with `fixed_pop-stat_fit/`

- Idea generale:
  - usa dati 'di prova' (in cui si usano sia exact che hybrid algorithm) per controllare 
  che siano in accordo con paper
  - esplora con diversi fitness landscape e anche con variable population usando solo
  hybrid algorithm
  - (eventualmente) fai studio dell'efficienza usando rirunnando 'prova'

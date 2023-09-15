- Add competition contribute to fitness

- Use random.Generator to generate random variables (as suggested in numpy documentation)

- Far notare che si è risparmiato lo spazio del vettore (matrice) v e che si è usato un 
algoritmo ricorsivo per calcolare la reazione avvenuta in Gillespie

- Spiegare bene tutti tipi di fitness landscape

- Idea generale:
  - usa dati 'di prova' (in cui si usano sia exact che hybrid algorithm) per controllare 
  che siano in accordo con paper
  - esplora con diversi fitness landscape e anche con variable population usando solo
  hybrid algorithm
  - (eventualmente) fai studio dell'efficienza usando rirunnando 'prova'

- Pensare se aggiungere un tempo massimo alla simulazione (in particolare per fitness landscape
che non 'spingono' verso destra

- Fondere .sh e \_clust.sh

- Riadattare analisi.py per i csv con quattro colonne

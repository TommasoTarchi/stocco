- Use random.Generator to generate random variables (as suggested in numpy documentation)

- Far notare che si è risparmiato lo spazio del vettore (matrice) v e che si è usato un 
algoritmo ricorsivo per calcolare la reazione avvenuta in Gillespie

- Spiegare bene tutti tipi di fitness landscape

- Idea generale:
  - comparazione di risultati ed efficienza di algoritmi esatto e ibrido usando fixed population 
  e static fitness; comparazione di risultati ed efficienza tra ibrido con fixed e dynamic 
  population (con N\_tilde costante); comparazione di efficienza di spaziale con diversi valori di 
  resolution (caso base: fixed e dynamic population)
  - comparazione di risultati (sia tempo che stato finale) usando algo ibrido con fixed population 
  e tutti tipi di fitness (magari usare boxplot per tempi); per lo stato finale mostrare per quali 
  valori e in che percentuale si ha speciazione
  - plot di N e N\_tilde per mostrare che N\_tilde controlla N
  - comportamento di algoritmo spaziale (magari creare schema del mondo con colore per indicare
  genotipo medio in ogni area): al variare della resolution e confronto tra caso con neighbours e 
  senza

- Rirunnare tutti job che coinvolgono algoritmo con dynamic population

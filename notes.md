- Use random.Generator to generate random variables (as suggested in numpy documentation)

- Far notare che si è risparmiato lo spazio del vettore (matrice) v e che si è usato un 
algoritmo ricorsivo per calcolare la reazione avvenuta in Gillespie

- Spiegare bene tutti tipi di fitness landscape

- Idea generale:
  - comparazione di risultati ed efficienza di algoritmi esatto e ibrido usando fixed population 
  e static fitness; comparazione tra ibrido con fixed population e con dynamic population (con 
  N\_tilde costante)
  - comparazione di risultati (sia tempo che stato finale) usando algo ibrido con fixed population 
  e tutti tipi di fitness; per lo stato finale mostrare per quali valori e in che percentuale si 
  ha speciazione
  - plot di N e N\_tilde per mostrare che N\_tilde controlla N

- Controllare che effettivamente la population size si comporti come descritto nel paper nei
modelli con popolazione variabile

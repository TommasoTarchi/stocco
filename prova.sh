#!/bin/bash



datafile=$(pwd)/flat.csv


echo "# THIS IS A FIRST TRIAL RUN" > "$datafile"


echo "exact_simulation,hybrid_simulation" >> "$datafile"
for index in {1..3}
do
    python3 ../source/fixed_population.py --N_c 1000 --output "simulation_time" --datafile "$datafile"
    echo -n "," >> "$datafile"
    python3 ../source/fixed_population.py --N_c 10 --output "simulation_time" --datafile "$datafile"
    echo >> "$datafile"
done 

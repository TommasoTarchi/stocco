#!/bin/bash



datafile=$(pwd)/trial.csv


echo "# THIS IS A FIRST TRIAL RUN" > "$datafile"


echo "exact_simulation,hybrid_simulation" >> "$datafile"
for index in {1..10}
do
    python3 ../source/fixed_population.py --N_c 1000 --m 20 --fitness "static_inc" --output "simulation_time" --datafile "$datafile"
    echo -n "," >> "$datafile"
    python3 ../source/fixed_population.py --m 20 --fitness "static_inc" --output "simulation_time" --datafile "$datafile"
    echo >> "$datafile"
done 

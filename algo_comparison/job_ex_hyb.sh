#!/bin/bash


### script to run several simulations with both exact and hybrid algorithms on Orfeo, cluster 
### hosted at Area Science Park (Trieste, Italy)


#SBATCH --no-requeue
#SBATCH --job-name="algo_comparison"
#SBATCH --partition=EPYC
#SBATCH -N 1
#SBATCH -n 10
#SBATCH --time=02:00:00


module load architecture/AMD
module load conda/23.3.1

conda activate stoch_modelling

export OMP_NUM_THREADS=10


datafile=$(pwd)/data_ex_hyb.csv

echo "# data for simulation time and efficiency comparision between" > "$datafile"
echo "# exact and hybrid algorithms" >> "$datafile"
echo "#" >> "$datafile"
echo "# fitness landscape: static increasing" >> "$datafile"
echo "# number of genotipic classes: 20" >> "$datafile"
echo "# population size: 1000" >> "$datafile"
echo "# " >> "$datafile"

echo "exact_simulation,exact_elapsed,hybrid_simulation,hybrid_elapsed" >> "$datafile"
for index in {1..10}
do
    python3 ../src/fixed_population.py --N_c 1000 --m 20 --fitness "static_inc" --output "time" --datafile "$datafile"
    echo -n "," >> "$datafile"
    python3 ../src/fixed_population.py --m 20 --fitness "static_inc" --output "time" --datafile "$datafile"
    echo >> "$datafile"
done 


module purge

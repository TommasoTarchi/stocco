#!/bin/bash


### script to run several simulations with hybrid algorithms and different fitness
### landscapes on Orfeo, cluster hosted at Area Science Park (Trieste, Italy)
###
### number of genotipic classes = 4
###
### complement to job.sh in this directory


#SBATCH --no-requeue
#SBATCH --job-name="fitness_comparison"
#SBATCH --partition=EPYC
#SBATCH -N 1
#SBATCH -n 10
#SBATCH --time=02:00:00


module load architecture/AMD
module load conda/23.3.1

conda activate stoch_modelling

export OMP_NUM_THREADS=10


datafile=$(pwd)/data_dyndec.csv

echo "#" > "$datafile"
echo "# number of genotipic classes: 4" >> "$datafile"
echo "# population size: 10000" >> "$datafile"
echo "# " >> "$datafile"

echo "dynamic_dec_simul,dynamic_dec_elpsd,dynamic_dec_state" >> "$datafile"
for index in {1..20}
do
    python3 ../src/fixed_population.py --m 4 --N 10000 --fitness "dynamic_dec" --output "final_state" --datafile "$datafile"
    echo >> "$datafile"
done 


module purge

#!/bin/bash
#SBATCH --no-requeue
#SBATCH --job-name="algo_comparison"
#SBATCH --partition=EPYC
#SBATCH -N 1
#SBATCH -n 10
#SBATCH --time=02:00:00


module load architecture/Intel
module load conda/23.3.1

conda activate stoch_modelling

export OMP_NUM_THREADS=10


datafile=$(pwd)/data.csv

echo >> "$datafile"
for index in {1..10}
do
    python3 ../src/fixed_population.py --N_c 1000 --m 20 --fitness "static_inc" --output "time" --datafile "$datafile"
    echo -n "," >> "$datafile"
    python3 ../src/fixed_population.py --m 20 --fitness "static_inc" --output "time" --datafile "$datafile"
    echo >> "$datafile"
done 


module purge

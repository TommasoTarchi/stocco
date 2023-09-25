#!/bin/bash


###
###


#SBATCH --no-requeue
#SBATCH --job-name="spatial_model"
#SBATCH --partition=EPYC
#SBATCH -N 1
#SBATCH -n 10
#SBATCH --time=02:00:00


module load architecture/AMD
module load conda/23.3.1

conda activate stoch_modelling

export OMP_NUM_THREADS=10


datafile=$(pwd)/data.csv

echo "# data for final state of spatial model to check mutual influence" > "$datafile"
echo "# among neighbour areas' distributions" >> "$datafile"
echo "# " >> "$datafile"
echo "# number of genotipic classes: 4" >> "$datafile"
echo "# N_tilde: fixed to 10000" >> "$datafile"
echo "# fitness landscape: static increasing" >> "$datafile"
echo "# resolution: 64" >> "$datafile"
echo "# " >> "$datafile"

echo -n "simulation_time,elapsed_time," >> "$datafile"
for i in {1..64}
do
    echo -n state_area"$i", >> "$datafile"
done
echo "state_world" >> "$datafile"

python3 ../src/spatial_ngb.py --m 4 --N_0 10000 --fitness "static_inc" --resolution 64 --output "final_state" --datafile "$datafile"


module purge

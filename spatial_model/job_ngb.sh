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


datafile=$(pwd)/data_ngb.csv

echo "# " > "$datafile"
echo "# " >> "$datafile"
echo "# " >> "$datafile"
echo "# number of genotipic classes: 3" >> "$datafile"
echo "# population size: variable with N_tilde=10000" >> "$datafile"
echo "# resolution: 16" >> "$datafile"
echo "# " >> "$datafile"

echo "simulation_time,elapsed_time,state_area0,state_area1,state_area2,state_area3,state_world" >> "$datafile"
for index in {1..20}
do
    python3 ../src/spatial_ngb.py --m 3 --N_0 10000 --fitness "static_inc" --resolution 25 --output "final_state" --datafile "$datafile"
    echo >> "$datafile"
done 


module purge

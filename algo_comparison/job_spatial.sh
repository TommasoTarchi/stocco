#!/bin/bash


### script to run several simulations with spatial algorithm and different resolutions
### on Orfeo, cluster hosted at Area Science Park (Trieste, Italy)


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


datafile=$(pwd)/data_spatial.csv

echo "# data for simulation time and efficiency comparision among" > "$datafile"
echo "# spatial algorithm with different values of resolution" >> "$datafile"
echo "#" >> "$datafile"
echo "# fitness landscape: static increasing" >> "$datafile"
echo "# number of genotipic classes: 4" >> "$datafile"
echo "# population size: 1000000" >> "$datafile"
echo "# " >> "$datafile"

echo "base_simul,base_elpsd,4_simul,4_elpsd,16_simul,16_elpsd,36_simul,36_elpsd,64_simul,64_elpsd,100_simul,100_elpsd">> "$datafile"
for index in {1..20}
do
    python3 ../src/dynamic_population.py --m 4 --N_0 1000000 --fitness "static_inc" --output "time" --datafile "$datafile"
    echo -n "," >> "$datafile"
    python3 ../src/spatial_ngb.py --resolution 4 --m 4 --N_0 1000000 --fitness "static_inc" --output "time" --datafile "$datafile"
    echo -n "," >> "$datafile"
    python3 ../src/spatial_ngb.py --resolution 16 --m 4 --N_0 1000000 --fitness "static_inc" --output "time" --datafile "$datafile"
    echo -n "," >> "$datafile"
    python3 ../src/spatial_ngb.py --resolution 36 --m 4 --N_0 1000000 --fitness "static_inc" --output "time" --datafile "$datafile"
    echo -n "," >> "$datafile"
    python3 ../src/spatial_ngb.py --resolution 64 --m 4 --N_0 1000000 --fitness "static_inc" --output "time" --datafile "$datafile"
    echo -n "," >> "$datafile"
    python3 ../src/spatial_ngb.py --resolution 100 --m 4 --N_0 1000000 --fitness "static_inc" --output "time" --datafile "$datafile"
    echo >> "$datafile"
done 


module purge

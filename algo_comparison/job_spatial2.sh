#!/bin/bash


### script to be launched after job_spatial.sh to complete the data gathering on
### Orfeo (it was needed because of the time constraint we had on the cluster)


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

echo >> "$datafile"
for index in {1..10}
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

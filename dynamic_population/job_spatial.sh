#!/bin/bash


### script to run some simulations with spatial algorithm to see whether the parameter N_tilde
### actually controls the true population N, on Orfeo, cluster hosted at Area Science Park 
### (Trieste, Italy)
###
### N_tilde: constant


#SBATCH --no-requeue
#SBATCH --job-name="N_tilde"
#SBATCH --partition=EPYC
#SBATCH -N 1
#SBATCH -n 10
#SBATCH --time=02:00:00


module load architecture/AMD
module load conda/23.3.1

conda activate stoch_modelling

export OMP_NUM_THREADS=10


datafile=$(pwd)/data_spatial_1.csv

echo "# data to see the effect of the paramenter N_tilde on the population" > "$datafile"
echo "# size in simulations with spatial algorithm" >> "$datafile"
echo "#" >> "$datafile"
echo "# N_tilde: constant at 10000" >> "$datafile"
echo "# fitness: static increasing" >> "$datafile"
echo "# number of genotipic classes: 4" >> "$datafile"
echo "# resolution of the 'world': 16" >> "$datafile"
echo "# " >> "$datafile"

echo "t,N_tilde,N" >> "$datafile"
python3 ../src/spatial_ngb.py --resolution 16 --m 4 --N_0 10000 --fitness "static_inc" --output "population" --datafile "$datafile"

datafile=$(pwd)/data_spatial_2.csv

echo "# data to see the effect of the paramenter N_tilde on the population" > "$datafile"
echo "# size in simulations with spatial algorithm" >> "$datafile"
echo "#" >> "$datafile"
echo "# N_tilde: constant at 10000" >> "$datafile"
echo "# fitness: static increasing" >> "$datafile"
echo "# number of genotipic classes: 4" >> "$datafile"
echo "# resolution of the 'world': 16" >> "$datafile"
echo "# " >> "$datafile"

echo "t,N_tilde,N" >> "$datafile"
python3 ../src/spatial_ngb.py --resolution 16 --m 4 --N_0 10000 --fitness "static_inc" --output "population" --datafile "$datafile"

datafile=$(pwd)/data_spatial_3.csv

echo "# data to see the effect of the paramenter N_tilde on the population" > "$datafile"
echo "# size in simulations with spatial algorithm" >> "$datafile"
echo "#" >> "$datafile"
echo "# N_tilde: constant at 10000" >> "$datafile"
echo "# fitness: static increasing" >> "$datafile"
echo "# number of genotipic classes: 4" >> "$datafile"
echo "# resolution of the 'world': 16" >> "$datafile"
echo "# " >> "$datafile"

echo "t,N_tilde,N" >> "$datafile"
python3 ../src/spatial_ngb.py --resolution 16 --m 4 --N_0 10000 --fitness "static_inc" --output "population" --datafile "$datafile"

datafile=$(pwd)/data_spatial_4.csv

echo "# data to see the effect of the paramenter N_tilde on the population" > "$datafile"
echo "# size in simulations with spatial algorithm" >> "$datafile"
echo "#" >> "$datafile"
echo "# N_tilde: constant at 10000" >> "$datafile"
echo "# fitness: static increasing" >> "$datafile"
echo "# number of genotipic classes: 4" >> "$datafile"
echo "# resolution of the 'world': 16" >> "$datafile"
echo "# " >> "$datafile"

echo "t,N_tilde,N" >> "$datafile"
python3 ../src/spatial_ngb.py --resolution 16 --m 4 --N_0 10000 --fitness "static_inc" --output "population" --datafile "$datafile"

module purge

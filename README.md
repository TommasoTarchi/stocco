# stocco

This is **stocco**, final project for the exam Stochastic Modelling and Simulation from MSc in Data Science and Scientific Computing 
at University of Trieste/SISSA. The aim is that of reproducing the simulations results exposed in [this paper](Zhu-Efficient_simul_population_model_carcinogenesis.pdf) and (possibly) extend them.


## What you will find in this repository

- This README file
- `Zhu-Efficient_simul_population_model_carcinogenesis.pdf`: paper used as basis for the project
- `presentation.pdf`: slide presentation of the project
- `src/`: directory containing all python codes used to run the simulations; contains:
  - `stocco_lib.py`: library containing all functions used for the simulations
  - `fixed_population.py`: script used for fixed-population simulations
  - `dynamic_population.py`: script used for dynamic-population simulations
- `algo_comparison/`: directory containing results obtained with fixed population and static fitness landscape to compare exact and
  hybrid algorithms' results and performances
- `fitness_comparison/`: directory containing results obtained with fixed population and different fitness landscapes to compare the
  behaviour of the system

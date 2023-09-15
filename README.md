# stocco

This is **stocco**, final project for the exam Stochastic Modelling and Simulation, part of the MSc in Data Science and Scientific Computing 
at Uiversity of Trieste/SISSA. The aim is that of reproducing the simulations results exposed in [this paper](Zhu-Efficient_simul_population_model_carcinogenesis.pdf) and (possibly) extend them.


## What you will find in this repository

- This README file
- `Zhu-Efficient_simul_population_model_carcinogenesis.pdf`: paper used as basis for the project
- `presentation.pdf`: slide presentation of the project
- `src/`: directory containing all python codes used to run the simulations; contains:
  - `stocco_lib.py`: library containing all functions used for the simulations
  - `fixed_population.py`: script used for fixed-population simulations
- `fixed_pop-flat_fit/`: directory containing simulations with fixed population and flat fitness landscape; contains:
- `fixed_pop-stat_fit/`: directory containing simulations with fixed population and static fitness landscape; contains:
  - `algo_comparison.sh`: script to run simulation with both exact and hybrid algorithms to compare performance
  - `algo_comparison.csv`: data for comparison between exact and hybrid algorithms
- `fixed_pop-dyn_fit/`: directory containing simulations with fixed population and dynamic fitness landscape; contains:
- `var_pop-dyn_fit/`: directory containing simulations with variable population and dynamic fitness landscape; contains:

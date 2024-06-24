# Stocco

This is **Stocco**, final project for the exam Stochastic Modelling and Simulation from MSc in Data Science and Scientific Computing 
at University of Trieste/SISSA. I took the base model from [this paper][link1], by Tianqi Zhu, Yucheng Hu, Zhi-Ming Ma, De-Xing Zhang,
Tiejun Li and Ziheng Yang. My contribute consisted in adding competition and a spatial structure.

For an overview of the whole project see [this presentation](Stocco-Presentation.pdf).

**Note**: there is a small error in the code for spatial model, leading to an increasing mutation rate for increasing resolution;
because of that, please consider the results on waiting time and efficiency of spatiotemporal algorithms when varying resolution to
be wrong.

**Note**: some of the data in CSV files are not the same used in the slide presentation; the reason is that I ran some additional 
tests after I had already written the presentation. However, the results are coherent.


## What you will find in this repository

- This README file
- `Stocco-Presentation.pdf`: slide presentation of the project
- `src/`: directory containing all python codes used to run the simulations; contains:
  - `stocco_lib.py`: library containing all functions used for the simulations
  - `fixed_population.py`: script used for fixed-population non-spatial simulations
  - `dynamic_population.py`: script used for dynamic-population non-spatial simulations
  - `spatial.py`: script used for dynamic-population spatial simulations (naive, actually never used in the project)
  - `spatial_ngb.py`: script used for dynamic-population spatial simulations (less naive, used in the project)
- `algo_comparison/`: directory containing results obtained with all algorithms to compare waiting time and efficiency
- `fitness_comparison/`: directory containing results obtained with fixed population and different fitness landscapes to compare the
  behaviour of the system
- `dynamic_population/`: directory containing results obtained with dynamic population to check whether the $\tilde{N}$ parameter is
  actually able to control the population size
- `spatial_model/`: directory containing results for final average genotype distribution in spatial model
- `fitness_graphs/`: directory containing scripts for graphs (not interesting)


## References

- Tianqi Zhu, Yucheng Hu, Zhi-Ming Ma, De-Xing Zhang, Tiejun Li, Ziheng Yang, Efficient simulation under a population genetics model of carcinogenesis, Bioinformatics, Volume 27, Issue 6, March 2011, Pages 837–843, [https://doi.org/10.1093/bioinformatics/btr025][link1].



[link1]: https://doi.org/10.1093/bioinformatics/btr025

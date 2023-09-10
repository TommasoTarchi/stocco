import numpy as np
import stocco_lib as stclb



if __name__ == "__main__":



    # parameters setting

    N = 10000   # population size
    m = 100   # number of genotipic classes
    N_c = 10   # threshold for population size
    epsilon = 0.04   # parameter of the leaping condition 

    t = 0   # time

    # setting initial distribution of population in genotipic
    # space and assigning fitness to genotipic classes
    x = np.zeros(m)   # genotipic distribution
    x[0] = N
    s = np.zeros(m)   # fitness distribution



    while True:


        a = stclb.compute_rates(x, s, mu)


        SIGMA = np.where(a > N_c)[0]
        sigma = np.where(a <= N_c)[0]


        tau = stclb.compute_tau(epsilon)




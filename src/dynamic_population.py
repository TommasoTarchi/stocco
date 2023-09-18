import numpy as np
import math
import argparse
import time
import stocco_lib as stclb




# default parameters
N_0_deflt = 1000   # starting value of the N_tilde parameter (and of the 
                   # true population size)
m_deflt = 4   # number of genotipic classes
N_c_deflt = 10   # population threshold for exact evolution (i.e. use of
                 # Gillespie algorithm)
epsilon_deflt = 0.04   # parameter of the leaping condition
fitness_deflt = 'flat'   # kind of fitness distribution over genotipic space
N_tilde_mod_deflt = 'constant'   # behaviour of the N_tilde parameter
datafile_deflt = 'results.txt'   # file to store results
output_deflt = 'screen'   # kind of results to store




if __name__ == "__main__":



    # parameters setting

    parser = argparse.ArgumentParser()
    parser.add_argument('--N_0', type=int, default=N_0_deflt)
    parser.add_argument('--m', type=int, default=m_deflt)
    parser.add_argument('--N_c', type=int, default=N_c_deflt)
    parser.add_argument('--epsilon', type=float, default=epsilon_deflt)
    parser.add_argument('--fitness', choices=['flat', 'static_inc', 'static_dec', 'static_mount', 'dynamic'], default=fitness_deflt)
    parser.add_argument('--N_tilde_mod', choices=['constant', 'growing'], default=N_tilde_mod_deflt)
    parser.add_argument('--datafile', default=datafile_deflt)
    parser.add_argument('--output', choices=['screen', 'time', 'population'], default=output_deflt)

    args = parser.parse_args()

    N_tilde_mod = args.N_tilde_mod
    N_0 = args.N_0   # initial population
    N_tilde = N_0
    N = N_0
    m = args.m
    N_c = args.N_c
    epsilon = args.epsilon

    # population distribution in genotipic space
    x = np.zeros(m+1)
    x[0] = N_tilde

    # fitness distribution in genotipic space
    fitness = args.fitness
    f = np.ones(m)
    if args.fitness == 'flat':   # flat fitness landscape
        pass
    elif args.fitness == 'static_inc':   # static increasing fitness landscape
        f += 0.01
        for i in range(m):
            f[i] = f[i]**i
    elif args.fitness == 'static_dec':   # static decreasing fitness landscape
        f += 0.01
        for i in range(m):
            f[i] = f[i]**(m-i-1)
    elif args.fitness == 'static_mount':   # static 'mountain' fitness landscape
        f += 0.01
        for i in range(m):
            f[i] = f[i]**(m-math.fabs(m-2*i))
    elif args.fitness == 'dynamic':   # dynamic fitness landscape
        f += 0.01
        for i in range(m):
            f[i] = f[i]**(m-math.fabs(m-2*i))   # the static component is of the 
                                                # 'mountain' kind; the dynamic 
                                                # part is computed at the beginning
                                                # of each iteration of the main
                                                # loop

    mu = np.full(m, 1/N)   # mutation rate distribution

    t = 0   # time
    
    # setting datafile options
    datafile = args.datafile
    output = args.output
   


    # printing population data
    if output == 'population':
        with open(datafile, 'a') as file:
            file.write(f"{N_tilde},{N}\n")



    # for efficiency measure
    start_time = time.time()



    # main loop (evolution)

    m_temp = 1   # 'highest' genotipic class reached so far plus one
    while m_temp != m+1:


        # updating population parameters
        if N_tilde_mod == 'growing':
            ex = math.exp(0.001 * t)
            N_tilde = 10e7 * N_0 * ex / (10e7 + N_0*ex - 1)


        f_part = f[:m_temp]   # fitness values that will be actually used
                              # at this iteration

        # computing the dynamic component of the fitness
        if fitness == 'dynamic':
            x_rate = x[:m_temp]/N
            f_part += np.ones(m_temp)
            for i in range(m_temp):
                for j in range(m_temp):
                    f_part[i] -= x_rate[j] * (m-math.fabs(i-j)) / m


        # computing the events' rates
        a = stclb.compute_rates_dyn_pop(x[:m_temp], N_tilde, f_part, mu[:m_temp]) 


        # partitioning the set of events in non-critical and critical ones

        sigma = np.where(x[:m_temp] <= N_c)[0]   # small population classes
        SIGMA = np.where(x[:m_temp] > N_c)[0]   # large population classes


        OMEGA = []   # non-critical set
        LAMBDA = []   # critical set
        for i in range(3):
            for j in sigma:
                OMEGA.append(i*m_temp + j)
            for j in SIGMA:
                LAMBDA.append(i*m_temp + j)


        a_ncrit = a[OMEGA]   # non-critical events' rates
        a_crit = a[LAMBDA]   # critical events' rates


        # computing leap time and time to next critical reaction

        tau = stclb.compute_tau(epsilon) 


        e = tau + 1
        if a_crit.shape[0] > 0 and np.sum(a_crit) > 0:
            e = stclb.compute_e(a_crit)
        
        h = min(tau, e)


        # using the Gillespie algorithm (if any critical events occurred)
        if e < tau:

 
            # computing the index of the event

            index = LAMBDA[stclb.Gillespie_extract(a_crit)]
           
            
            # updating the state (we do it directly without using the state-change
            # vector)
            event_type = index // m_temp
            event_index = index % m_temp
            if event_type == 0:
                x[event_index] += 1
            elif event_type == 1:
                x[event_index] -= 1
            else:
                x[event_index] -= 1
                x[event_index+1] += 1


           
        r = stclb.tau_leap_extract(a_ncrit, h)

        
        # using the tau-leap algorithm
        i = 0
        for index in OMEGA:
            
            # updating the state (we do it directly without using the state-change
            # vector)
            event_type = index // m_temp
            event_index = index % m_temp
            if event_type == 0:
                x[event_index] += r[i]
            elif event_type == 1:
                x[event_index] -= r[i]
            else:
                x[event_index] -= r[i]
                x[event_index+1] += r[i]

            i += 1


        # updating time and 'highest' genotipic class reached so far
        t += h
        if x[m_temp] > 0:
            m_temp += 1


        # updating population size
        N = np.sum(x[:m_temp])


        # printing population data
        if output == 'population':
            with open(datafile, 'a') as file:
                file.write(f"{N_tilde},{N}\n")


        # the algorithm did not converge within an acceptable time
        if t > 20000 + m * 2000:
            t = 'not_converge'
            break



    # for efficieny measure
    elapsed_time = time.time() - start_time


    
    # printing final results 
    
    if output == 'screen':
        print(f"final state:  {x}\nsimulation time:  {t}\nelapsed time:  {elapsed_time} s\n")

    elif output == 'time':
        with open(datafile, 'a') as file:
            file.write(f"{t},{elapsed_time}")

import time
import argparse
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

resolution_deflt = 4   # number of areas in which the world is divided

datafile_deflt = 'results.txt'   # file to store results
output_deflt = 'screen'   # kind of results to store




if __name__ == "__main__":



    # parameters setting

    parser = argparse.ArgumentParser()
    parser.add_argument('--N_0', type=int, default=N_0_deflt)
    parser.add_argument('--m', type=int, default=m_deflt)
    parser.add_argument('--N_c', type=int, default=N_c_deflt)
    parser.add_argument('--epsilon', type=float, default=epsilon_deflt)
    parser.add_argument('--fitness', choices=['flat', 'static_inc', 'static_dec', 'static_mount'], default=fitness_deflt)
    parser.add_argument('--N_tilde_mod', choices=['constant',], default=N_tilde_mod_deflt)
    parser.add_argument('--resolution', type=int, choices=[i**2 for i in range(1, 1000)], default=resolution_deflt)
    parser.add_argument('--datafile', default=datafile_deflt)
    parser.add_argument('--output', choices=['screen', 'time', 'final_state', 'population'], default=output_deflt)

    args = parser.parse_args()


    N_tilde_mod = args.N_tilde_mod
    N_0 = args.N_0 // args.resolution * args.resolution
    N_tilde = N_0
    m = args.m
    N_c = args.N_c
    epsilon = args.epsilon
    resolution = args.resolution


    
    # initializing the world
    wrld = stclb.world_w_neighbours(N_0, m, N_c, args.fitness, args.resolution)
    wrld.find_neighbours()
    wrld.compute_mu()


    
    # setting datafile options
    datafile = args.datafile
    output = args.output



    t = 0.0


    
    # for efficiency measure
    start_time = time.time()



    # computing tau-leap time step
    tau = stclb.compute_tau(epsilon)



    # main loop (evolution)

    m_temp = 1   # 'highest' genotipic class reached so far plus one
    while m_temp != m+1:

        
        wrld.compute_rates(N_tilde / resolution)


        wrld.compute_partition()


        # computing time to next critical event
        e = wrld.compute_e(tau)

        e_copy = e.copy()
        if tau+1 in e_copy:
            e_copy.remove(tau+1)
        mid_e = min(e_copy) + (max(e_copy)-min(e_copy)) / 2
        
        e.append(tau)
        h = min(e)
        h_index = e.index(h)

        
        # applying Gillespie's algorithm
        #if h_index < resolution:
        #    wrld.Gillespie_apply(h_index)
        if mid_e < tau:   # heuristic error fixing
            wrld.Gillespie_apply(h_index)


        # applying tau-leap algorithm
        wrld.tau_leap_apply(h)


        # updating time and 'highest' genotipic class reached so far
        t += h 
        wrld.update_parms()
        wrld.update_parms_tot()
        m_temp = wrld.return_m_temp()


        if output == 'population':
            with open(datafile, 'a') as file:
                file.write(f"{t},{N_0},{wrld.N_tot}\n") 


        # the algorithm did not converge within an acceptable time
        if t > 50000 + m*2000:
            t = 'not_converge'
            break



    # updating total population distribution
    wrld.update_parms_tot()



    # for efficieny measure
    elapsed_time = time.time() - start_time



    # printing results

    if output == 'screen':
        print(f"final state:  {wrld.x_tot}\nsimulation time:  {t}\nelapsed time:  {elapsed_time} s\n")
    
    elif output == 'time':
        with open(datafile, 'a') as file:
            file.write(f"{t},{elapsed_time}")

    elif output == 'final_state':
        with open(datafile, 'a') as file:
            file.write(f"{t},{elapsed_time},")
            for i in range(resolution):
                file.write(f"{wrld.x[i]},")
            file.write(f"{wrld.x_tot}")

import numpy as np
import stocco_lib as stclb
import time



if __name__ == "__main__":



    start_time = time.time()



    # parameters setting

    N = 1000   # population size
    m = 4   # number of genotipic classes
    N_c = 10   # threshold for population size
    epsilon = 0.04   # parameter of the leaping condition 

    t = 0   # time

    # setting initial distribution of population in genotipic
    # space and assigning fitness and mutation rates to genotipic
    # classes
    x = np.zeros(m+1)   # genotipic distribution
    x[0] = N
    s = np.zeros(m)   # fitness distribution
    mu = np.full(m, 1/N)   # mutation rate distribution



    # initializing the state-change vector

    #v = np.zeros((m**2, m+1))

    # initializing death/birth events
    #for i in range(m):
    #    for j in range(i):
    #        v[i*m+j, i] = -1
    #        v[i*m+j, j] = 1
    #    for j in range(i, m-1):
    #        v[i*m+j, i] = -1
    #        v[i*m+j, j+1] = 1

    # initializing mutation events
    #for i in range(m*(m-1), m**2):
    #    ind = 0
    #    v[ind, ind] = -1
    #    v[ind, ind+1] = 1
    #    ind += 1 
    


    # main loop (evolution)

    m_temp = 1   # 'highest' genotipic class reached so far plus one
    while m_temp != m+1:
        

        #####################
        #print(m_temp)
        #print(t)
        #if t == 0:
        #    f = open("states.dat", "w")
        #    f.close()
        #if t % 20 < 0.1:           
        #    f = open("states.dat", "a")
        #    f.write(f"{x}\n")
        #    f.close()
        #print(f"x:  {x}")
        #####################


        # computing the events rates
        a = stclb.compute_rates(x[:m_temp], s[:m_temp], mu[:m_temp])


        # partitioning the set of events in non-critical and critical ones

        sigma = np.where(x[:m_temp] <= N_c)[0]   # small population classes

        OMEGA = list(range(m_temp**2))   # non-critical set
        LAMBDA = []   # critical set
        for i in sigma:
            for j in range(i):
                pos = j*(m_temp-1)+i-1
                if pos in OMEGA:
                    OMEGA.remove(pos)
                    LAMBDA.append(pos)
            for j in range(i*(m_temp-1), (i+1)*(m_temp-1)):
                if j in OMEGA:
                    OMEGA.remove(j)
                    LAMBDA.append(j)
            for j in range(i+1, m_temp):
                pos = j*(m_temp-1)+i
                if pos in OMEGA:
                    OMEGA.remove(pos)
                    LAMBDA.append(pos)
            OMEGA.remove(m_temp*(m_temp-1)+i)
            LAMBDA.append(m_temp*(m_temp-1)+i)
        LAMBDA.sort()


        a_ncrit = a[OMEGA]
        a_crit = a[LAMBDA]


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
            if index < m_temp*(m_temp-1):
                j = index // (m_temp-1)
                j_prime = index % (m_temp-1)
                if j <= j_prime:
                    j_prime += 1
                x[j] -= 1
                x[j_prime] += 1
            else:
                x[index-m_temp*(m_temp-1)] -= 1
                x[index-m_temp*(m_temp-1)+1] += 1

           
        r = stclb.tau_leap_extract(a_ncrit, h)

        
        # using the tau-leap algorithm
        i = 0
        for index in OMEGA:
            
            # updating the state (we do it directly without using the state-change
            # vector)
            if index < m_temp*(m_temp-1):
                j = index // (m_temp-1)
                j_prime = index % (m_temp-1)
                if j <= j_prime:
                    j_prime += 1
                x[j] -= r[i]
                x[j_prime] += r[i]
            else:
                x[index-m_temp*(m_temp-1)] -= r[i]
                x[index-m_temp*(m_temp-1)+1] += r[i]

            i += 1
        

        # updating time and 'highest' genotipic class reached so far
        t += h
        if x[m_temp] > 0:
            m_temp += 1



    elapsed_time = time.time() - start_time


    
    # printing final state and time 
    print(f"final state:  {x}\nfinal time:  {t}\nelapsed simulation time:  {elapsed_time}\n")

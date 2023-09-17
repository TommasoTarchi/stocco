import numpy as np




# computes events' rates for fixed population size (in the array a 
# death/birth events are placed before mutation events)
def compute_rates(x, f, mu):


    m = x.shape[0]
    a = np.zeros(m**2)
    

    # computing birth/death rates
    norm = np.sum(f*x)
    for j in range(m):
        a[j*(m-1):(j+1)*(m-1)] = (np.delete(f, j)) * np.delete(x, j)
        a[j*(m-1):(j+1)*(m-1)] *= x[j]
    a[:m*(m-1)] /= norm


    # computing mutation rates
    a[m*(m-1):m*m] = mu*x


    return a




# computes events' rates for dynamic population size (in the array a birth 
# events come first, then death and finally mutation ones)
def compute_rates_dyn_pop(x, N_tilde, f, mu):


    m = x.shape[0]
    a = np.zeros(m*3)
    for i in range(3):
        a[i*m:(i+1)*m] = x


    # computing birth rates
    norm = np.sum(f*x)
    a[:m] *= N_tilde * f / norm

    # death rates already computed

    # computing mutation rates
    a[2*m:3*m-1] *= mu


    return a




# computes the tau-leaping step length, given the parameter epsilon of the
# leaping condition
def compute_tau(epsilon):
    
    return epsilon/2




# extracts time to next critical event (to be used in Gillespie algorithm)
def compute_e(a):

    a_tot = np.sum(a)

    e = np.random.exponential(scale=1/a_tot)

    return e




# extracts the index of the next event in Gillespie algorithm (to be used in 
# Gillespie algorithm)
def Gillespie_extract(a):


    # selecting only a's elements that are different from zero
    good_indexes = np.where(a>0)[0]
    a_good = a[good_indexes]

    a_tot = np.sum(a)
    m_2 = a_good.shape[0]   # number of possible events


    u = np.random.uniform() * a_tot

    
    # computing 'cumulative' rates
    a_cum = np.zeros(m_2)
    a_cum[0] = a_good[0]
    for i in range(1, m_2):
        a_cum[i] = a_cum[i-1] + a_good[i]
           
    
    # extracting the index (naive algorithm)
    #found = False
    #index = 0
    #while not found:
    #    if u < a_cum[index]:
    #        found = True
    #    else:
    #        index += 1


    # extracting the index (recursive algorithm)
    index = find_index(u, a_cum)


    return good_indexes[index]




# extracts events happened during a tau-leap step
def tau_leap_extract(a, h):

    r = np.random.poisson(lam=a*h)

    return r




# function for the recursive algorithm used in Gillespie_extract()
def find_index(u, a_cum):

        index = a_cum.shape[0] // 2
        
        if index == 0:
            return index
        
        if u <= a_cum[index-1]:
            index = find_index(u, a_cum[:index])
        elif a_cum[index] < u:
            index += 1 + find_index(u, a_cum[index+1:])
       
        return index

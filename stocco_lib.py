import numpy as np




# computes events' rates (for all events, both critical and non-critical);
# in the array a death/birth events are placed before mutation events
def compute_rates(x, s, mu):


    m = x.shape[0]
    a = np.zeros(m**2)
    
    # computing rates of birth/death events
    norm = np.sum((1+s)*x)
    for j in range(m):
        a[j*(m-1):(j+1)*(m-1)] = (1+np.delete(s, j)) * np.delete(x, j)
        a[j*(m-1):(j+1)*(m-1)] *= x[j]
    a[:m*(m-1)] /= norm


    # computing rates of mutation events
    a[m*(m-1):m*m] = mu*x


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
           

    # extracting the index (we use a sort of binary search strategy)
    #found = False
    #index = m_2//2
    #while (not found) and index>0:
    #    if a_cum[index-1]<=u and u<a_cum[index]:
    #        found = True
    #    elif u<a_cum[index-1]:
    #        index = index//2
    #    else:
    #        index += (m_2-index)//2


    found = False
    index = 0
    while not found:
        if u < a_cum[index]:
            found = True
        else:
            index += 1


    return good_indexes[index]




def tau_leap_extract(a, h):

    r = np.random.poisson(lam=a*h)

    return r

import numpy as np
import math




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
    a[2*m:3*m] *= mu


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




# class for evolution with spatial structure
class world:


    def __init__(self, N_0, m, N_c, fitness, resolution):
        
        self.N_tot = N_0   # initial population
        self.m = m   # number of genotipic classes
        self.N_c = N_c   # threshold for small populations
        self.fitness = fitness
        self.resolution = resolution   # number of areas in which
                                       # we divide the world
        self.dim = math.sqrt(self.resolution)
        
        # total population distribution in genotipic space
        self.x_tot = np.zeros(self.m+1)
        self.x_tot[0] = self.N_tot

        # single areas' distributions in genotipic space
        self.N = np.repeat(self.N_tot / self.resolution, self.resolution)
        self.x = []
        for i in range(self.resolution):
            self.x.append(self.x_tot / self.resolution)
        self.m_temp = np.repeat(1, self.resolution)

        # fitness distribution in genotipic space
        self.f = np.ones(self.m)
        if fitness == 'flat':   # flat fitness landscape
            pass
        elif fitness == 'static_inc':   # static increasing fitness landscape
            self.f += 0.01
            for i in range(self.m):
                self.f[i] = self.f[i]**i
        elif fitness == 'static_dec':   # static decreasing fitness landscape
            self.f += 0.01
            for i in range(self.m):
                self.f[i] = self.f[i]**(self.m-i-1)
        elif fitness == 'static_mount':   # static 'mountain' fitness landscape
            self.f += 0.01
            for i in range(self.m):
                self.f[i] = self.f[i]**(self.m-math.fabs(self.m-2*i))

        self.mu = np.full(self.m, 1 / self.N_tot)   # mutation rate distribution
    

    # computes events' rates
    def compute_rates(self, N_tilde):
                
        self.a = [] 
        
        for i in range(self.resolution):
            self.a.append(compute_rates_dyn_pop(self.x[i][:self.m_temp[i]], N_tilde, self.f[:self.m_temp[i]], self.mu[:self.m_temp[i]])) 


    # partitioning the set of events in non-critical and critical ones
    def compute_partition(self):

        self.sigma = []
        self.SIGMA = []
        self.OMEGA = []
        self.LAMBDA = []

        self.a_crit = []
        self.a_ncrit = []

        for id in range(self.resolution):
            
            self.sigma.append(np.where(self.x[id][:self.m_temp[id]] <= self.N_c)[0])   # small population classes
            self.SIGMA.append(np.where(self.x[id][:self.m_temp[id]] > self.N_c)[0])   # large population classes

            self.OMEGA.append([])   # non-critical set
            self.LAMBDA.append([])   # critical set
            for i in range(3):
                for j in self.sigma[id]:
                    self.LAMBDA[id].append(i*self.m_temp[id] + j)
                for j in self.SIGMA[id]:
                    self.OMEGA[id].append(i*self.m_temp[id] + j)

            self.a_ncrit.append(self.a[id][self.OMEGA[id]])   # non-critical events' rates
            self.a_crit.append(self.a[id][self.LAMBDA[id]])   # critical events' rates


    def compute_e(self, tau):

        e = []

        for i in range(self.resolution):
            if self.a_crit[i].shape[0] > 0 and np.sum(self.a_crit[i]) > 0:
                e.append(compute_e(self.a_crit[i]))
            else:
                e.append(tau+1)

        return e


    def Gillespie_apply(self, id):

        # computing the index of the event
        index = self.LAMBDA[id][Gillespie_extract(self.a_crit[id])]         
        
        # updating the state (we do it directly without using the state-change
        # vector)
        event_type = index // self.m_temp[id]
        event_index = index % self.m_temp[id]
        if event_type == 0:
            self.x[id][event_index] += 1
        elif event_type == 1:
            self.x[id][event_index] -= 1
        else:
            self.x[id][event_index] -= 1
            self.x[id][event_index+1] += 1


    def tau_leap_apply(self, h):

        for id in range(self.resolution):

            r = tau_leap_extract(self.a_ncrit[id], h)
            
            # using the tau-leap algorithm
            i = 0
            for index in self.OMEGA[id]:
                
                # updating the state (we do it directly without using the state-change
                # vector)
                event_type = index // self.m_temp[id]
                event_index = index % self.m_temp[id]
                if event_type == 0:
                    self.x[id][event_index] += r[i]
                elif event_type == 1:
                    self.x[id][event_index] -= r[i]
                else:
                    self.x[id][event_index] -= r[i]
                    self.x[id][event_index+1] += r[i]

                i += 1


    def return_m_temp(self):

        return np.max(self.m_temp) 


    # updates population size and 'highest' genotipic class reached
    def update_parms(self):

        for i in range(self.resolution):

            if self.x[i][self.m_temp[i]] > 0:
                self.m_temp[i] += 1
            
            self.N[i] = np.sum(self.x[i])


    def update_parms_tot(self):

        self.x_tot = np.zeros(self.m+1)
        self.N_tot = 0

        for i in range(self.resolution):
            self.x_tot += self.x[i]
            self.N_tot += self.N[i]

    
    def print_state(self, datafile):

        with open(datafile, 'a') as file:
            for i in range(self.resolution):
                file.write(f"{self.x[i]},")
            file.write(f"{self.x_tot}")



# class for evolution with spatial structure and (reduced) neighbours' contribution
# to events rates
class world_w_neighbours:


    def __init__(self, N_0, m, N_c, fitness, resolution):
        
        self.N_tot = N_0    # initial population
        self.m = m   # number of genotipic classes
        self.N_c = N_c   # threshold for small populations
        self.fitness = fitness
        self.resolution = resolution   # number of areas in which
                                       # we divide the world
        self.dim = int(math.sqrt(self.resolution))
        
        # total population distribution in genotipic space
        self.x_tot = np.zeros(self.m+1)
        self.x_tot[0] = self.N_tot

        # single areas' distributions in genotipic space
        self.N = np.repeat(self.N_tot / self.resolution, self.resolution)
        self.x = []
        for i in range(self.resolution):
            self.x.append(self.x_tot / self.resolution)
        self.m_temp = np.repeat(1, self.resolution)

        # fitness distribution in genotipic space
        self.f = np.ones(self.m)
        if fitness == 'flat':   # flat fitness landscape
            pass
        elif fitness == 'static_inc':   # static increasing fitness landscape
            self.f += 0.01
            for i in range(self.m):
                self.f[i] = self.f[i]**i
        elif fitness == 'static_dec':   # static decreasing fitness landscape
            self.f += 0.01
            for i in range(self.m):
                self.f[i] = self.f[i]**(self.m-i-1)
        elif fitness == 'static_mount':   # static 'mountain' fitness landscape
            self.f += 0.01
            for i in range(self.m):
                self.f[i] = self.f[i]**(self.m-math.fabs(self.m-2*i))


    # find each area's neighbour areas
    def find_neighbours(self):

        self.neigh = []

        for i in range(self.resolution):

            self.neigh.append([])
            
            if i // self.dim == 0:   # first row
                if i % self.dim == 0:   # first column
                    self.neigh[i].append(i+1)
                    self.neigh[i].append(i+self.dim+1)
                elif i % self.dim == self.dim-1:   # last column
                    self.neigh[i].append(i-1)
                    self.neigh[i].append(i+self.dim-1)
                else:   # internal columns
                    self.neigh[i].append(i-1)
                    self.neigh[i].append(i+1)
                    self.neigh[i].append(i+self.dim-1)
                    self.neigh[i].append(i+self.dim+1)
                self.neigh[i].append(i+self.dim)
            
            elif i // self.dim == self.dim-1:   # last row
                if i % self.dim == 0:   # first column
                    self.neigh[i].append(i+1)
                    self.neigh[i].append(i-self.dim+1)
                elif i % self.dim == self.dim-1:   # last column
                    self.neigh[i].append(i-1)
                    self.neigh[i].append(i-self.dim-1)
                else:   # internal columns
                    self.neigh[i].append(i-1)
                    self.neigh[i].append(i+1)
                    self.neigh[i].append(i-self.dim-1)
                    self.neigh[i].append(i-self.dim+1)
                self.neigh[i].append(i-self.dim)
            
            else:   # internal rows
                if i % self.dim == 0:   # first column
                    self.neigh[i].append(i+1)
                    self.neigh[i].append(i-self.dim+1)
                    self.neigh[i].append(i+self.dim+1)
                elif i % self.dim == self.dim-1:   # last column
                    self.neigh[i].append(i-1)
                    self.neigh[i].append(i-self.dim-1)
                    self.neigh[i].append(i+self.dim-1)
                else:   # internal columns
                    self.neigh[i].append(i-1)
                    self.neigh[i].append(i+1)
                    self.neigh[i].append(i-self.dim-1)
                    self.neigh[i].append(i-self.dim+1)
                    self.neigh[i].append(i+self.dim-1)
                    self.neigh[i].append(i+self.dim+1)
                self.neigh[i].append(i-self.dim)
                self.neigh[i].append(i+self.dim)


    def compute_mu(self):

        self.mu = []
        for i in range(self.resolution):
            #self.mu.append(np.full(self.m, 1/((self.N_tot/self.resolution)*(1+len(self.neigh[i])/4))))
            self.mu.append(np.full(self.m, 1 / self.N_tot))


    # computes events' rates
    def compute_rates(self, N_tilde):
                
        self.a = []
        
        for i in range(self.resolution):
            
            N_tilde_adj = N_tilde * (1+len(self.neigh[i])/4)   # N_tilde adjusted depending on the 
                                                               # number of neighbours
            # distribution of population in genotipic space adjusted depending on the neighbours' 
            # distributions (the contribute of the neighbours is reduced of a factor 4)
            x_adj = self.x[i][:self.m_temp[i]].copy()
            for ngb_id in self.neigh[i]:
                for j in range(x_adj.shape[0]):
                    if x_adj[j] > 0:   # to avoid negative population in Gillespie algorithm
                        x_adj[j] += self.x[ngb_id][j] // 4
            x_adj[x_adj < 0] = 0   # to avoid negative rates

            a_id = compute_rates_dyn_pop(x_adj, N_tilde, self.f[:self.m_temp[i]], self.mu[i][:self.m_temp[i]])
            #a_id /= (1+len(self.neigh[i])/4) / self.resolution   # 'renormalization' of the rates
            a_id /= (1+len(self.neigh[i])/4)

            self.a.append(a_id) 


    # partitioning the set of events in non-critical and critical ones
    def compute_partition(self):

        self.sigma = []
        self.SIGMA = []
        self.OMEGA = []
        self.LAMBDA = []

        self.a_crit = []
        self.a_ncrit = []

        for id in range(self.resolution):
            
            self.sigma.append(np.where(self.x[id][:self.m_temp[id]] <= self.N_c)[0])   # small population classes
            self.SIGMA.append(np.where(self.x[id][:self.m_temp[id]] > self.N_c)[0])   # large population classes

            self.OMEGA.append([])   # non-critical set
            self.LAMBDA.append([])   # critical set
            for i in range(3):
                for j in self.sigma[id]:
                    self.LAMBDA[id].append(i*self.m_temp[id] + j)
                for j in self.SIGMA[id]:
                    self.OMEGA[id].append(i*self.m_temp[id] + j)

            self.a_ncrit.append(self.a[id][self.OMEGA[id]])   # non-critical events' rates
            self.a_crit.append(self.a[id][self.LAMBDA[id]])   # critical events' rates


    def compute_e(self, tau):

        e = []

        for i in range(self.resolution):
            if self.a_crit[i].shape[0] > 0 and np.sum(self.a_crit[i]) > 0:
                e.append(compute_e(self.a_crit[i]))
            else:
                e.append(tau+1)

        return e


    def Gillespie_apply(self, id):

        # computing the index of the event
        index = self.LAMBDA[id][Gillespie_extract(self.a_crit[id])]
        
        # updating the state (we do it directly without using the state-change
        # vector)
        event_type = index // self.m_temp[id]
        event_index = index % self.m_temp[id]
        if event_type == 0:
            self.x[id][event_index] += 1
        elif event_type == 1:
            self.x[id][event_index] -= 1
        else:
            self.x[id][event_index] -= 1
            self.x[id][event_index+1] += 1


    def tau_leap_apply(self, h):

        for id in range(self.resolution):

            r = tau_leap_extract(self.a_ncrit[id], h)

            # using the tau-leap algorithm
            i = 0
            for index in self.OMEGA[id]:
                
                # updating the state (we do it directly without using the state-change
                # vector)
                event_type = index // self.m_temp[id]
                event_index = index % self.m_temp[id]
                if event_type == 0:
                    self.x[id][event_index] += r[i]
                elif event_type == 1:
                    self.x[id][event_index] -= r[i]
                else:
                    self.x[id][event_index] -= r[i]
                    self.x[id][event_index+1] += r[i]

                i += 1


    def return_m_temp(self):

        return np.max(self.m_temp) 


    # updates population size and 'highest' genotipic class reached
    def update_parms(self):

        for i in range(self.resolution):
            self.x[i][self.x[i] < 0] = 0

        for i in range(self.resolution):

            if self.x[i][self.m_temp[i]] > 0:
                self.m_temp[i] += 1
            
            self.N[i] = np.sum(self.x[i])


    def update_parms_tot(self):

        self.x_tot = np.zeros(self.m+1)
        self.N_tot = 0

        for i in range(self.resolution):
            self.x_tot += self.x[i]
            self.N_tot += self.N[i] 

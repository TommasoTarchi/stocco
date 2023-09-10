import math
import random



def compute_RW(g, gamma, mu):

    R = math.sqrt((g-gamma)**2 + (2*g+2*gamma+mu)*mu)
    W = g + gamma + mu

    return R, W


def compute_p(R, W, g, gamma):

    pM 
    pE 
    pB = g*pE / gamma
    
    return pM, pE, pB


def extract_time(R, W, g, gamma, n):

    r = random.random()
    ext = bool(r<=((R-W+2*gamma) / (R+W-2*gamma)) ** n)

    if ext:
        part = W - 2 * gamma * math.pow(r, -1/n)  # just to speed up the computation
        t = 1/R * math.log((part-R) / (part+R))
    else:
        part = math.pow(r, 1/n)  # just to speed up the computation
        t = 1/R * math.log((part * (R-W+2*g) - W - R + 2*gamma) / 
                           (part * (-R-W+2*g) - W + R + 2*gamma))

    return ext, t  # ext is a bolean and tells whether the population has gone extinct


def extract_state(pM, pE, pB):
    
    return state


def update_state(state, prop):  # 'prop' stands for 'propensity'
    
    return state

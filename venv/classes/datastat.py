from random import *
import math
#from scipy import stats
import numpy as np


def get_sex():
    is_male= [True, False]
    return choice(is_male)

def get_age():
    MIN_AGE = 18
    MAX_AGE = 65
    """
    Count of candidates by ages (from 18 to 64)
    """
    ages = np.arange(MIN_AGE,MAX_AGE,1)
    _w = []
    for age in ages:
        # distribution func
        #todo: make koef 1.2 dynamic by situation
        _w.append(sum(ages) / math.pow(age, 1.2))
    _w = np.array(_w)
    _w /= _w.sum()
    the_age_sample = np.random.choice(ages,1,p = _w)
    selected_age = the_age_sample[0]
    return selected_age

def get_job_dist():
    numbers = '1,2,3,4,5,6,7,8,9,0'
    weights = np.arange(1, 11, 1.0)
    weights = [1/x for x in weights]
    numbers = numbers.split(',')
    steps = np.arange(2,8)
    steps_w = [1/x for x in steps]
    steps_w /= sum(steps_w)
    weights /= sum(weights)
    steps_count = np.random.choice(steps, 1, p= steps_w)
    steps_count = steps_count[0]
    dist_str_arr = np.random.choice(numbers, steps_count, p = weights)
    dist_str = ''
    step = 0
    for sym in dist_str_arr:
        if (int(sym) < 2) and (step < 2) and (steps_count < 4):
            dist_str += str(randint(2,9))
        else:
            dist_str += sym
        step += 1
    dist = int(dist_str)
    return dist
    # #I don't know, how is it matters to save my distibution in another object
    # #dist_distr = stats.rv_discrete(name='hyperbolic normalized', values=(all_dists,weights))
    # return dist[0]


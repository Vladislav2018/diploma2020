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
    #it was better thanks for @trapwalker from Habr Answers, but not at all
    NEAREST_DIST = 20.0
    FAR_DIST = 1.8*10**7
    all_dists = np.arange(NEAREST_DIST, FAR_DIST, 1.0)
    weights = [1/x for x in all_dists]
    weights = np.array(weights)
    weights /= weights.sum()
    dist = np.random.choice(all_dists,1, p = weights)
    #I don't know, how is it matters to save my distibution in another object
    #dist_distr = stats.rv_discrete(name='hyperbolic normalized', values=(all_dists,weights))
    return dist[0]

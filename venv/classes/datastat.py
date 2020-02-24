from random import *
import math
from scipy import stats
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
    ages = [*range(MIN_AGE, MAX_AGE)]
    _w = []
    for age in ages:
        # distribution func
        #todo: make koef 1.2 dynamic by situation
        _w.append(sum(ages) / math.pow(age, 1.2))

    the_age_sample = choices(ages, weights=_w, k=1)
    selected_age = the_age_sample[0]
    return selected_age

def get_job_dist():
    #it was better thanks for @trapwalker from Habr Answers, but not at all
    #todo: solve it normal way, for example with scipy.stats.rv_discrete
    NEAREST_DIST = 20.0
    FAR_DIST = 1.8*10**7
    all_dists = np.arange(NEAREST_DIST, FAR_DIST, 1.0)
    weights = [1/x for x in all_dists]
    weights = np.array(weights)
    weights /= weights.sum()
    print(weights)
    dist = np.random.choice(all_dists,1, p = weights)
    return dist

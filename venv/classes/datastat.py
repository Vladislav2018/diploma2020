from random import *
import math

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
        _w.append(sum(ages) / math.pow(age, 1.2))

    the_age_sample = choices(ages, weights=_w, k=1)
    selected_age = the_age_sample[0]
    return selected_age

def get_job_dist():
    all_dists = [*range(20,20000000, 20)]
    weights = []
    for dist in all_dists:
        weights.append(1/dist)
    dist = choices(all_dists,weights,k=1)
    dist = dist[0]
    return dist

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
    #it was better thanks for @trapwalker from Habr Answers, but not at all
    #todo: solve it normal way, for example with scipy.stats.rv_discrete
    all_dists = [*range(20,20000000)]
    dist = choices(all_dists, (1/x for x in all_dists))
    return dist

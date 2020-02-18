from random import *
from faker import Faker
from datastat import *

fake = Faker([
    'en_AU',
    'en_CA',
    'en_GB',
    'en_NZ',
    'en_US'
])
class Candidate:

    # the distance that the candidate must overcome in order to be in the workplace
    job_dist = get_job_dist()
    male = get_sex()
    age = get_age()

    def get_bad_habits(is_male, age):
        '''
        :param is_male: self bool
        :param age: self int
        :return: dict {habit:normalised (from 0 to 1) consumer koefficient}
        this function is calculate frequency of personal dependence from bad habits
        '''
        # this will detect candidates absolutely without the bad habit
        habit_exists = [0,1]

        # this parameters are common for consumers and non-consumers yet and non-statistical
        # ToDo: change this params in true statistical and normalize; and create more bad habits
        alco_age_koef = (100-age)/(abs(age - 40)+1)
        smocking_age_koef = age*0.01
        drug_age_koef = 1/age
        #probabilities (random yet)
        alco_weights_exists = [0.2, 0.8]
        smocking_weights_exists = [0.3, 0.7]
        drugs_weights_exists = [0.7, 0.3]
        alcoholic = choices(habit_exists, alco_weights_exists, k = 1)
        alcoholic = alcoholic[0]
        smocker = choices(habit_exists, smocking_weights_exists, k = 1)
        smocker = smocker[0]
        druger = choices(habit_exists, drugs_weights_exists, k = 1)
        druger = druger[0]
        if is_male == True:
            alco_koef = alco_age_koef*random()*0.3*alcoholic
            smocking_koef = smocking_age_koef*random()*0.5*smocker
            drugs_koef = drug_age_koef*random()*0.6*druger
        else:
            alco_koef = alco_age_koef*random()*0.1*alcoholic
            smocking_koef = smocking_age_koef * random() * 0.2*smocker
            drugs_koef = drug_age_koef * random() * 0.45*druger
            #todo: make more kind of subhabits
        bad_habits = {
            'alcohol':{
                'light': alco_koef,
                'heavy': alco_koef
            },
            'smocking':{
                'tabaco': smocking_koef,
                'wape and ikos':smocking_koef
            },
            'drugs':{
                'light':drugs_koef,
                'heavy':drugs_koef,
                'medical': drugs_koef
            }
        }
        return bad_habits

    bad_habits = get_bad_habits(male, age)

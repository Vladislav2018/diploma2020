import sys
from datawriter import *
from classes.candidate import Candidate
from datastat import *

def main():
   #test= Candidate()
   #print(test.job_dist,  test.male, test.age, '\n', test.bad_habits)
   #print(dir((test)))
   #write(test)
   #read('Candidate')
   #print(test)
   for i in range(1000):
    print(str(get_job_dist()) + '\t')

if __name__== "__main__":
  main()
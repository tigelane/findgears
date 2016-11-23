#!/usr/bin/env python
from __future__ import division
from random import randint

'''  This application will find a 3 gear combination that will meet your desired total ratio.'''

#Adjust the following numbers
cogmin = 8
cogmax = 40
desired_ratio = 45
maximum_good_combinations = 30

# This is maximum number of combinations to try before it stops.
maxguess = 9000000
num = 0
numsthatwork = []
matches = 0
print_loop = 0

while num < maxguess and matches < maximum_good_combinations:
    mynums = []
    for a in range (0,6):
        mynums.append(randint(cogmin, cogmax))
    ratio = (mynums[1]/mynums[0])*(mynums[3]/mynums[2])*(mynums[5]/mynums[4])
    # Use the following for 2 gears.
    # ratio = (mynums[1]/mynums[0])*(mynums[3]/mynums[2])
    if ratio == desired_ratio:
        numsthatwork.append(mynums)
        print ("Behold:  {}".format(mynums))
        matches += 1
    num += 1

    # Give a status update on how many combinations we have checked so far.
    print_loop += 1
    rand = randint(115000,221000)
    if print_loop >= rand:
        print ("--Number of combinations checked so far: {0}".format(str(num)))
        print_loop = 0

if matches == 0:
    print ("Oh no..  I didn't find any matches.  Try increasing the number of guesses or broadaning the number of cogs that can be used.")
else:
    print ("\nI tried {0} combinations.  Of that, {1} worked for your desired ratio of {2}.  Please see the following:".format(num, str(len(numsthatwork)), desired_ratio))
    for combo in numsthatwork:
        print (combo)

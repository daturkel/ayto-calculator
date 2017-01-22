#!/usr/bin/env python

from __future__ import division # (python 2 compatibility)
import pandas as pd
from itertools import permutations
import json

# REPLACE s1 WITH s4 TO SWITCH TO SEASON 4
from s1 import guys, girls, truth_booth, mc

pd.set_option('display.expand_frame_repr', False)

# vocab
# pairing: a guy-girl pair, regardless of whether it's correct
# perfect match: a correct guy-girl pair
# guess: a set of ten pairings submitted at the end of the episode

# initialize dataframe with even odds
probability = pd.DataFrame([[10.0]*10 for i in range(10)],columns=girls,index=guys)

# initialize all possible guesses
remaining_guesses = list(permutations(range(0,10)))

# number of possible guesses
num_guesses = len(remaining_guesses)

def num_shared(a,b):
    """ count how many pairings are shared between two guesses
        arguments: two guesses
        return: number of shared pairings """
    return sum([a[i] == b[i] for i in range(10)])

def tally_pairings(remaining_guesses):
    """ record the number of times each pairing occurs throughout all the remaining guesses
        arguments: list of remaining guesses
        return: list of lists of ints tallying the number of times each pairing occurs """
    temp = [[0]*10 for r in range(10)]
    for matchup in remaining_guesses:
        for guy, girl in enumerate(matchup):
            temp[guy][girl] += 1
    return temp

print("{} guesses left\n".format(num_guesses))
print(probability)

# main episode loop
for i in range(10): 
    # eliminate all guesses that don't fit this episode's truth booth result
    remaining_guesses = [guess for guess in remaining_guesses if 
            (guess[truth_booth[i][0]] == truth_booth[i][1]) == truth_booth[i][2]]
    # update the number of guesses remaining
    num_guesses = len(remaining_guesses)
    print("\nEpisode {}, Truth Booth\n{} guess(es) left\n".format(i+1,num_guesses))
    

    temp = tally_pairings(remaining_guesses)
    # copy tallies to dataframe, then normalize into probabilities
    probability = pd.DataFrame(temp,columns=girls,index=guys)
    probability *= 100/num_guesses
    print("Probability %")
    print(probability)
    
    # eliminate all guesses that don't fit this episode's match ceremony
    remaining_guesses = [guess for guess in remaining_guesses if
            num_shared(guess,mc[i][0]) == mc[i][1]]
    # update the number of guesses remaining
    num_guesses = len(remaining_guesses)
    print("\nEpisode {}, Match Ceremony\n{} guess(es) left\n".format(i+1,num_guesses))

    temp = tally_pairings(remaining_guesses)
    # update probability dataframe again
    probability = pd.DataFrame(temp,columns=girls,index=guys)
    probability /= num_guesses/100
    print("Probability %")
    print(probability)




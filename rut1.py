#!/usr/bin/env python

from __future__ import division # (python 2 compatibility)
import pandas as pd
from itertools import permutations
import pickle
import sys
import importlib
from os import listdir
from os.path import isfile, join

# load correct season based on argument
try:
    season = sys.argv[1]
except IndexError:
    raise IndexError("No season argument.\nPlease supply a season as an argument, e.g. ~./rut1.py s4")
try:
    season_data = importlib.import_module(season)
except ImportError:
    seasons = [f for f in listdir(".") if isfile(join(".",f)) and f[-3:] == ".py" and join(".",f) != sys.argv[0]]
    seasons = ", ".join([f[:-3] for f in seasons]) + "."
    raise ImportError("There is no season: {}.\nTry one of the following: {}".format(season,seasons))
guys = season_data.guys
girls = season_data.girls
truth_booth = season_data.truth_booth
mc = season_data.mc

pd.set_option('display.expand_frame_repr', False)

# vocab
# pairing: a guy-girl pair, regardless of whether it's correct
# perfect match: a correct guy-girl pair
# guess: a set of ten pairings submitted at the end of the episode

length = len(guys)

def num_shared(a,b):
    """ count how many pairings are shared between two guesses
        arguments: two guesses
        return: number of shared pairings """
    return sum([a[i] == b[i] for i in range(length)])

def tally_pairings(remaining_guesses):
    """ record the number of times each pairing occurs throughout all the remaining guesses
        arguments: list of remaining guesses
        return: list of lists of ints tallying the number of times each pairing occurs """
    temp = [[0]*length for r in range(length)]
    for matchup in remaining_guesses:
        for guy, girl in enumerate(matchup):
            temp[guy][girl] += 1
    return temp

try:
    with open("{}.pickle".format(season),"rb") as f:
        data = pickle.load(f)
        resume = data["resume"]
        remaining_guesses = data["remaining_guesses"]
        num_guesses = len(remaining_guesses)
        # re-initialize dataframe
        probability = pd.DataFrame(tally_pairings(remaining_guesses),columns=girls,index=guys)
        probability /= num_guesses/100
except (OSError, IOError) as e:
    # initialize all possible guesses
    remaining_guesses = list(permutations(range(0,length)))
    # number of possible guesses
    num_guesses = len(remaining_guesses)
    resume = -1 
    # initialize dataframe with even odds
    probability = pd.DataFrame([[100.0/length]*length for i in range(length)],columns=girls,index=guys)

print("{} guess(es) left\n".format(num_guesses))
print("Probability %")
print(probability)

# main episode loop
for i in range(resume + 1,len(mc)): 
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

resume = len(mc) - 1
with open("{}.pickle".format(season), "wb") as f:
    pickle.dump({"resume": resume, "remaining_guesses": remaining_guesses}, f)
with open("data.pickle".format(season), "wb") as g:
    pickle.dump(probability,g)

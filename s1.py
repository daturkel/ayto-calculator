# list of the guys' names, in alphabetical order
guys = ["Adam",    #0
        "Chris S.",#1
        "Chris T.",#2
        "Dillan",  #3 
        "Dre",     #4
        "Ethan",   #5
        "John",    #6
        "Joey",    #7
        "Ryan",    #8
        "Wes"]     #9

# list of the girls' names, in alphabetical order
girls = ["Amber",   #0
         "Ashleigh",#1
         "Brittany",#2
         "Coleysia",#3
         "Jacy",    #4
         "Jessica", #5
         "Kayla",   #6
         "Paige",   #7
         "Shanley", #8
         "Simone"]  #9

# each truth booth revelation
# [guy_index, girl_index, perfect_match?]
truth_booth = [[2,8,False],
               [5,5,False],
               [6,9,False],
               [3,5,False],
               [4,1,False],
               [2,7,True],
               [2,7,True], # ep 7 had no truth booth, so duplicating ep 6 here
               [8,6,False],
               [9,6,True],
               [6,4,False]]

# each matching ceremony guess and number of resultant beams
# [[guy_0_girl, guy_1_girl, ... guy_8_girl, guy_9_girl], number_correct]
mc = [[[2,1,5,3,4,8,9,7,0,6],2],
       [[8,9,7,5,1,0,4,2,6,3],4],
       [[2,7,9,3,1,0,5,8,6,4],2],
       [[0,7,1,3,9,6,8,4,2,5],2],
       [[8,9,7,3,2,0,4,5,1,6],5],
       [[8,9,7,3,2,0,4,5,1,6],5], # ep 6 had no matchup ceremony, so duplicating ep 5 here
       [[1,2,7,3,8,0,4,9,5,6],5],
       [[8,4,7,3,9,0,2,5,1,6],7],
       [[8,1,7,3,9,0,4,2,5,6],8],
       [[8,4,7,3,9,0,1,2,5,6],10]]


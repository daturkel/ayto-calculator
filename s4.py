# list of the guys' names, in alphabetical order
guys = ["Asaf",    #0
        "Cam",     #1
        "Cameron", #2
        "Giovanni",#3 
        "John",    #4
        "Morgan",  #5
        "Prosper", #6
        "Sam",     #7
        "Stephen", #8
        "Tyler"]   #9

# list of the girls' names, in alphabetical order
girls = ["Alyssa",   #0
         "Camille",  #1
         "Emma",     #2
         "Francesca",#3
         "Julia",    #4
         "Kaylen",   #5
         "Mikala",   #6
         "Nicole",   #7
         "Tori",     #8
         "Victoria"] #9

# each truth booth revelation
# [guy_index, girl_index, perfect_match?]
truth_booth = [[6,8,False],
               [4,4,False],
               [2,6,True],
               [0,8,False],
               [3,5,False],
               [7,0,True],
               [1,9,False],
               [3,4,False],
               [6,2,True],
               [1,4,True]]

# each matching ceremony guess and number of resultant beams
# [[guy_0_girl, guy_1_girl, ... guy_8_girl, guy_9_girl], number_correct]
mc = [[[3,9,6,5,2,4,1,0,7,8],3],
       [[1,4,6,5,7,0,2,3,8,9],3],
       [[1,7,6,5,9,3,2,0,8,4],4],
       [[1,2,6,5,9,8,7,0,4,3],4],
       [[1,2,6,3,8,4,9,0,7,5],4],
       [[1,9,6,3,2,8,5,0,4,7],4],
       [[3,7,6,2,5,8,9,0,4,1],4],
       [[1,8,6,7,5,9,3,0,4,2],2],
       [[8,7,6,3,9,4,2,0,5,1],6],
       [[5,4,6,3,9,8,2,0,7,1],10]]

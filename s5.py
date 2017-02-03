# list of the guys' names, in alphabetical order
guys = ["Andre",    #0
        "Derrick",  #1
        "Edward",   #2
        "Hayden",   #3 
        "Jaylan",   #4
        "Joey",     #5
        "Michael",  #6
        "Mike",     #7
        "Osvaldo",  #8
        "Ozzy",     #9
        "Tyler"]    #10

# list of the girls' names, in alphabetical order
girls = ["Alicia",   #0
         "Carolina", #1
         "Cas",      #2
         "Gianna",   #3
         "Hannah",   #4
         "Kam",      #5
         "Kari",     #6
         "Kathryn",  #7
         "Shannon",  #8
         "Taylor",   #9
         "Tyranny",] #10

# each truth booth revelation
# [guy_index, girl_index, perfect_match?]
truth_booth = [[3,3,False],
               [0,0,False],
               [9,1,False],
               [8,10,False]]

# each matching ceremony guess and number of resultant beams
# [[guy_0_girl, guy_1_girl, ... guy_8_girl, guy_9_girl], number_correct]
mc = [[[0,7,5,8,2,1,4,6,10,3,9],2],
      [[4,0,8,9,5,1,3,2,6,7,10],0],
      [[6,4,5,1,2,7,9,0,10,3,8],4],
      [[2,3,0,1,10,7,6,5,9,4,8],4]]

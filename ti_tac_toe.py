#Jhamni Young-Shinnick
# September 1st,2017
#tic_tac_toe.py
#Runs a game of tic-tac-toe
def play():    #is Functioon
#type play() in console to begin     
    consent = raw_input("Do you want to play Tic-Tac-Toe? ")
    if "n" in consent:
        print "Thank you! Have a nice day!"
    if "y" in consent:              
#y = yes, n = no
        p1= raw_input("Player 1, Would you like to be x or o? ")
        p1 == "x" or "o"
        if p1 == "x":
                p2 = "o"
        elif p1 == "o":
                p2 = "x"
#choose position
        print "p1: " + p1
        print "p2: " + p2 
        print "  a   b   c "
        print "1   |   |   "
        print " --- --- ---"
        print "2   |   |   "
        print " --- --- ---"
        print "3   |   |   "
        begin = "Let's play Tic-Tac-Toe!"
        print begin
# Displays board and position     
        p1mv = raw_input("Player 1, what is your move?")
        if "a1" or "1a" in p1mv: 
            print "  a   b   c "
            print "1 " + p1 + " |   |   "
            print " --- --- ---"
            print "2   |   |   "
            print " --- --- ---"
            print "3   |   |   "   

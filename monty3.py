# Simulate playing n (user input) games of the Monty Hall problem
# Generate random number for door behind which real prize is and another random number for door selected by the contestant
#
# Function for when contestant always changes doors and when they never change
# Both these functions return True if contestant wins; return False if contestant loses
#
# Calculate the fraction of times the contestant wins for both - always switching and never switching
#
# Priyanka Puthran, MHI 289I, Winter 2018
#

import random
import sys

#
# Function to pick a door
# returns: integer out of (1, 2 or 3) randomly
#
def getrandom():
    return random.randint(1,3)

#
# Function to randomly generate the prize door
#
def prizedoor():
    p_door = getrandom()
    return p_door

#
# Function to randomly generate the contestant's first choice of door
#
def contestantdoor():   
    c_door = getrandom()
    return c_door

#
# Contestant always switches his choice after Monty opens the remaining door
#
def montyalways():
    x = contestantdoor()
    y = prizedoor()
    if x == y:  # If contestant always switches
        return False # Contestant loses
    else:
        return True # Contestant wins

#
# Contestant never switches his choice after Monty opens the remaining door
#
def montynever():
    x = contestantdoor()
    y = prizedoor()
    if x == y:  # If contestant never switches
        return True # Contestant wins
    else:
        return False # Contestant loses

#
# Function to read and vet user selection
# Returns: n, number of games
# NOTE: n must be greater than 0, return -1 to quit
#
def getinput():
    # Loop to get good output
    while True:
        try:
            # get input from user and check type
            n = int(raw_input("Number of games to play: "))
        except EOFError:    # user wants to quit, so help
            n = -1
            sys.exit([0])
        except ValueError:  # user did not enter a number
            n = -1
            print "Please enter a positive integer"
            sys.exit([0])
        # got an integer
        # now check the value we read/were given
        if n > 0:
            break
        # this is bad input, so say so
        else:
            print "Please enter a positive integer"
            sys.exit([0])

    # it's positive to continue, -1 to quit
    return n
  
#
# main routine : Let's play the game!!!
#
# Get number of games from user
n = getinput()

# Initialize variable for wins on switching choice    
wins_on_switch = 0

#Initialize variable for wins on not switching choice
wins_on_stay = 0

# Run the game for number of times that user inputs
# Switch and no switch every time
for i in range(n):
    montyalways()   # One set of games when contestant always switches the door
    if montyalways() == True:   # If contestant wins after switching, increment wins
        wins_on_switch += 1
    montynever()   # One set of games when contestant never switches the door
    if montynever() == True:    #If contestant wins after staying with first choice, increment wins
        wins_on_stay += 1    

#
# Print out the result
#
print "Out of",n,"games:"
print "Always switching wins:", '%.7f' % (wins_on_switch/float(n)),"(\r",wins_on_switch, "games)"
print "Never switching wins:", '%.7f' % (wins_on_stay/float(n)),"(\r",wins_on_stay, "games)"

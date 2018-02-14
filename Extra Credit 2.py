# Module for generating the collatz conjecture
#
# Take input from user
# Print the collatz sequence for the number and the stopping time(least number of iterations to reach 1)
#
# Priyanka Puthran, MHI 289I, Winter 2018
#

import sys

#
# Function to generate the collatz sequence for any number
# Returns: n/2 if number is even;
#          3*n + 1 if number is odd
#
def collatz(n):
    if n%2 == 0:    # if number is even
        return n/2
    else:           # if number is odd
        return 3*n + 1

#
# Function to take input number from the user
#
def getinput():
    # Loop to get good output
    while True:
        try:
            # get input from user and check type
            n = int(raw_input("Enter a positive integer greater than 1: "))
        except EOFError:    # user wants to quit, so help
            sys.exit([0])
        except ValueError:  # user did not enter a number
            n = -1
            print "Please enter a positive integer greater than 1"
            continue
        # got an integer
        # now check the value we read/were given
        if n > 1:
            break
        # this is bad input, so say so
        else:
            print "Please enter a positive integer greater than 1"

    # it's positive to continue, -1 to quit
    return n

#
# main routine
#
# Get input number from user
n = getinput()

# Initiate variable for stopping time
counter = 0

# Print the input number first in the collatz sequence
print n,

# Generate the collatz sequence
n_seq = n
while n_seq != 1:   # Loop till sequence reaches 1
    n_seq = collatz(int(n_seq))
    print n_seq,
    counter += 1    # Increment iterations to get the stopping time

# Print the result
print "\nThe total stopping time for",n, "is",counter










# Program to compute average, standard deviation, maximum and minimum difference
# between air inspired and expired for each breath
#
# Function to calculate average of a list of numbers
# Another function to calculate the standard deviation of a list of numbers
#
# Priyanka Puthran, MHI 289I, Winter 2018
#

import math

#
# Function to calculate the average of a list of numbers
#
def mean(L):
    S = 0
    for i in range(len(L)):
        S += L[i]
    return (S / len(L))

#
# Function to calculate the standard deviation of a list of numbers
#
def stddev(L):
    S = 0
    mn = mean(L)
    for i in range(len(L)):
        S += (L[i] - mn) ** 2
    return math.sqrt(S / len(L))

#
# Main function to read file and print out results
#
def main():
    # Read the input file and convert it into a list.
    # Values on each file line are split by whitespace and make up for one row in the list
    inputfile = open('C:\Users\pripu\Downloads\data_hw_3','r')
    lst = []
    for line in inputfile:
        lst.append([x for x in line.split(' ')])

    # Split the list into 3 different lists for Breath Number, Air Inspired and Air Expired
    # Also convert string values in each list to floating point numbers
    BN = [float(x[0]) for x in lst]
    insair = [float(x[1]) for x in lst]
    expair = [float(x[2]) for x in lst]

    # Calculate difference between inspired air and expired air at each breath and store in new list
    diff = [insair[i]-expair[i] for i in xrange(min(len(insair), len(expair)))]
    # Take the absolute of all values in list and store it back
    diff = map(abs,diff)


    print 'Average volume of air inspired is' , "%.2f" % mean(insair), 'ml with a standard deviation of', "%.2f" %  stddev(insair)
    print 'Average volume of air expired is' , "%.2f" % mean(expair), 'ml with a standard deviation of', "%.2f" % stddev(expair)
    print 'The maximum difference between air inspired and expired is', "%d" % max(diff)
    print 'The minimum difference between air inspired and expired is', "%d" % min(diff)

main()

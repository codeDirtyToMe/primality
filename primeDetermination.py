#!/usr/bin/python3.5
#Primality testing.
#Take the square root of the number in question. The floor of the result
#is the ceiling of the numbers to divide by. In other words, start the
#loop at the math.floor(math.sqrt(num)).
#codeDirtyToMe

##Updates
#January 4, 2018
#   -No prompt for a user is really necessary here so it was removed.
#   -It now runs through a range of numbers and keeps prime and non-prime numbers in their
#    own list for output at the end of the program.
#   -Added a bunch of comments so that I don't forget what the hell I've been doing.

#To do:
#       1: Compare the first 100k prime numbers a list of confirmed prime numbers in order to
#          check the validity of the program.
#       2: Add multi-threading for crunching really large numbers.
#           -Will I have to have threads leap frog each other? This should be fun.
#       3: Possibly implement this as a function into my polymorphic cipher that I haven't
#          worked on in a couple months.

import math

num = 1 #Start at this number. Change if desired.
nonPrimeNumbers = []
primeNumbers = []

for s in range(10000) : #How many numbers to check the primality of.
    # Set the ceiling of the numbers to check based on the floor of the sqrt of the num value.
    ceiling = math.floor(math.sqrt(num))
    while ceiling >= 1 :
        remainder = num % ceiling #Check for remainder.
        if remainder == 0 : #No remainder.
            if ceiling == 1 : #Is divisible by 1.
                #num is prime because it wouldn't get to a ceiling value of 1 unless it wasn't divisible by any thing larger.
                primeNumbers.append(str(num))
                ceiling = 0 #Set ceiling to a value that will break the while loop.
            else :
                nonPrimeNumbers.append(str(num))
                ceiling = 0 ##Set ceiling to a value that will break the while loop.
        else :
            # If a remainder other than zero is present after modulo division, divide num by the next lower ceiling value.
            ceiling -= 1
            continue
    s += 1 #Increase the for loop counter.
    num += 1 #Test the next number in the range.

#Print out the results.
print("Not Prime: " + ",".join(nonPrimeNumbers))
print("Prime: " + ",".join(primeNumbers))
exit(0)

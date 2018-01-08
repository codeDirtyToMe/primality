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

#January 6-7, 2018
#   -Started getting the multi-threading ready.
#   -Timed the execution w/o threading for numbers 1-100,000. It took 3.66715407371521 seconds.
#   -Hopefully, after implementing at least two threads I'll see a shorter time.
#   -Ability to write primes to a file for comparison was added.
#   -After outputting primes to file, I ran "$diff primeNumbers.txt confirmedPrimes.txt -wq" and
#       confirmed that they are in fact equivalent.
#   -Instead of implementing threads, I started working on performance improvements.
#       Eliminated the need to check even numbers. Execution time was 1.0901169776916504 seconds.
#       This is a difference of 2.577037096 seconds.

#To do:
#       1: (DONE) Compare the first 100k prime numbers a list of confirmed prime numbers in order to
#          check the validity of the program. $>diff file1 file2
#       2: (STARTED) Add multi-threading for crunching really large numbers.
#          Will I have to have threads leap frog each other? This should be fun.
#       3: Possibly implement this as a function into my polymorphic cipher that I haven't
#          worked on in a couple months.

import math, time, os, threading

def primeCruncher(num, endNum):
    nonPrimeNumbers = []
    primeNumbers = []
    # Let's time this as a single thread.
    s = 1
    while s <= endNum : #How many numbers to check the primality of. Divided by 2 for multiple threads.
        # Set the ceiling of the numbers to check based on the floor of the sqrt of the num value.
        ceiling = math.floor(math.sqrt(num))
        while ceiling >= 1 :
            remainder = num % ceiling #Check for remainder.
            if remainder == 0 : #No remainder.
                if ceiling == 1 : #Is divisible by 1.
                    #num is prime because it wouldn't get to a ceiling of 1 unless it wasn't divisible by anything larger.
                    primeNumbers.append(str(num))
                    ceiling = 0 #Set ceiling to a value that will break the while loop.
                else :
                    nonPrimeNumbers.append(str(num))
                    ceiling = 0 ##Set ceiling to a value that will break the while loop.
            else :
                # If a remainder other than zero is present after modulo division, divide num by the next lower ceiling value.
                ceiling -= 1
                continue
        s += 2 #Increase the for loop counter.
        if (num == 2) or (num % 2 == 0) :
            num += 1 #There's no point in checking even numbers other than 2.
        else :
            num += 2 #If odd, try the next odd number.

    return primeNumbers
#Main###################################################################################################################
#Spool up some threads.
#evenThread = threading.Thread(target = primeCruncher, args = [num])
#oddThread = threading.Thread(target = primeCruncher, args = [num + 1])

num = 2       #Start at this number. Change if desired.
endNum = 100000  #End at this number. Change if desired.

primeValues = []
startTime = time.time()  # Start time recorded.
primeValues = primeCruncher(num, endNum)
stopTime = time.time()
totalTime = stopTime - startTime

print("Execution took: " + str(totalTime) + str(" seconds."))
print("Formatting found primes for file comparision...")

#Format results to match the list  of confirmed prime numbers. I suppose I could do this easier in the loop above.
#However, I suspect that would hinder the performance; not that I'm all that worried about that until I start
#the multi-threading. Whatever, we'll make it a learning experience. That and I actually enjoy doing this stuff.
#10 across. \t between each. last value ends with \n.

#Open the file to output the data to, or create the file if it doesn't already exist.
if os.path.exists("primeNumbers.txt"):
    primeFile = open("/home/malmach/PycharmProjects/primeNumbers/primeNumbers.txt", "w")
else :
    primeFile = open("primeNumbers.txt", "w")

#Set up some counters.
a = 0
b = 0
#Start adding tabs and newline feeds.
while a <= math.ceil(endNum / 10) : #Essentially, how many lines are there?
    if len(primeValues[b:]) >= 10 : #If there are currently more than ten left.
        primeFile.write("\t".join(primeValues[b:b + 10]) + "\n")
    elif (len(primeValues[b:]) < 10) and (len(primeValues[b:]) > 0) : #If there are < 10 && > 0 values left.
        primeFile.write("\t".join(primeValues[b:]) + "\n")
    else :
        break #No values left, break the loop.

    b += 10 #Shift 10 indices to the right.
    a += 1  #Next line.

primeFile.close()
print("Now, if one were to \"$diff confirmedPrimes.txt primeNumbers.txt -wq\", one should see no return. This means\ "
      "that there is a reasonable chance that this program is working as intended.")

exit(0)

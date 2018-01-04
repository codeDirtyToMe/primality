#!/usr/bin/python3.5
#Primality application.
#Take the square root of the number in question. The floor of the result
#is the ceiling of the numbers to divide by. In other words, start the
#loop at the math.floor(math.sqrt(num)).
#A basic

import math

num = int(input("Number in question: "))
ceiling = math.floor(math.sqrt(num))

for x in range(ceiling) :
    if x % 100 == 0 :
        print(x)
    val = num % ceiling
    if val == 0 :
        if ceiling == 1 :
            print("The number is prime.")
            exit(0)
        else :
            print("The number is NOT prime.")
            exit(0)
    else :
        x += 1
        ceiling -= 1
        continue

exit(0)
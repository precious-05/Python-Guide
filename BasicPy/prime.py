#prime number having only 2 factors or which is divisibly by 1 and by itself only
#In even numbers prime number is 2 only all other even no are not prime
# all odd numbers are prime except 1
from math import sqrt

def is_prime(number):
    if number <= 1:
        return False  # Numbers less than or equal to 1 are not prime
    # Loop to check for factors from 2 to the square root of n
    for i in range(2, int(sqrt(number)) + 1,1):
        # Check if n is divisible by i
        if number % i == 0:
            return False  # If n is divisible by 2, it is not prime
    return True  # If no divisors are found, n is prime

def last_prime():
    # Loop to find the last prime number
    count = 0
    number = 2
    primes = []
    
    while count < 450:
        if is_prime(number):
            #print(number) 
            primes.append(number)
            count = count+1
            
            if count % 50 == 0:
                c

        number = number+1
    
    print(f"Finally! The 450 prime numbers found")

last_prime()





"""
We iterate the loop up to the square root of the number because if a number is not prime, 
at least one of its factors will be less than or equal to its square root. 
or if it is prime it is confirm that it has only 2 factors
This allows us to efficiently check for factors without needing to check all numbers up to the number itself

Examples to understand are given in Example pdf
"""
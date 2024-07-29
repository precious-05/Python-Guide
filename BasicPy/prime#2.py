"""The second problem is built on the foundation of the first problem. 
It was established that the sum of the logarithms of prime numbers between 
2 and n will converge on the value of n. For example, the sum of the logarithms of all prime
numbers between 2 and 5000 is approximately 4912. The sum of the logarithms of all prime numbers between 2
and 50,000 is approximately 49,732. The problem is that some may contest that this is a valid theory.
To solve this problem, write a program that evaluates the numbers between 2 and n to determine if the number is
a prime number. If it is, find the logarithm of the prime number. Add all logarithms of the prime numbers between
2 and n. After iterating over the values between 2 and n, print out the sum, the number n, and the ratio of these 
two quantities. The ratio of the sum and n should converge on the number one. Evaluate the results with multiple
values for n to demonstrate this convergence. To use the Python function log(), add from math import * to the script
 file immediately following the block comments that include the task name, task purpose, date, and your name at the 
top of the script file. """

from math import sqrt, log

def is_prime(number):
    if number <= 1:
        return False  # Numbers less than or equal to 1 are not prime
    # Loop to check for factors from 2 to the square root of n
    for i in range(2, int(sqrt(number)) + 1):
        # Check if n is divisible by i
        if number % i == 0:
            return False  # If n is divisible by 2, it is not prime
    return True  # If no divisors are found, n is prime

def sum_of_log_primes(n):
    sum_logs = 0.0
    prime_count = 0
    number = 2
    
    while number <= n:
        if is_prime(number):
            sum_logs += log(number)
            prime_count += 1
        number += 1
    
    return sum_logs, prime_count

# Example usage:
n_values = [5000, 10000, 20000, 50000]
for n in n_values:
    sum_logs, prime_count = sum_of_log_primes(n)
    ratio = sum_logs / n
    print(f"For n = {n}:")
    print(f"Sum of logarithms of primes up to {n} is approximately {sum_logs:.2f}")
    print(f"Ratio of sum to n is approximately {ratio:.4f}")
    print()

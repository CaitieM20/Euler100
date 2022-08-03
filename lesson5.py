import math
from multiprocessing.sharedctypes import Value
import lesson3
# Project Euler: Problem 5: Smallest multiple
# 2520 is the smallest number that can be divided by each of the
# numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by
# all of the numbers from 1 to n?

def smallest_multiple(n): 

    # n = 1 -> 1, primes = 1
    # n = 2 -> 2, primes = 2 * 1
    # n = 3 -> 6, primes = 3 * 2 * 1
    # n = 4 -> 12, primes = 3 * 2(2) * 1
    # n = 5 -> 60, primes = 5 * 3 * 2(2) * 1
    # n = 6 -> 60, no new primes
    # n = 7 -> 420, primes = 7 * 5 * 3 * 2(2) * 1
    # n = 8 -> 840, primes = 7 * 5 * 3 * 3(2) * 1

    primeFactorDict = {}
    smallest_multiple_primes(n, {})

    returnVal = 1
    for prime in primeFactorDict:
        returnVal = (prime**primeFactorDict[prime]) * returnVal

    return returnVal

def smallest_multiple_primes(n, primeFactorDict):

    if (n < 1):
        return Exception("n must be greater than 0")

    if (n == 1):
       primeFactorDict[1] = 1
       return

    smallest_multiple_primes

    prime_factors = lesson3.compute_prime_factors(n,n, [1])

    
    
    # if (n == 3):
    #     return {1:1, 2:1, 3:1}

    # if (n == 4):
    #     return {1:1, 2:2, 3:1}

    
    # if n is prime multiple by smallest_multiple(n-1)
    # if n has prime factors check if we'e accounted for them in smallest_multiple(n-1)
    # if not multiply by missing prime factors. 
 
    # dictionary of primes to instances of primes in current computation
    dict = {}
    



smallest_multiple(4)





import math
#Lesson Three
#Largest Prime Factor
#The prime factors of 13195 are 5, 7, 13, 29
#What is the largest prime factor of the given number?

def largest_prime_factor(number_to_factor):
    prime_factors = compute_prime_factors(number_to_factor, number_to_factor, [1])
    print(prime_factors)
    return prime_factors[len(prime_factors)-1]

def compute_prime_factors(number_to_factor, current_factor, prime_factors):
    curr_prime = compute_next_prime(prime_factors[len(prime_factors)-1])

    # once while loop exists we know we have found a new prime factor
    while(current_factor % curr_prime != 0):
        curr_prime = compute_next_prime(curr_prime)
    
    prime_factors.append(curr_prime)
    factor = current_factor / curr_prime
    
    # if the factor that is returned is a smaller prime then we are done.
    if(prime_factors.__contains__(factor)):
        return prime_factors

    # if the product of all the prime factors equals the number we are 
    # factoring then we are done.
    product = 1
    for prime in prime_factors:
        product = product * prime

    if(product == number_to_factor):
        return prime_factors

    # otherwise we need to keep factoring
    return compute_prime_factors(number_to_factor, factor, prime_factors)

def compute_next_prime(current_prime):   
    if(current_prime < 1):
        raise Exception("Argument Error: current_prime must be greater than or equal to 1.")

    if(current_prime == 1):
        return 2

    if(current_prime == 2):
        return 3
    
    # all primes are odd numbers, threfore we can start our search for the next prime
    # by adding two to the current_prime.  Adding one would result in an even number
    # which is not prime.
    next_prime = current_prime + 2
    while (is_prime(next_prime) == False):
        next_prime = next_prime + 1

    return next_prime

# returns true if the number is prime, false otherwise
def is_prime(number):
    current_divisor = 2
    
    # if a number has one or more factors,
    # one will be encountered before the square root of that number
    # so we can shrink the divisor search space by taking the square
    # root of the number.  
    while current_divisor < math.sqrt(number):
        if number % current_divisor == 0:
            return False
        current_divisor = current_divisor + 1

    return True

# print(f"Largest Prime {largest_prime_factor(600851475143)}")
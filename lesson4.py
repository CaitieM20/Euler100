import math
# Project Euler: Problem 4: Largest palindrome product
# A palindromic number reads the same both ways. The 
# largest palindrome made from the product of two 2-digit
#  numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two
#  n-digit numbers.

def larget_palindrome_product(num_digits):
    maxFactorStr = ""

    for x in list(range(num_digits)):
        maxFactorStr = maxFactorStr + "9"

    maxFactor = int(maxFactorStr)
    # This loop needs to change to go through factors as
    # 999 * 999, a=0, b=0
    # 999 * 998, a=0, b=1
    # 998 * 998, a=1, b=1,
    # 999 * 997, a=0, b=2,
    # 998 * 997, a=1, b=2
    # 997 * 997, a=2, b=2

    palindromes = []

    a = 0 
    b = 0
    while (b < maxFactor):
        while (a <= b):
            factorA = maxFactor - a
            factorB = maxFactor - b
            product = factorA * factorB

            if(is_palindrome(str(product)) == True):
                palindromes.append(product)

            a = a + 1
        b = b + 1
        a = 0

    maxPalindrome = 0
    for p in palindromes:
        if p > maxPalindrome:
            maxPalindrome = p
    
    return maxPalindrome

def is_palindrome(number):
    index = 0

    while index < (len(number)-1)/2:
        charFront = number[index]
        charBack = number[len(number)-index-1]

        if(charFront != charBack):
            return False

        index = index + 1
    
    return True

print(larget_palindrome_product(4))

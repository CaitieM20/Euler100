#Euler100 - Lesson One
#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
#The sum of these multiples is 23.  Find the sum of all the multiples of 3 or 5 below the
#provided parameter value number.

def sum_multiples_of_three_and_five (starting_num):
    curr_num = starting_num - 1
    sum = 0

    while curr_num > 0: 
        is_multiple_of_five = (curr_num % 5) == 0
        is_multiple_of_three = (curr_num % 3 ) == 0
        is_multiple_of_three_or_five = is_multiple_of_five or is_multiple_of_three
    
        if(is_multiple_of_three_or_five):
            sum = sum + curr_num

        curr_num = curr_num - 1

    return sum


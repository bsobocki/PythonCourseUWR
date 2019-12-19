import math
from functools import reduce

def isPrime_imper(number):
    for i in range(2, math.floor(math.sqrt(number))+1):
        if number % i == 0:
            return False
    return True

def isPrime_fold(number):
    return all([number%x!=0 for x in range(2, math.floor(math.sqrt(number))+1)])

def isPrime_func(number):
    return reduce(lambda x, y: x and y, (number%x!=0 for x in range(2, math.floor(math.sqrt(number))+2)))

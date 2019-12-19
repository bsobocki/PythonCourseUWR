import timeit
from primes import *

def prime_imper(n):
    result = []
    for i in range(2, n):
        if isPrime_imper(i):
            result.append(i)
    return result

def prime_fold(n):
    return [x for x in list(range(2, n)) if isPrime_fold(x)]

def prime_fun(n):
    return list(filter(lambda x : isPrime_func(x), list(range(2, n))))

imperative = """

def isPrime_imper(number):
    for i in range(2, math.floor(math.sqrt(number))+1):
        if number % i == 0:
            return False
    return True

def prime_imper(n):
    result = []
    for i in range(2, n):
        if isPrime_imper(i):
            result.append(i)
    return result
prime_imper(20) 
"""

folded = """

def isPrime_fold(number):
    return all([number%x!=0 for x in range(2, math.floor(math.sqrt(number))+1)])

def prime_fold(n):
    return [x for x in list(range(2, n)) if isPrime_fold(x)]
prime_fold(20) 
"""

functional = """

def isPrime_func(number):
    return reduce(lambda x, y: x and y, 
                (number%x!=0 for x in range(2, math.floor(math.sqrt(number))+2)))

def prime_fun(n):
    return list(filter(lambda x : isPrime_func(x), list(range(2, n))))
prime_fun(20) 
"""

m_setup = """
import math
from functools import reduce
"""


print ('imper :',timeit.timeit(setup = m_setup, 
                    stmt = imperative, 
                    number = 10000) )
print ('folded :',timeit.timeit(setup = m_setup, 
                    stmt = folded, 
                    number = 10000) )
print ('functional :',timeit.timeit(setup = m_setup, 
                    stmt = functional, 
                    number = 10000) )

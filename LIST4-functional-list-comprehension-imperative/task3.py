import timeit 

setup = """
import math
from functools import reduce

"""
program = """

def isPrime_imper(number):
    for i in range(2, math.floor(math.sqrt(number))+1):
        if number % i == 0:
            return False
    return True

def isPrime_fold(number):
    return all([number%x!=0 for x in range(2, math.floor(math.sqrt(number))+1)])

def isPrime_func(number):
    return reduce(lambda x, y: x and y, (number%x!=0 for x in range(2, math.floor(math.sqrt(number))+2)))

# prime factor distribution - pfd

def distribution_a_by_b(a, b):
    count = 0
    while a % b == 0:
        a /= b
        count += 1
    return (b, count)

def distr_a_b_fold(a, b):
    pass

def distr_a_b_func(a, b):
    passs

def pfd_imper(n):
    result_list = []
    b = 1
    while n != 1:
        count = 0
        b += 1
        if n%b==0:
            while n % b == 0:
                n /= b
                count += 1
            result_list.append((b, count)) 
    return result_list

def pfd_imper2(n):
    result_list = []
    for i in range(2, math.floor(math.sqrt(n))+1):
        if n% i ==0 and isPrime_imper(i):
            result_list.append(distribution_a_by_b(n,i))
    return result_list

def pfd_fold(n):
    prime_divisors = [x for x in range(2, math.floor(math.sqrt(n))+1) if n%x==0 and isPrime_fold(x)]
    return [distribution_a_by_b(n, x) for x in prime_divisors]

def pfd_func(n):
    prime_dividors = filter(lambda x : n%x == 0 and isPrime_func(x), range(2, math.floor(math.sqrt(n))+1))
    return list(map(lambda x : distribution_a_by_b(n, x), prime_dividors))

big_number = 2**4 * 3**3 * 5**5 * 7**2 * 11**2

"""

imperative1 = """pfd_imper(big_number)"""

imperative2 = """pfd_imper2(big_number)"""

folded = """pfd_fold(big_number)"""

functional = """pfd_func(big_number)"""


print ("the best way : " ,
            timeit.timeit(setup = setup, 
            stmt = program+imperative1, 
            number = 100) )
print ("imperative :",
            timeit.timeit(
            setup = setup, 
            stmt = program+imperative2, 
            number = 100) )
print ("folded : ",
            timeit.timeit(setup = setup, 
            stmt = program+folded, 
            number = 100) )
print ("functional : ",
            timeit.timeit(setup = setup, 
            stmt = program+functional, 
            number = 100) )
import timeit

m_setup = """
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

def prime_generator(n):
    gen = (x for x in list(range(2, n)) if isPrime_fold(x))
    return [x for x in gen]

class iterPrime:
    def __init__(self, n):
        self.current = 2
        self.count = 0
        self.max = n

    def __iter__(self):
        return self
    
    def __next__(self):
        x = self.current
        self.count += 1
        if self.count <= self.max:
            while not isPrime_imper(x):
                x+=1
            self.current = x
        else:
            raise StopIteration

def prime_iter(n):
    primes = iterPrime(n)
    return [x for x in primes]

"""

def print_table(n):
    imperative = """prime_imper("""+str(n)+""")"""
    folded = """prime_fold("""+str(n)+""")"""
    functional = """prime_fun("""+str(n)+""")"""
    generator = """prime_generator("""+str(n)+""")"""
    iterator = """prime_iter("""+str(n)+""")"""

    imper = "{:.4f}".format(timeit.timeit(setup = m_setup, 
                        stmt = program+imperative, 
                        number = 1000) )
    fold = "{:.4f}".format(timeit.timeit(setup = m_setup, 
                        stmt = program+folded, 
                        number = 1000) )
    func = "{:.4f}".format(timeit.timeit(setup = m_setup, 
                        stmt = program+functional, 
                        number = 1000) )
    gener = "{:.4f}".format(timeit.timeit(setup = m_setup, 
                        stmt = program+generator, 
                        number = 1000) )
    iterator = "{:.4f}".format(timeit.timeit(setup = m_setup, 
                        stmt = program+iterator, 
                        number = 1000) )

    print(n,'\t|',imper,'\t|',fold,'\t|',func,'\t|',gener,'\t|',iterator,'\t|')


print('\n\t|  prime_?..?(n) -> list(n first prime numbers) |\t')
print('-----------------------------------------------------------------------------------------')
print('    n   |  imper\t|  fold  \t|  func  \t|  generator \t|  iter \t|')
print('-----------------------------------------------------------------------------------------')
print_table(10)
print_table(100)
print_table(1000)
print_table(10000)
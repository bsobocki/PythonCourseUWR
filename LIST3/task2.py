import math

# Sum [ i=1..k ] (2i - 1) = k^2 
# sqrt(n) = m  :  n = Sum [i=1..m] (2i - 1)
# look for m !

def sqrt_by_sum(n):
    s = 0
    m = 0
    while s <= n: # until the sum is bigger than n 
        m += 1
        s += (2*m -1)

    return m - 1

print(sqrt_by_sum(10000))
print(sqrt_by_sum(16))
print(sqrt_by_sum(25))
print(sqrt_by_sum(36))
print(sqrt_by_sum(49))
print(sqrt_by_sum(0))
print(sqrt_by_sum(9))
print(sqrt_by_sum(17))
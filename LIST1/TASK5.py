import math as m

def distribution(n):
    result = []
    count = 0
    pair = ()
    N = n
    for i in range(2, N+1):
        if (divisible(n,i)):
            pair = [i]
            while (divisible(n, i)):
                n = n//i
                count += 1
            pair.append(count)
            count = 0
            result.append( list(pair))
    return result

def divisible(a, b):
    return a % b == 0

print("756 = ", distribution(756))
print("7 = ", distribution(7))
print("4 = ",distribution(4))
print("3^7 * 2^4 * 13^2 = ", distribution(3**7*2**4*13**2))
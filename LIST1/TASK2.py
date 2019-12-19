def rest(n):
    denomination = [20, 10 , 5 , 2 , 1]
    result = []
    for i in denomination:
        if n>=i:
            count=0
            pair = [i]
            while n>=i:
                count+=1
                n -= i
            pair.append(count)
            result.append(list(pair))
    return result

print(rest(1200))
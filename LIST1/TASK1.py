def receipt(prices):
    #return sum(map(lambda x : x * 0.77, prices))
    return sum([x*0.23 for x in prices])

def invoice(prices):
    return sum(prices)*0.23

prices = [5.0,6.0,7.0,3.0]

print(receipt(prices) == invoice(prices))
print(receipt(prices))
print(invoice(prices))
    
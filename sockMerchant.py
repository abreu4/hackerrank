# https://www.hackerrank.com/challenges/sock-merchant/problem

import math

def sockMerchant(ar):
    
    lookup = {}
    
    for sock in ar:
        
        try:
            lookup[sock] += 1
        except:
            lookup[sock] = 1
            
    return sum((math.floor(s/2) for s in lookup.values()))


ar = [0,1,1,2,3,1,3]

print(sockMerchant(ar))
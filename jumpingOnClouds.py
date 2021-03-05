# https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem

def jumpingOnClouds(c):
   
    n = len(c)
    jumps = 0
    i = 0
    
    while i < n:
        
        if (i+2 < n) and c[i+2] == 0:
            
            i += 2
            jumps += 1
        
        elif (i+1 < n) and c[i+1] == 0:
        
            i += 1
            jumps += 1
            
        else: return jumps
            
    return jumps


c = [0,1,0,0,0,1,0]
c2 = [0,0,1,0,0,1,0]


print(jumps(c2))
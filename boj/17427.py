import sys
import math
input = sys.stdin.readline

n = int(input())

def g(x): 
    ret = 0 
    for i in range(1, x+1): 
        ret += (n // i) * i
    
    return ret

print(g(n))
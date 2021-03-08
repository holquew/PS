import sys
input = sys.stdin.readline

a = list(map(int, input().split()))

def ascending(a):
    for i in range(1, len(a)): 
        if a[i-1] > a[i]: 
            print('mixed')
            return
    
    print('ascending')


def descending(a): 
    for i in range(1, len(a)): 
        if a[i-1] < a[i]: 
            print('mixed')
            return 
    
    print('descending')

if a[0] < a[1]: 
    ascending(a)
else: 
    descending(a)


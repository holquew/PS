import sys
input = sys.stdin.readline

while True: 
    a = list(input().rstrip())
    if a[0] == '0': 
        break
    
    for i in range(len(a) // 2): 
        if a[i] != a[len(a) - i -1]: 
            print('no')
            break
        
    else: print('yes')
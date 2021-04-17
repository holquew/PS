'''일곱 난쟁이'''
import sys
input = sys.stdin.readline

dwarfs = [int(input()) for _ in range(9)]
total = sum(dwarfs)

for i in range(9): 
    for j in range(9): 
        if i == j: 
            continue
        
        if total - dwarfs[i] - dwarfs[j] == 100: 
            ans = [x for x in dwarfs if x != dwarfs[i] and x != dwarfs[j]]
            break

ans.sort()
print('\n'.join(map(str, ans)))
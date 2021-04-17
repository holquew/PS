'''부등호'''
import sys
input = sys.stdin.readline

def good(x, y, op): 
    if op == '<': 
        return False if x > y else True
    elif op == '>':
        return False if x < y else True


def check(num): 
    for i in range(n): 
        if a[i] == '<': 
            if num[i] > num[i+1]:
                return False
        elif a[i] == '>': 
            if num[i] < num[i+1]: 
                return False 
        
    return True

used = [False for _ in range(10)]
ans = []
def go(index, num): 
    if index == n+1:
        if check(num): 
            ans.append(num)
        return 
    
    for i in range(10): 
        if used[i]: 
            continue
        if index == 0 or good(num[index-1], str(i), a[index-1]):
            used[i] = True
            go(index+1, num+str(i))
            used[i] = False
        

n = int(input())
a = list(input().split())

go(0, "")
print(ans[-1])
print(ans[0])
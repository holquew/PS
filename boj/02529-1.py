import sys
input = sys.stdin.readline

k = int(input())
a = list(input().rstrip().split())

def good(a, b, op):
    if op == "<": 
        return True if a < b else False 
    elif op == ">": 
        return True if a > b else False

def check(s):
    for i in range(k): 
        if a[i] == '<': 
            if s[i] > s[i+1]: 
                return False
        if a[i] == '>': 
            if s[i] < s[i+1]: 
                return False 
    
    return True


answer = []
used = [False for _ in range(10)]
def go(index, s):
    if len(s) == k+1: 
        if check(s):
            answer.append(s)
        return 

    for i in range(10): 
        if used[i]: 
            continue 
        if index == 0 or good(s[index-1], str(i), a[index-1]): 
            used[i] = True
            go(index+1, s+str(i))
            used[i] = False

go(0, "")
print(answer[-1])
print(answer[0])
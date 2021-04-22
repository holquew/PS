import sys
input = sys.stdin.readline

l, c = map(int, input().split())
a = list(input().rstrip().split())
a.sort()

def check(s):
    mo = 0
    ja = 0 
    for c in s: 
        if c in 'aeiou': 
            mo += 1
        else: 
            ja += 1
    
    return mo >= 1 and ja >= 2

def go(index, word):
    if len(word) == l: 
        if check(word): 
            print(word)
        return 
    
    if index >= c: 
        return 
    
    go(index+1, word+a[index])
    go(index+1, word)


go(0, "")

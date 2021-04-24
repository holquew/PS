import sys
input = sys.stdin.readline

n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]

def get_score_diff(ones, twos):
    one = 0
    two = 0
    for i in range(n//2): 
        for j in range(n//2): 
            if i == j: 
                continue
            one += s[ones[i]][ones[j]]
            two += s[twos[i]][twos[j]]
    
    return abs(one-two)

def go(index, ones, twos):
    if len(ones) > n//2 or len(twos) > n//2: 
        return -1

    if index == n:
        if len(ones) != n//2:
            return -1 
        if len(twos) != n//2:
            return -1
        
        diff = get_score_diff(ones, twos)
        return diff
    
    ans = 987654321
    s1 = go(index+1, ones+[index], twos)
    if ans > s1 and s1 != -1: 
        ans = s1
    s2 = go(index+1, ones, twos+[index])
    if ans > s2 and s2 != -1: 
        ans = s2
    
    return ans


print(go(0, [], []))

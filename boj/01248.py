import sys
input = sys.stdin.readline

def check(index):
    s = 0
    for i in range(index, -1, -1): 
        s += ans[i]
        if sign[i][index] == 0: 
            if s != 0: 
                return False 
        elif sign[i][index] < 0: 
            if s >= 0: 
                return False 
        elif sign[i][index] > 0: 
            if s <= 0: 
                return False
    
    return True


def go(index): 
    if index == n: 
        return True

    if sign[index][index] == 0: 
        ans[index] = 0
        return (check(index) and go(index+1))

    for i in range(1, 11):
        ans[index] = i * sign[index][index]
        if check(index) and go(index+1): 
            return True
        
    return False

    

n = int(input())
a = list(input().rstrip())
sign = [[None] * n for _ in range(n)]
cnt = 0 
for i in range(n): 
    for j in range(i, n): 
        if a[cnt] == '0': 
            sign[i][j] = 0
        elif a[cnt] == '+': 
            sign[i][j] = 1
        else: 
            sign[i][j] = -1
        cnt += 1

ans = [0] * n 
go(0)
print(' '.join(map(str,ans)))
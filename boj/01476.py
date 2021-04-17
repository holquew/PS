import sys
input = sys.stdin.readline

e, s, m = map(int, input().split())
a, b, c = 0, 0, 0
count = 0
while True: 
    count += 1

    a += 1 
    b += 1 
    c += 1

    if a > 15:
        a = 1 
    if b > 28: 
        b =1
    if c > 19: 
        c = 1

    if a == e and b ==s and c == m: 
        print(count)
        break
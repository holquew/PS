import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t): 
    n = int(input())
    s = set()
    for i in range(n): 
        city = input().rstrip()
        s.add(city)

    print(len(s))
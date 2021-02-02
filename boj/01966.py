import sys
from collections import deque

t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    q = deque(map(int, sys.stdin.readline().split()))

    count = 0
    while q:
        highest = max(q)
        doc = q.popleft()
        m -= 1
        if doc != highest:
            q.append(doc)
            if m < 0:
                m = len(q) - 1
        else:
            count += 1
            if m < 0:
                print(count)
                break

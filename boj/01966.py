from collections import deque

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    q = deque(map(int, input().split()))
    index = [x for x in range(len(q))]
        

    count = 0
    while q:
        highest = max(q)
        paper = q.popleft()

        if paper == find:
            print('count ',  count)
            break

        if paper == highest:
            q.popleft()
        else:
            q.append(paper)

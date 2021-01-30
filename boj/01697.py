from collections import deque


def bfs():
    q = deque([n])
    while q:
        node = q.popleft()
        if node == k:
            print(time[node])
            return
        for i in (node-1, node+1, node*2):
            if 0 <= i <= MAX_N:
                if not time[i]:
                    q.append(i)
                    time[i] = time[node] + 1


n, k = map(int, input().split())
MAX_N = 100000
time = [0] * (MAX_N + 1)

bfs()


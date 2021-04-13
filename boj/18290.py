'''NM과 K'''
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

c = [[False] * m for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

answer = -987654321

def go(cnt, k_sum):
    global answer

    if cnt == k:
        if k_sum > answer:
            answer = k_sum
        return
    
    for x in range(n): 
        for y in range(m):
            if c[x][y]: 
                continue

            ok = True
            for o in range(4): 
                nx, ny = x + dx[o], y + dy[o]
                if 0 <= nx < n and 0 <= ny < m: 
                    if c[nx][ny]: 
                        ok = False

            if ok: 
                c[x][y] = True
                go(cnt + 1, k_sum + a[x][y])
                c[x][y] = False

go(0, 0)
print(answer)


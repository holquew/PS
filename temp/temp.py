import sys
input = sys.stdin.readline

n = int(input())
graph = [[0 for __ in range(n)] for _ in range(n)]

num = 1
x, y = 0, -1
for i in range(n):
    for j in range(i, n):
        if i % 3 == 0:
            y += 1
        elif i % 3 == 1:
            x += 1
        elif i % 3 == 2:
            x -= 1
            y -= 1

        graph[y][x] = num
        num += 1

answer = [x for g in graph for x in g if x != 0]
print(answer)

'''플로이드'''
import sys
input = sys.stdin.readline
INF = 987654321

n = int(input())
m = int(input())
costs = [[INF for _ in range(n)] for _ in range(n)]
for _ in range(m): 
    a, b, c = map(int, input().split())
    if costs[a-1][b-1] > c:
        costs[a-1][b-1] = c

for k in range(n): 
    for i in range(n): 
        for j in range(n):
            if i == j: 
                costs[i][j] = 0
                continue

            new_cost = costs[i][k] + costs[k][j] 
            if new_cost < costs[i][j]:
                costs[i][j] = new_cost

for cost in costs: 
    for i in cost: 
        if i == INF: 
            print(0, end=" ")
        else:
            print(i, end=" ")
    print()


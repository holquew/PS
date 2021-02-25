import sys
input = sys.stdin.readline

n = int(input())
dist = list(map(int, input().split()))
price = list(map(int, input().split()))
answer = 0

temp_min = price[0]
for i in range(n-1):
    if price[i] < temp_min:
        temp_min = price[i]

    answer += temp_min * dist[i]


print(answer)

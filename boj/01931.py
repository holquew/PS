import sys

n = int(input())
a = []
for i in range(n):
    a.append(tuple(map(int, sys.stdin.readline().split())))

a.sort(key=lambda x: (x[1], x[0]))

count = 1
last_time = a[0][1]
for time in a[1:]:
    if time[0] >= last_time:
        count += 1
        last_time = time[1]

print(count)

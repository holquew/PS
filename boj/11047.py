n, k = map(int, input().split())
a = []
for i in range(n):
    a.append(int(input()))

count = 0
for coin in a[::-1]:
    if k - coin < 0:
        continue

    m = k // coin
    k -= coin * m
    count += m


print(count)

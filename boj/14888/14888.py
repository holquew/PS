n = int(input())
a = list(map(int, input().split()))
cnt = list(map(int, input().split()))
b = []
for i in range(4):
    for c in range(cnt[i]):
        b.append(i)


print(b)

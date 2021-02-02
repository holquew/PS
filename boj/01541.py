exp = input().split('-')

ans = 0
for i in exp[0].split('+'):
    ans += int(i)

for e in exp[1:]:
    for num in e.split('+'):
        ans -= int(num)

print(ans)

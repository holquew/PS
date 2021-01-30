T = int(input())
for i in range(1, T + 1):
    nums = list(map(int, input().split()))
    total = 0
    for num in nums:
        if (num % 2 == 1):
            total += num
        else:
            pass

    print(f'#{i} {total}')

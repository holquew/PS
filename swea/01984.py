T = int(input())

for case in range(1, T+1):
    nums = list(map(int, input().split()))
    nums.sort()
    answer = 0
    for num in nums[1:-1]:
        answer += num
    print(f'#{case} {round(answer / 8)}')

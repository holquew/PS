T = int(input())

for case in range(1, T+1):
    N = int(input())
    answer = 0
    for i in range(1, N+1):
        if i % 2 != 0:
            answer += i
        else:
            answer -= i
    print(f'#{case} {answer}')

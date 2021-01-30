T = int(input())

for case in range(1, T+1):
    N = int(input())
    answer = [[1]]

    for i in range(1, N):
        temp = []
        for j in range(i + 1):
            if j == 0 or j == i:
                temp.append(1)
            else:
                temp.append(answer[i-1][j-1] + answer[i-1][j])
        answer.append(temp)

    print(f'#{case}')
    for line in answer:
        print(' '.join(map(str, line)))

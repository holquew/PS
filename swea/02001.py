def partial_sum(col_start, row_start, num_list, m):
    p_sum = 0
    sliced_table = [row[row_start:row_start+m]
                    for row in num_list[col_start: col_start+m]]

    for i in range(len(sliced_table)):
        for j in range(len(sliced_table[i])):
            p_sum += sliced_table[i][j]

    return p_sum


T = int(input())

for case in range(1, T+1):
    N, M = map(int, input().split())
    table = []
    for _ in range(N):
        row = list(map(int, input().split()))
        table.append(row)

    max_sum = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            result = partial_sum(i, j, table, M)
            if result > max_sum:
                max_sum = result

    print(f'#{case} {max_sum}')

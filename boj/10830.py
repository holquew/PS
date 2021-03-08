import sys
input = sys.stdin.readline


def mult_matrix(a, b, n):
    result = [[None] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            value = 0
            for k in range(n):
                value += a[i][k] * b[k][j]

            result[i][j] = value % 1000

    return result


def pow(x, y, n):
    if y == 0:
        return [[1, 0], [0, 1]]

    if y == 1:
        x = [[item % 1000 for item in sub] for sub in x]
        return x

    t = pow(x, y // 2, n)

    if y % 2 == 0:
        return mult_matrix(t, t, n)
    else:
        return mult_matrix(x, mult_matrix(t, t, n), n)


n, b = map(int, input().split())
a = []
for _ in range(n):
    a.append(list(map(int, input().split())))


answer = pow(a, b, n)
for i in answer: 
    print(*i)
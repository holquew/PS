from itertools import combinations

a = [1, 3, 5, 7]
answer = [''.join(map(str, x)) for x in list(combinations(a, 3))]


def go(current, arr, a, index, n):
    if len(current) == n:
        arr.append(''.join(map(str, current)))
        return

    for i in range(index, len(a)):
        current.append(a[i])
        go(current, arr, a, i+1, n)
        current.pop()


def comb(a, n):
    arr = []
    go([], arr, a, 0, n)
    return arr


print(
    answer)

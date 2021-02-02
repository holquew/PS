import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
n, m = map(int, input().split())

p = [x for x in range(n + 1)]


def find(x):
    if x == p[x]:
        return x
    else:
        p[x] = find(p[x])
        return p[x]


def union(a, b):
    x = find(a)
    y = find(b)
    if x != y:
        if x < y:
            p[y] = x
        else:
            p[x] = y


def is_same_parent(a, b):
    if find(a) == find(b):
        return True
    else:
        return False


for i in range(m):
    op, a, b = map(int, input().split())
    if op == 0:
        union(a, b)
    elif op == 1:
        if is_same_parent(a, b):
            print('YES')
        else:
            print('NO')

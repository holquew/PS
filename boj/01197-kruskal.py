import sys
input = sys.stdin.readline


def find(x, parent):
    if x == parent[x]:
        return x
    else:
        parent[x] = find(parent[x], parent)
        return parent[x]


def union(a, b, parent):
    x = find(a, parent)
    y = find(b, parent)
    if x != y:
        if x < y:
            parent[y] = x
        else:
            parent[x] = y


def is_same_parent(a, b, parent):
    x = find(a, parent)
    y = find(b, parent)
    return True if x == y else False


v, e = map(int, input().split())

edges = []
p = [x for x in range(v+1)]

for i in range(e):
    a, b, w = map(int, input().split())
    edges.append((a, b, w))

edges.sort(key=lambda x: x[2])

answer = 0
for e in edges:
    if is_same_parent(e[0], e[1], p):
        continue

    answer += e[2]
    union(e[0], e[1], p)


print(answer)

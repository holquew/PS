'''링크와 스타트'''
import sys
input = sys.stdin.readline

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]


def calc_diff(first, second):
    t1 = 0
    t2 = 0

    for i in range(len(first)):
        for j in range(len(first)):
            if i == j:
                continue
            t1 += a[first[i]][first[j]]

    for i in range(len(second)):
        for j in range(len(second)):
            if i == j:
                continue

            t2 += a[second[i]][second[j]]

    return abs(t1-t2)


answer = 987654321


def go(index, first, second):
    global answer

    if index > n:
        return

    if index == n:
        if len(first) < 1:
            return -1
        if len(second) < 1:
            return -1
        temp = calc_diff(first, second)
        if temp < answer:
            answer = temp

    go(index+1, first+[index], second)
    go(index+1, first, second+[index])


go(0, [], [])
print(answer)

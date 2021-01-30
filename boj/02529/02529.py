from itertools import permutations


def check(perm, A):
    for i in range(len(A)):
        if (A[i] == '<' and perm[i] > perm[i + 1]):
            return False

        if (A[i] == '>' and perm[i] < perm[i + 1]):
            return False

    return True


K = int(input())
A = list(input().split())

big = [x for x in range(9, 9 - K - 1, -1)]
small = [x for x in range(0, K + 1)]

for big_p in permutations(big, K+1):
    if check(big_p, A):
        print(''.join(map(str, big_p)))
        break


for small_p in permutations(small, K+1):
    if check(small_p, A):
        print(''.join(map(str, small_p)))
        break

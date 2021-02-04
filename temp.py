import sys
from itertools import permutations
input = sys.stdin.readline

n, m = map(int, input().split())

nums = [x for x in range(1, n+1)]
permute = list(permutations(['a', 'b', 'c'], 3))
for p in permute: 
    print(' '.join(map(str, p)))


# n, m, k = map(int, input().split())
# a = list(map(int, input().split()))

# a.sort(reverse=True)
# first = a[0]
# second = a[1]
# partial_sum = first * k + second

# answer = partial_sum * (m // (k+1)) + first * (m % (k+1))
# print(answer)


# from itertools import product

# data = ['A', 'B', 'C']
# result = list(product(data, repeat=2))

# print(result)


# n = int(input())

# if n % 2 == 0:
#     print('CY')
# else:
#     print('SK')

# word = input()
# a = ['', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ', ]

# time = 0
# for ch in word:
#     for i in range(len(a)):
#         if ch in a[i]:
#             time += i + 2

# print(time)


# a, b = input().split()
# print(max(a[::-1], b[::-1]))

# word = input()
# alpha = [-1] * 26
# for i in range(len(word)):
#     if alpha[ord(word[i]) - 97] == -1:
#         alpha[ord(word[i]) - 97] = i

# print(' '.join(map(str, alpha)))

# t = int(input())
# for i in range(t):
#     n, s = input().split()
#     print(''.join([c * int(n) for c in list(s)]))


# word = input()
# word = word.upper()
# dic = {}
# for ch in word:
#     if ch in dic.keys():
#         dic[ch] += 1
#     else:
#         dic[ch] = 1

# answer = [k for k, v in dic.items() if max(dic.values()) == v]
# if len(answer) == 1:
#     print(answer[0])
# else:
#     print('?')

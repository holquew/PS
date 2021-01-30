# import re

# p = re.compile('[0124578]*[369][0124578]*')
# num = int(input())

# for i in range(1, num + 1):
#     if p.match(str(i)):
#         word = i
#         while word > 0:
#             if word % 10 == 3 or word % 10 == 6 or word % 10 == 9:
#                 print('-', end='')
#             word = word // 10
#         print(' ', end='')
#     else:
#         print(i, end=' ')

num = int(input())

for i in range(1, num + 1):
    stack = 0
    l = list(str(i))
    for j in range(len(l)):
        if l[j] == '3' or l[j] == '6' or l[j] == '9':
            stack += 1
    if stack == 0:
        print(i, end='')
    elif stack == 1:
        print('-', end='')
    elif stack == 2:
        print('--', end='')
    elif stack == 3:
        print('---', end='')

    print(' ', end='')

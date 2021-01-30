# 괄호
n = int(input())


def isVPS(string):
    temp = []
    for i in string:
        if (i == '('):
            temp.append(i)
        else:
            if len(temp) == 0:
                print('NO')
                return
            else:
                temp.pop()

    if len(temp) == 0:
        print('YES')
        return
    else:
        print('NO')
        return


for _ in range(n):
    s = list(input())
    isVPS(s)

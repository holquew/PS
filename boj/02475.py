ns = list(map(int, input().split()))


def pow2(i):
    return i ** 2


print(sum(map(pow2, ns)) % 10)

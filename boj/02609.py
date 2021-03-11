'''최대공약수와 최소공배수'''
import sys
input = sys.stdin.readline


def gcd(x, y):
    if x < y:
        temp = x
        x = y
        y = temp

    while y > 0:
        r = x % y
        x = y
        y = r

    return x


def lcm(x, y):
    return (x * y) // gcd(x, y)


a, b = map(int, input().split())
print(gcd(a, b))
print(lcm(a, b))

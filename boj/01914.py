import sys
input = sys.stdin.readline

answer = []
def hanoi(n, fr, to, temp):
    if n == 1:
        print(f'{fr} {to}')
        return

    hanoi(n-1, fr, temp, to)
    print(f'{fr} {to}')
    hanoi(n-1, temp, to, fr)


n = int(input())
print(2**n -1)
if n <= 20:
    hanoi(n, 1, 3, 2)

N = int(input())

for i in range(1, N):
    for j in range(N - i):
        print(" ", end="")
    print("*", end="")
    for h in range(2 * (i - 1) - 1):
        print(" ", end="")
    if i != 1:
        print("*", end="")
    print()

for a in range(2 * N - 1):
    print("*", end="")

T = int(input())

for case in range(1, T+1):
    string = input()
    for i in range(1, len(string)):
        if string[:i] == string[i:i+i]:
            temp = i
            break
    print(f'#{case}', len(string[:i]))

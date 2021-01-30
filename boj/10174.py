n = int(input())


def isPalindrome(s):
    s = s.lower()

    half_len = len(s) // 2

    for i in range(half_len):
        if s[i] != s[-i - 1]:
            return False

    return True


for _ in range(n):
    s = input()
    if isPalindrome(s):
        print('Yes')
    else:
        print('No')

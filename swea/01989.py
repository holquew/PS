T = int(input())


def isPalindrome(s):
    s = s.lower()

    half_len = len(s) // 2

    for i in range(half_len):
        if s[i] != s[-i - 1]:
            return False

    return True


for case in range(1, T+1):
    word = input()
    if isPalindrome(word):
        print(f'#{case} 1')
    else:
        print(f'#{case} 0')

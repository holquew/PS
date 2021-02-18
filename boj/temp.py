while True:
    try:
        n = int(input())
        remainder = 0
        count = 0
        while True:
            count += 1
            remainder = remainder * 10 + 1
            remainder %= n
            if remainder == 0:
                print(count)
                break
    except:
        break

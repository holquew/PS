'''N과 M (5)'''

n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort() 
used = []

def go(index, cur, m): 
    if index > n: 
        return 

    if len(cur) == m: 
        print(' '.join(map(str, cur)))
        return 
    
    for i in range(n): 
        if a[i] in used: 
            continue 
        used.append(a[i])
        go(index+1, cur+[a[i]], m)
        used.pop()

go(0, [], m)
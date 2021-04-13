from itertools import permutations

a = [3, 5, 9, 1]
answer = [''.join(map(str, x)) for x in list(permutations(a, len(a)))]


def go(current, arr, left):
    if len(left) == 0: 
        arr.append(''.join(map(str, current)))
        return 
    
    for c in left: 
        current.append(c)
        new_left = list(left)
        new_left.remove(c)
        go(current, arr, new_left)
        current.pop()

def perm(a): 
    arr = []
    go([], arr, a)
    return arr

print(
    perm(a)
)
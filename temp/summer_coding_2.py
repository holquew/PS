from collections import deque

def solution(t, r):
    answer = []
    customers = []
    
    n = len(t)
    max_t = max(t)

    for i in range(n):
        customers.append((t[i], r[i], i))

    waiting = deque([])
    now = 0
    while customers:
        incomes = [x for x in customers if x[0] == now]
        if waiting and not incomes:
            out = waiting.popleft()
            answer.append(out[2])
            customers.remove(out)
        
        if incomes:
            new = list(waiting) + incomes
            new.sort(key=lambda x: (x[1], x[2]))
            waiting = deque(new)
        
        if waiting:
            out = waiting.popleft()
            answer.append(out[2])
            customers.remove(out)
        
        now += 1

    return answer

print(
    solution([0, 0, 0, 0] ,[0, 0, 0, 0])
)
print(
    solution([7, 6, 8, 1] ,[0, 1, 2, 3])
)
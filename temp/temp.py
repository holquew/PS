from collections import deque


def solution(priorities, location):
    answer = 0
    queue = deque(priorities)
    while queue:
        max_priority = max(queue)
        check = queue.popleft()
        location -= 1
        if location == -1:
            if check == max_priority:
                answer += 1
                break
            else:
                location = len(queue)

        if check == max_priority:
            answer += 1
        else:
            queue.append(check)

    return answer


print(solution([1, 1, 9, 1, 1, 1], 0))

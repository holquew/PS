board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [
    0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
moves = [1, 5, 3, 5, 1, 2, 1, 4]


def solution(board, moves):
    answer = 0
    stack = []

    for i in moves:
        for j in range(len(board)):
            if board[j][i - 1] > 0:
                stack.append(board[j][i - 1])
                board[j][i - 1] = 0
                print(stack)

                if len(stack) >= 2 and stack[-1] == stack[-2]:
                    stack.pop()
                    stack.pop()
                    answer += 2

    return answer

# def solution(board, moves):
#     bucket = []
#     answer = 0

#     for i in moves:
#         for j in range(len(board)):
#             if board[j][i-1] == 0:
#                 pass
#             else:
#                 bucket.append(board[j][i-1])
#                 board[j][i-1] = 0
#                 break

#         if len(bucket) >= 2 and bucket[len(bucket) - 1] == bucket[len(bucket) - 2]:
#             bucket.pop()
#             bucket.pop()
#             answer += 2

#     return answer


print(solution(board, moves))

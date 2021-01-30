T = int(input())

for case in range(1, T+1):
    N, K = map(int, input().split())

    scores = []
    grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    for _ in range(N):
        s1, s2, s3 = map(int, input().split())
        total_score = s1 * 0.35 + s2 * 0.45 + s3 * 0.2
        scores.append(total_score)

    grades = sorted(scores, reverse=True)
    K_grade = grades.index(scores[K-1]) // (N//10)
    print(f'#{case} {grade[K_grade]}')

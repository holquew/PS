participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]


def solution(participant, completion):
    dic = {}
    for p in participant:
        if p not in dic.keys():
            dic[p] = 1
        else:
            dic[p] += 1

    for c in completion:
        if c in dic.keys():
            dic[c] -= 1

    answer = [k for k, v in dic.items() if v != 0][0]
    return answer


print(zip(participant, completion))

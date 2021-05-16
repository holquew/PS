import re
from collections import defaultdict


def solution(code, day, data):
    answer = []
    n = len(data)
    infos = defaultdict(list)
    arr = []
    for i in range(n):
        d = data[i].split()
        price_info = int(re.findall("\d+", d[0])[0])
        code_num = re.findall("\d+", d[1])[0]
        time_info = re.findall("\d+", d[2])[0]
        infos[code_num].append((time_info[:8], time_info[8:], price_info))

    for info in infos[code]:
        if info[0].startswith(day):
            answer.append((info[1], info[2]))

    answer = [x[1] for x in sorted(answer)]
    return answer


print(
    solution("012345", "20190620", ["price=80 code=987654 time=2019062113", "price=90 code=012345 time=2019062014",
                                    "price=120 code=987654 time=2019062010", "price=110 code=012345 time=2019062009", "price=95 code=012345 time=2019062111"])
)

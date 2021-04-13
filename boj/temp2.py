import re


def solution(inp_str):
    answer = []
    p = re.compile('[\d\w~!@#$%^&*]')
    if not 8 <= len(inp_str) <= 15:
        answer.append(1)

    letters = p.findall(inp_str)
    if len(letters) != len(inp_str): 
        answer.append(2)
    
    kind = 0
    if re.search('[A-Z]', inp_str):
        kind += 1
    if re.search('[a-z]', inp_str): 
        kind += 1
    if re.search('[0-9]', inp_str): 
        kind += 1
    if re.search('[~!@#$%^&*]', inp_str): 
        kind += 1
    
    if kind < 3: 
        answer.append(3)

    for letter in letters: 
        if re.search(letter * 4, inp_str): 
            answer.append(4)
            break

    for letter in letters:
        if len(re.findall(letter, inp_str)) >= 5: 
            answer.append(5)
            break
    
    if len(answer) == 0: 
        answer.append(0)
    
    return answer


print(
    solution(
        "CaCbCgCdC888834A"
    )
)

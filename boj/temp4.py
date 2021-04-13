name_id_pairs = {0: 'root'}

visited = []
answer = []

def dfs(start_id, search, dic, temp):
    visited.append(start_id)
    stack = [start_id]

    if len(dic[start_id]) == 0: 
        temp = '/'.join(temp)
        if search in temp: 
            answer.append(temp)
        print(answer)
        return

    while stack:
        for node in dic[start_id]:
            node_id, name = node
            if node_id not in visited:
                temp.append(name)
                dfs(node_id, search, dic, temp)


def solution(data, word):
    dic = {}

    for item in data:
        node_id, name, parent = item.split()
        node_id = int(node_id)
        parent = int(parent)
        name_id_pairs[node_id] = name
        if parent not in dic:
            dic[parent] = []

        dic[parent].append((node_id, name))
        if node_id not in dic:
            dic[node_id] = []
    
    dfs(0, word, dic, [])

    return answer


print(
    solution(
        ["1 BROWN 0", "2 CONY 0", "3 DOLL 1", "4 DOLL 2", "5 LARGE-BROWN 3",
            "6 SMALL-BROWN 3", "7 BLACK-CONY 4", "8 BROWN-CONY 4"],
        'BROWN'
    )
)

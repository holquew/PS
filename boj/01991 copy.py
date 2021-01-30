
n = int(input())
tree = [None] * 1000000

index_hashmap = {}


def insert(p, cl, cr):
    p_index = index_hashmap[p]

    if cl != '.':
        tree[p_index * 2] = cl
        index_hashmap[cl] = p_index*2

    if cr != '.':
        tree[p_index * 2 + 1] = cr
        index_hashmap[cr] = p_index*2 + 1


p, cl, cr = input().split()
tree[1] = p
index_hashmap[p] = 1
insert(p, cl, cr)

for i in range(n - 1):
    p, cl, cr = input().split()
    insert(p, cl, cr)


def preorder(index):
    if tree[index] == None:
        return

    print(tree[index], end='')
    preorder(index * 2)
    preorder(index * 2 + 1)


def inorder(index):
    if tree[index] == None:
        return

    inorder(index * 2)
    print(tree[index], end='')
    inorder(index * 2 + 1)


def postorder(index):
    if tree[index] == None:
        return

    postorder(index * 2)
    postorder(index * 2 + 1)
    print(tree[index], end='')


preorder(1)
print()
inorder(1)
print()
postorder(1)
print()

import sys
input = sys.stdin.readline


class Stack:
    def __init__(self):
        self._stack = []
        self.size = 0

    def push_back(self, value):
        self._stack.append(value)
        self.size += 1

    def pop_back(self): 
        if self.size == 0: 
            return -1
        
        self.size -= 1
        return self._stack.pop(-1)

    def my_size(self): 
        return self.size

    def empty(self): 
        return 1 if self.size == 0 else 0

    def top(self): 
        return self._stack[-1] if self.size != 0 else -1



n = int(input())
a = Stack()
for _ in range(n):
    op = input().split()
    if op[0] == 'push':
        a.push_back(int(op[1]))
    elif op[0] == 'pop': 
        print(a.pop_back())
    elif op[0] == 'size':
        print(a.my_size())
    elif op[0] == 'empty':
        print(a.empty())
    elif op[0] == 'top': 
        print(a.top())


import sys
input = sys.stdin.readline


class Deque:
    def __init__(self):
        self._deque = []
        self.size = 0

    def push_front(self, value):
        self._deque.insert(0, value)
        self.size += 1

    def push_back(self, value):
        self._deque.append(value)
        self.size += 1

    def pop_front(self): 
        if self.size == 0: 
            return -1
        
        self.size -= 1
        return self._deque.pop(0)

    def pop_back(self): 
        if self.size == 0: 
            return -1
        
        self.size -= 1
        return self._deque.pop(-1)

    def my_size(self): 
        return self.size

    def empty(self): 
        return 1 if self.size == 0 else 0

    def front(self): 
        return self._deque[0] if self.size != 0 else -1
    
    def back(self): 
        return self._deque[-1] if self.size != 0 else -1



n = int(input())
a = Deque()
for _ in range(n):
    op = input().split()
    if op[0] == 'push_front':
        a.push_front(int(op[1]))
    elif op[0] == 'push_back': 
        a.push_back(int(op[1]))
    elif op[0] == 'pop_front': 
        print(a.pop_front())
    elif op[0] == 'pop_back': 
        print(a.pop_back())
    elif op[0] == 'size':
        print(a.my_size())
    elif op[0] == 'empty':
        print(a.empty())
    elif op[0] == 'front': 
        print(a.front())
    elif op[0] == 'back': 
        print(a.back())


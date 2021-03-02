import sys
input = sys.stdin.readline


class Queue:
    def __init__(self):
        self._my_queue = []
        self.size = 0

    def push_back(self, value):
        self._my_queue.append(value)
        self.size += 1

    def pop_front(self): 
        if self.size == 0: 
            return -1
        
        self.size -= 1
        return self._my_queue.pop(0)

    def my_size(self): 
        return self.size

    def empty(self): 
        return 1 if self.size == 0 else 0

    def front(self): 
        return self._my_queue[0] if self.size != 0 else -1
    
    def back(self): 
        return self._my_queue[-1] if self.size != 0 else -1



n = int(input())
a = Queue()
for _ in range(n):
    op = input().split()
    if op[0] == 'push':
        a.push_back(int(op[1]))
    elif op[0] == 'pop': 
        print(a.pop_front())
    elif op[0] == 'size':
        print(a.my_size())
    elif op[0] == 'empty':
        print(a.empty())
    elif op[0] == 'front': 
        print(a.front())
    elif op[0] == 'back': 
        print(a.back())


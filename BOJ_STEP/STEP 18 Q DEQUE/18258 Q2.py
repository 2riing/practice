import sys
# sys.stdin = open('input.txt')
from collections import deque

q = deque()
N = int(sys.stdin.readline())
# print(Instruction)
for i in range(N):
    Instruction = sys.stdin.readline().split()
    if Instruction[0] == 'push':
        q.append(int(Instruction[1]))
    elif Instruction[0] == 'pop':
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif Instruction[0] == 'size':
        print(len(q))
    elif Instruction[0] == 'empty':
        if q:
            print(0)
        else:
            print(1)
    elif Instruction[0] == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    elif Instruction[0] == 'back':
        if q:
            print(q[-1])
        else:
            print(-1)



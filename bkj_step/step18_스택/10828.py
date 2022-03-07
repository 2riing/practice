import sys
sys.stdin = open('input.txt')

N = int(input())
instructions = []

for i in range(N):
    instructions.append(input())

stack = []
for instruction in instructions:
    if instruction[0:4] == 'push':
        stack.append(int(instruction[5:]))
    elif instruction == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif instruction == 'size':
        print(len(stack))
    elif instruction == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    elif instruction == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)

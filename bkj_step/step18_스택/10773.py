import sys
sys.stdin = open('input.txt')

K = int(input())
arr = [int(input()) for _ in range(K)]
result = 0
stack = []

for a in arr:
    if len(arr) == 0:
        break
    elif a > 0:
        stack.append(a)
    elif a == 0:
        stack.pop()


print(sum(stack))
import sys
sys.stdin = open('input.txt')

N = int(input())

def Find_VPS(arr):
    stack = []
    for a in arr:
        if a == '(':
            stack.append(a)
        else: # 닫는 괄호가 나오면
            if len(stack) > 0:
                stack.pop()
            else:
                return "NO"
    if len(stack) == 0:
        return "YES"
    else:
        return "NO"

for i in range(N):
    arr = input()
    print(Find_VPS(arr))


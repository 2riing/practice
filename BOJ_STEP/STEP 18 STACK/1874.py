import sys
sys.stdin = open('input.txt')

T = int(input())
nums = [int(input()) for _ in range(T)]
stack = []
num_list = [i+1 for i in range(T)]


sign = []

def StackNumber():
    result = 0
    for j in range(len(nums)):
        for i in range(len(num_list)):
            if stack[-1] == nums[j]:
                if stack: # 스택이 유효할 경우 pop 해서 result에 저장
                    result += stack.pop()
                    sign.append('-')
                else:
                    return 'No'
            else:
                stack.append(num_list[i])
                sign.append('+')
    if result == nums:
        return sign
    else:
        return 'No'





print(StackNumber())
import sys
sys.stdin = open('input.txt')

def FindBalance(words):
    for word in words:
        if word == '(' or word == '[':
            stack.append(word)
        elif stack and word == ')':
            if stack[-1] == '(':
                stack.pop()
            else:
                return 'no'
        elif len(stack) > 0 and word == ']':
            if stack[-1] == '[':
                stack.pop()
            else:
                return 'no'

    if stack:
        return 'no'
    elif len(stack)==0:
        return 'yes'

while True:
    words = input()
    stack = []
    if words == '.':
        break
    else:
        print(FindBalance(words))
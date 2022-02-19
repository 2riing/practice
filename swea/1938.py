import sys
sys.stdin = open('input.txt')

num1, num2 = list(map(int,input().split()))

print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(round(num1 // num2))
import sys
sys.stdin = open('input.txt')

N = int(input())
num = list(input())
total = 0
for i in range(len(num)):
    total += int(num[i])

print(total)
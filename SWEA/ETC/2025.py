import sys
sys.stdin = open('input.txt')

num = int(input())
total = 0
for i in range(1,num+1):
    total += i
print(total)
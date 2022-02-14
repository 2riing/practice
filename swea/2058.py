import sys
sys.stdin = open('input.txt')

N = input()
total = 0

for i in N:
    total += int(i)

print(total)
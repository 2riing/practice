import sys
sys.stdin = open('input.txt')
total = 0
for _ in range(5):
    total += int(input())
print(total)
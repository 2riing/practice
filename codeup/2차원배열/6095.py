import sys
sys.stdin = open('input.txt')


pan = [[0]*19 for _ in range(19)]

n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    pan[x-1][y-1] = 1


for i in range(19):
    print(*pan[i])
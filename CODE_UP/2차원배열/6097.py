import sys
sys.stdin = open('input.txt')


h, w = map(int, input().split())
n = int(input())
pan = [[0]*w for _ in range(h)]

def Turn(l, d, row, col, pan):
    if d == 0:
        for i in range(l):
            pan[row-1][col-1+i] = 1
    else:
        for i in range(l):
            pan[row+i-1][col-1]= 1

for _ in range(n):
    l, d, x, y = map(int, input().split())
    Turn(l, d, x, y, pan)

for i in range(len(pan)):
    print(*pan[i])
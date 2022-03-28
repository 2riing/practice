import sys
sys.stdin = open('input.txt')

n = int(input())
points = [list(map(int, input().split())) for _ in range(n)]
matrix = []
for _ in range(19):
    matrix.append([0 for _ in range(19)])

for i in range(len(points)):
    matrix[points[i][0]-1][points[i][1]-1] = 1

for i in range(19):
    print(*matrix[i])
import sys
sys.stdin = open('input.txt')

matrix = []
for _ in range(19):
    matrix.append(list(map(str,input().split())))

n = int(input())
points = [list(map(int, input().split())) for _ in range(n)]

print(matrix)

for i in range(len(points)):
    for j in range(19):
    matrix[points[i][0]-1][points[i][1]-1] = 1

for i in range(19):
    print(*matrix[i])
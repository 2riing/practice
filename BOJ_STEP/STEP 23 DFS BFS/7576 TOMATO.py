import sys
sys.stdin = open('input.txt')
from collections import deque

def BFS():
    ni, nj = [1, -1, 0, 0], [0, 0, 1, -1]
    while q:
        temp = q.popleft()
        row, col = temp[0], temp[1]
        for i in range(4):
            di, dj = row + ni[i], col + nj[i]
            if 0 <= di < N and 0<= dj < M:
                if visited[di][dj] == 0 and tomato[di][dj] == 0:
                    visited[di][dj] = visited[row][col] + 1
                    q.append([di, dj])

M, N = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

q = deque()
for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            q.append([i,j])
            visited[i][j] = 1

BFS()
max_num = 0
for i in range(len(visited)):
    if max_num < max(visited[i]):
        max_num = max(visited[i])

print(max_num-1)


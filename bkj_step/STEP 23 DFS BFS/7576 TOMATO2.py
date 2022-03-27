import sys
sys.stdin = open('input.txt')
from collections import deque


# 토마토 찾는 함수
def BFS():
    global N, M, q
    global tomato
    ni, nj = [1, -1, 0, 0], [0, 0, 1, -1]
    while q:
        temp = q.popleft()
        row, col = temp[0], temp[1]
        for i in range(4):
            di, dj = row + ni[i], col + nj[i]
            if 0 <= di < N and 0 <= dj < M:
                if tomato[di][dj] != -1 and tomato[di][dj] == 0:
                    tomato[di][dj] = tomato[row][col] + 1
                    q.append([di, dj])
    return tomato[row][col]-1


# 토마토가 익지 않은게 있으면 -1
def result():
    global N, M, q
    global tomato
    results = BFS()
    for l in range(N):
        for m in range(M):
            if tomato[l][m] == 0:
                return -1
    else:
        return results

# 기본 입력
M, N = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(N)]
q = deque()
for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            q.append([i,j])
if q:
    print(result())
else:
    print(-1)





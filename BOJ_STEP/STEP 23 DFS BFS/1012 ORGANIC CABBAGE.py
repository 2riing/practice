import sys
sys.stdin = open('input.txt')


def DFS(cnt, i, j):
    ni, nj = [1, -1, 0, 0], [0, 0, 1, -1]
    stack = []
    stack.append([i,j])
    while stack:
        temp = stack.pop()
        row, col = temp[0], temp[1]
        visited[row][col] = cnt
        for i in range(4):
            di, dj = row + ni[i], col + nj[i]
            if 0<= di < N and 0<= dj < M:
                if visited[di][dj] == 0 and farm[di][dj] == 1:
                    stack.append([di, dj])


# 기본 입력
T = int(input())
for tc in range(1, T+1):
    M, N, K = map(int, input().split()) # 가로길이, 세로길이, 배추 위치의 개수
    farm = [[0] * M for _ in range(N)]
    visited = [[0]*M for _ in range(N)]
    # 배추의 위치를 입력받아서 farm에 1로 표시해줌
    for k in range(K):
        a, b = map(int, input().split())
        farm[b][a] = 1

    cnt = 1
    for i in range(N):
        for j in range(M):
            if farm[i][j] == 1 and visited[i][j] == 0:
                DFS(cnt, i, j)
                cnt += 1

    print(cnt-1)
import sys
sys.stdin = open('input.txt')
from collections import deque
import psutil

def memory_usage():
    # current process RAM usage
    p = psutil.Process()
    rss = p.memory_info().rss / 2 ** 20 # Bytes to MB
    return f"{rss: 10.1f} MB"

def CheckPipe(row, col): # 현재 위치를 받아와서 체크할 파이프 방향을 반환
    if pipe[row][col] == 1: # 상하좌우
        di = [1, -1, 0, 0]
        dj = [0, 0, 1, -1]
        return di, dj
    elif pipe[row][col] == 2: # 상하
        di = [1, -1, 0, 0]
        dj = [0, 0, 0, 0]
        return di, dj
    elif pipe[row][col] == 3: # 좌우
        di = [0, 0, 0, 0]
        dj = [0, 0, 1, -1]
        return di, dj
    elif pipe[row][col] == 4: # 상우
        di = [0, -1, 0, 0]
        dj = [0, 0, 1, 0]
        return di, dj
    elif pipe[row][col] == 5: # 하우
        di = [1, 0, 0, 0]
        dj = [0, 0, 1, 0]
        return di, dj
    elif pipe[row][col] == 6: # 하좌
        di = [1, 0, 0, 0]
        dj = [0, 0, 0, -1]
        return di, dj
    elif pipe[row][col] == 7: # 상좌
        di = [0, -1, 0, 0]
        dj = [0, 0, 0, -1]
        return di, dj

def CheckNextPipe(i, mi, mj):
    if i == 0 and mi[1] == -1:
        return True
    elif i == 1 and mi[0] == 1:
        return True
    elif i == 2 and mj[3] == -1:
        return True
    elif i == 3 and mj[2] == 1:
        return True
    else:
        return False

def FindFugitiveBFS():
    global visited
    while queue:
        cur = queue.popleft()
        row, col = cur[0], cur[1]
        if pipe[row][col] != 0:
            di, dj = CheckPipe(row, col)
        for i in range(4):
            ni = di[i]
            nj = dj[i]
            if 0 <= row+ni < N and 0<= col+nj < M and visited[row+ni][col+nj] == 0 and pipe[row+ni][col+nj]:
                mi, mj = CheckPipe(row+ni, col+nj)
                if CheckNextPipe(i, mi, mj):
                    queue.append([row+ni, col+nj])
                    visited[row+ni][col+nj] = visited[row][col] + 1

# 기본 입출력
T = int(input())
for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    # 세로 N * 가로 M 지도 / 세로 R 가로 C 맨홀 위치 / L 주어진 시간
    pipe = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0 for _ in range(M)] for _ in range(N)]
    queue = deque([[R, C]]) # 시작값
    visited[R][C] = 1 # 시작 True로 만들어주기

    FindFugitiveBFS()

    total = 0
    for i in range(N):
        for j in range(M):
            if 0<visited[i][j]<=L:
                total += 1
    print(f'#{tc} {total}')

print(memory_usage())
def dfs_delta(i
    visited[i][j] = True

    # 0. base case
    if matrix[i][j] == 3:
        return True
    # 1. 이동할 수 있는 곳 찾아서 가보기. 상 우 하 좌 순
    for di, dj in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        ni = i + di
        nj = j + dj
        # 2. 갈 수 있는 길이면서
        if 0 <= ni < N and 0 <= nj < N and matrix[ni][nj] != 1:
            # 2. 방문한 적이 없다면 이동
            if not visited[ni][nj]:
                dfs_delta(ni, nj)


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, list(input()))) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]

    # 시작점에서 출발해서 갈 수 있는 곳을 visited에 표현한다.
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 2:
                dfs_delta(i, j)
                break

    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 3:
                print(f'#{tc} {int(visited[i][j])}')
                break
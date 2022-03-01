def dfs_delta(i, j):
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
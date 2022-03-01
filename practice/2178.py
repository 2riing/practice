from collections import deque
import sys
sys.stdin = open('input.txt')

n, m = map(int, input().split())
maze = [list(map(int, input())) for _ in range(n)]
dist = [[0]*m for i in range(n)]
dist[0][0] = 1

dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

print(maze)

def bfs(x, y):
    q = deque()
    q.append((x, y))

    while q:
        if q == False:
            return dist[n-1][m-1]
        else:
            x, y = q.popleft()

            for dx, dy in dir:
                nx = x + dx
                ny = y + dy
                if nx < 0 or ny < 0 or nx >= n or ny >= m-1:
                    continue
                if nx>=0 and ny>=0 and nx<n and ny<m:
                    if maze[nx][ny] == 1:
                        dist[nx][ny] = dist[x][y] + 1
                        q.append((nx, ny))


print(bfs(0, 0))
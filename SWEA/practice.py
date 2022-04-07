from collections import deque
def BFS():
    ni, nj = [1, -1, 0, 0], [0, 0, 1, -1]
    q = deque()
    q.append((0,0))
    visited[0][0] = 1
    while q:
        row, col = q.popleft()
        if a[row][col] == 2:
            return 1
        for i in range(4):
            di, dj = ni[i]+row , nj[i]+col
            if 0<= di <5 and 0<= dj <4:
                if visited[di][dj] == 0 and a[di][dj] == 0:
                    q.append((di, dj))
                    visited[di][dj] = visited[row][col] + 1



a = [[0,1,0,0],[0,1,2,2],[0,1,0,2],[0,1,0,2],[0,0,0,0]]
visited =[[ 0 for _ in range(4)] for _ in range(5)]

print(BFS())
print(visited)
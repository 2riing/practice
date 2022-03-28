import sys
sys.stdin = open('input.txt')

N = int(input()) # 컴퓨터의 수 (노드 개수)
M = int(input()) # 쌍의 수
graph = [[0] * (N+1) for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1
visited = [0] * (N+1)
stack = []
def DFS(v):
    stack.append(v)
    while stack:
        v = stack.pop()
        visited[v] = 1
        for i in range(N+1):
            if graph[v][i] == 1 and visited[i] == 0:
                stack.append(i)
DFS(1)
print(sum(visited)-1)


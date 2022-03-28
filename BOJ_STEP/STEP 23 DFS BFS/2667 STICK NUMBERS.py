import sys
sys.stdin = open('input.txt')

# 이동하면서 danji의 수로 바꿔주기
def DFS(danji, i, j):
    ni, nj = [1, -1, 0, 0], [0, 0, 1, -1]
    stack = []
    stack.append([i, j])
    while stack:
        temp = stack.pop()
        row, col = temp[0], temp[1]
        visited[row][col] = danji
        for k in range(4):
            di, dj = row + ni[k], col+ nj[k]
            if 0<= di < N and 0<= dj < N:
                if visited[di][dj] == 0 and maps[di][dj] == 1:
                    stack.append([di, dj])

# 기본 입력
N = int(input()) # 지도의 크기
maps = [list(map(int, input())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]

# 방문하지 않은 1을 만나면 DFS실행
danji = 2
for i in range(N):
    for j in range(N):
        if maps[i][j] == 1 and visited[i][j] == 0:
            DFS(danji, i, j)
            danji += 1

# 단지의 개수 세주기
results = []
sum_temp = 0
print(danji-2)
for j in range(2, danji):
    sum_temp = 0
    for i in range(len(visited)):
        sum_temp += visited[i].count(j)
    results.append(sum_temp)

# 정렬해서 출력해주기
results.sort()
for result in results:
    print(result)

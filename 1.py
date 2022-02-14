N = int(input())
arr = [[0]*N] + [list(map(int,input().split())) for _ in range(N)] + [[0]]*N + [0]*N

print(arr)
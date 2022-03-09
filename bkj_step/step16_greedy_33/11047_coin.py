import sys
sys.stdin = open('input.txt')

N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
cnt = 0

for i in range(len(coins)-1, -1, -1):
    if K % coins[i] == 0:
        cnt += K // coins[i]
        break
    else:
        cnt += K // coins[i]
        K -= (K // coins[i]) * coins[i]

print(cnt)

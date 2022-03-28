import sys
sys.stdin = open('input.txt')


# 홀수만 더하기
T = int(input())

for tc in range(1,T+1):
    arr = list(map(int, input().split()))
    total = 0
    for a in arr:
        if a%2 == 1:
            total += a
    print(f'#{tc} {total}')



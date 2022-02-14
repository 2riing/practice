import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    arr = list(map(int,input().split()))
    total = 0
    cnt = 0
    for a in arr:
        total += a
        cnt += 1
    avg = round(total/cnt)

    print(f'#{tc} {avg}')
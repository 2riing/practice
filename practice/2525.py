import sys
sys.stdin = open('input.txt')

H, M = map(int, input().split())
times = int(input())

if (M + times) > 59: # 만약 분이 60 이상이면
    if H + times//60 > 23: # 시간이 24 이상이면
        H += times//60 -23
        M += times%60 - 60
    else:
        H += times // 60 -23
        M += times%60 - 60
else: # 만약 M이 60 이하이면
    if H + times//60 > 23:
        H += times//60 -24
        M += times
    else:
        H += times // 60
        M += times

print(H, M)
import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    a,b = list(map(int, input().split()))

    if a == b:
        print(f'#{tc} =')
    elif a > b:
        print(f'#{tc} >')
    else:
        print(f'#{tc} <')

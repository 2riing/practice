import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    arr = list(map(int,input().split()))
    max_arr=0
    for i in range(len(arr)):
        if max_arr < arr[i]:
            max_arr = arr[i]

    print(f'#{tc} {max_arr}')
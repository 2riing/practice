import sys
sys.stdin=open('input.txt')

# 기본 입출력
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int,input().split()))

    # minmax arr의 0번 값으로 초기화
    max_num = arr[0]
    min_num = arr[0]

    # minmax 구하기
    for i in range(1, N):
        if arr[i] > max_num:
            max_num = arr[i]
        elif arr[i] < min_num:
            min_num = arr[i]

    # 출력
    print(f'#{tc} {max_num - min_num}')
import sys
sys.stdin = open('input.txt')

# M개의 합이 가장 큰 경우
# 가장 작은 경우

T = int(input())
for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    arr = list(map(int, input().split()))

    temp = 0
    num = 0
    for j in range(M):
        num += arr[j]
    max_sum, min_sum = num, num

    for i in range(N-M+1):
        temp = 0
        for j in range(M):
            temp += arr[i+j]
        if temp > max_sum:
            max_sum = temp
        if temp < min_sum:
            min_sum = temp

    print(f'#{tc} {max_sum - min_sum}')


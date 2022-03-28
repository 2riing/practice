import sys
sys.stdin = open('input.txt')

# 크로스 방향
def Cross():
    ni, nj = [1, -1, 0, 0] , [0, 0, 1, -1]
    result = []

    for i in range(N):
        for j in range(N):
            temp = 0
            for k in range(4):
                for l in range(1, M):
                    di, dj = i + ni[k]*l, j + nj[k]*l
                    if 0 <= di < N and 0 <= dj < N:
                        temp += arr[di][dj]
            result.append(temp + arr[i][j])
    return max(result)

# 대각선 방향
def Diagonal():
    ni, nj = [1, 1, -1, -1],[1, -1, 1, -1]
    result = []
    for i in range(N):
        for j in range(N):
            temp = 0
            for k in range(4):
                for l in range(1, M):
                    di, dj = i + ni[k] * l, j + nj[k] * l
                    if 0 <= di < N and 0 <= dj < N:
                        temp += arr[di][dj]
            result.append(temp + arr[i][j])
    return max(result)


# 기본 입력
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) # N*N배열 M은 스프레이의 세기
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 정답 출력
    answer = []
    answer.append(Cross())
    answer.append(Diagonal())
    print(f'#{tc} {max(answer)}')
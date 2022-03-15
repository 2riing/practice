import sys
sys.stdin = open('input.txt')

# 시작지점 찾는 함수
def findstart():
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                return i, j

# 위아래 양옆을 검사하는 함수
def Test(i, row, col):
    ni = dx[i]  # 좌우로 이동
    nj = dy[i]  # 위아래로 이동
    if  0<= row+nj <N and 0 <= col+ni <N and arr[row + nj][col + ni] == 0 : # 0이고, 범위를 벗어나지 않는다면
        row = row + nj
        col = col + ni
        arr[row][col] = 3 # 볼 수 있는 곳은 3으로 바꿔준다.
        return Test(i, row, col) # 계속 재귀로 반복해줌
    else: # 안되면 함수 종료
        return

# result 사각지대(0)을 찾는 함수
def countzero():
    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                cnt += 1
    return cnt  # 0의 개수를 세서 리턴(사각지대의 수)

# 오른쪽, 왼쪽, 위, 아래 (0, 1, 2, 3)
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

#입력 + 함수 실행 + 결과 출력
T = int(input())
for tc in range(1, T+1):
    N = int(input()) # N*N의 arr 입력될 것임
    arr = [list(map(int, input().split())) for _ in range(N)] # 지도 arr 입력
    row, col = findstart() # 2가 있는 시작지점 받아오기

    for i in range(4): # 오른쪽, 왼쪽, 위, 아래 (0, 1, 2, 3) 순으로 탐색
        Test(i, row, col) # 탐색 및 가능한 부분 3으로 변경 함수 실행

    result = countzero()

    # 출력
    print(f'#{tc} {result}')
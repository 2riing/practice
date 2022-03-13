import sys
sys.stdin = open('input.txt')

C, R = map(int, input().split()) # 가로 C * 세로 R
K = int(input()) # 이분의 자리 찾기
seat = [[0 for _ in range(C)] for _ in range(R)] # 가로 C 세로 R인 0 배열생성
x, y = -1, 0 # x,y 값 초기화
r, c = R, C # 반복 해줄 값
cnt = 0
k = 1
result = []

def Go(row, col, r, c, k, cnt):
    if cnt > C*R or cnt == K:
        return col+1, row+1
    else:
        for i in range(r):
            cnt += 1 # 해주고
            row += k # row 방향으로 k씩 증가하면
            seat[row][col] = cnt # 그 자리에 cnt한 숫자를 저장한다.
            if cnt == K:
                return col+1, row+1
        for _ in range(c-1):
            col += k
            cnt += 1
            seat[row][col] = cnt
            if cnt == K:
                return col+1, row+1
        k *= -1
        return Go(row, col, r - 1, c - 1, k, cnt)

if C * R >= K: # 만약에 찾는 범위가 C*R 배열안에 있다면
    result = Go(x, y, r, c, k, cnt) # 함수 실행
    print(*result, end= '')
else: # 없으면
    print(0, end ='') # print 0

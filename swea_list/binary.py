import sys
sys.stdin=open('input.txt')

T = int(input())
for tc in range(1, T+1):
    P, A, B = list(map(int, input().split()))

    def CntPage(num, P):
        l = 1; r = P
        cnt = 0
        while 1:
            mid = int((l+r)/2)

            if num == mid: # 숫자가 중간 값보다 왼쪽에 있을 경우
                cnt += 1
                return cnt
            elif num < mid:
                r = mid
                cnt += 1
            else:
                l = mid
                cnt += 1


    cntA, cntB = CntPage(A, P), CntPage(B, P)
    if cntA > cntB:
        result = 'B'
    elif cntA == cntB:
        result = '0'
    else:
        result = 'A'

    print(f'#{tc} {result}')
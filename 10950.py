
import sys


# 테스트 케이스 개수 T입력

T = int(input())

# 정수 A B를 입력
# A+B를 출력 

i = 0
while i < T:
    A, B = map(int, input().split())
    print(A+B)
    i += 1



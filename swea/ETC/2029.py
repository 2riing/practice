import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    num1, num2 = list(map(int, input().split()))
    print(f'#{tc} {num1//num2} {num1%num2}')

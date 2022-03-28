import sys
sys.stdin=open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, K = list(map(int, input().split()))

    for i in range(1,13):
        pass

    print(f'#{tc}')



    # 집합 A의 1~12까지의 수가 부부
    # N개의 원소를 가지고 있고 1,2,3 3개인데, 합이 6을 만족하는 것
    # 원소의 합이 K인것
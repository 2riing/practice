import sys
sys.stdin=open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M, K = list(map(int, input().split())) # M초에 K개의 붕어빵 N명의 사람
    people = list(map(int, input().split()))
    flag = 0
    sec = 0
    bbang = 0
    while 1:
        sec += 1
        if sec % 60 == 0:
            bbang += K
        for i in range(len(people)):
            if sec == people[i]:
                bbang -= 1
                if bbang < 1:
                    flag = 0
                    break
                elif bbang >= 1 and i == len(people)-1:
                    flag = 1
                    break



    print(f'{tc} {flag}')
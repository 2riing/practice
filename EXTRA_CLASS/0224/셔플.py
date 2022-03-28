import sys
sys.stdin=open('input.txt')


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    card = list(map(str, input().split()))

    C = len(card)
    bucket = []
    mid = int(len(card)/2)
    left = []
    right = []
    for i in range(0, mid):
        left.append(card[i])
    for i in range(mid, C):
        right.append((card[i]))

    print(left, right)

    for i in range(1, len(right)):
        bucket.append(left[i])
        bucket.append(right[i])
        if i ==


    # 앞에 절반은 홀수에 넣고
    # 뒤에 절반은 짝수에 넣는다.

    result = ' '.join(bucket)
    print(f'#{tc} {result}')
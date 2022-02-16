import sys
sys.stdin=open('../input.txt', encoding='utf-8-sig')

T = int(input())

for _ in range(T):
    tc, N = list(map(str, input().split()))
    arr = list(map(str, input().split()))

    chk = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    ck = [0]*10

    for i in range(len(arr)):
        for j in range(len(chk)):
            if arr[i]==chk[j]:
                ck[j] += 1

    print('\n'+tc)

    for i in range(len(ck)):
        if ck[i]>=1:
            result = (chk[i]+' ') * ck[i]
            print(result, end='')




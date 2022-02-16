import sys
sys.stdin=open('../input.txt', encoding='utf-8-sig')
T = int(input())
for tc in range(1,T+1):
    n = int(input())

    arr = [[0 for _ in range(n)] for _ in range(n)]
    print(arr)
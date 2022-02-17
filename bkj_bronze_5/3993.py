import sys
sys.stdin = open('input.txt')

chk = [1,1,2,2,2,8]
chess = list(map(int, input().split()))

for i in range(len(chk)):
    print(chk[i] - chess[i],end=' ')
